from contextlib import redirect_stdout
from io import StringIO
from os import path, remove
from time import sleep

import esptool

from mqshell import MQTTShell


def main():
    """Test the 'ota' command in the MQTT shell."""
    # Connect
    sleep(1)
    shell = MQTTShell()
    output = StringIO()
    with redirect_stdout(output):
        shell.do_connect("test/device localhost")
    last = output.getvalue().strip().splitlines()[-1]
    assert "MQTerm v" in last, f"Unexpected response to 'connect': {last}"

    # Analyze the fixture firmware file
    output = StringIO()
    with redirect_stdout(output):
        esptool.main(["image_info", "tests/fixtures/firmware.app-bin"])
    esptool_info_in = output.getvalue().strip().splitlines()[-1]

    # Run OTA command
    output = StringIO()
    with redirect_stdout(output):
        shell.do_ota("tests/fixtures/firmware.app-bin")
    last = output.getvalue().strip().splitlines()[-1]
    assert int(last), "Response to 'ota' command should be bytes written"
    assert path.exists("partition.bin"), "Partition file not created"

    # Analyze output file
    output = StringIO()
    with redirect_stdout(output):
        esptool.main(["image_info", "partition.bin"])
    esptool_info_out = output.getvalue().strip().splitlines()[-1]

    # Compare the two outputs
    assert (
        esptool_info_in == esptool_info_out
    ), f"Firmware analysis differs: {esptool_info_in} != {esptool_info_out}"

    # Clean up
    if path.isfile("partition.bin"):
        remove("partition.bin")


if __name__ == "__main__":
    main()
    print("\033[1m\tOK\033[0m")
