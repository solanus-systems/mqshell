import os
from contextlib import redirect_stdout
from io import StringIO
from time import sleep

from mqshell import MQTTShell


def main():
    """Test file operations in the MQTT shell."""
    # Connect
    sleep(1)
    shell = MQTTShell()
    output = StringIO()
    with redirect_stdout(output):
        shell.do_connect("test/device localhost")
    last = output.getvalue().strip().splitlines()[-1]
    assert "MQTerm v" in last, f"Unexpected response to 'connect': {last}"

    # Create a file and stream it to the terminal
    file_contents = "This is a test file.\n"
    with open("test_file.txt", "w") as f:
        f.write(file_contents)
    size_bytes = os.path.getsize("test_file.txt")
    with redirect_stdout(output):
        shell.do_cp("test_file.txt dest_filename.txt")
    sleep(2)
    last = output.getvalue().strip().splitlines()[-1]
    assert last == str(size_bytes), (
        f"Expected 'cp' response to be {size_bytes}, got {last}"
    )
    assert os.path.exists("dest_filename.txt"), "File was not created successfully."
    assert os.path.getsize("dest_filename.txt") == size_bytes, (
        "File size mismatch after copy."
    )

    # Check that the file appears in the file list
    with StringIO() as buf, redirect_stdout(buf):
        shell.do_ls(".")
        output = buf.getvalue()
    assert "dest_filename.txt" in output, f"File not found in 'ls' output: {output}"

    # Read the file content
    with StringIO() as buf, redirect_stdout(buf):
        shell.do_cat("dest_filename.txt")
        output = buf.getvalue()
    assert output == "This is a test file.", f"expected file content: {file_contents}, got: {output}"


if __name__ == "__main__":
    try:
        main()
    finally:
        # Cleanup
        os.remove("test_file.txt")
        os.remove("dest_filename.txt")
    print("\033[1m\tOK\033[0m")
