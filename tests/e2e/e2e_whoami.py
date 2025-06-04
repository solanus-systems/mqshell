from contextlib import redirect_stdout
from io import StringIO
from time import sleep

from mqshell import MQTTShell


def main():
    """Test the 'whoami' command in the MQTT shell."""
    # Connect
    sleep(1)
    shell = MQTTShell()
    output = StringIO()
    with redirect_stdout(output):
        shell.do_connect("test/device localhost")
    last = output.getvalue().strip().splitlines()[-1]
    assert "MQTerm v" in last, f"Unexpected response to 'connect': {last}"

    # Send the "whoami" command
    with redirect_stdout(output):
        shell.do_whoami(None)
    last = output.getvalue().strip().splitlines()[-1]
    assert (
        last == shell.client_id
    ), f"Expected 'whoami' response '{shell.client_id}', got '{last}'"


if __name__ == "__main__":
    main()
    print("\033[1m\tOK\033[0m")
