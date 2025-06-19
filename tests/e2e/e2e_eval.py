"""Test eval/exec commands."""

import os
from contextlib import redirect_stdout
from io import StringIO

from mqshell import MQTTShell
from tests.utils import wait_for_connect


def main():
    shell = MQTTShell()
    wait_for_connect(shell)

    # test with an expression that will be eval'd
    with StringIO() as buf, redirect_stdout(buf):
        shell.do_eval("'1 + 1'")
        output = buf.getvalue()
    assert output.strip() == "2", f"Unexpected output for eval: {output}"

    # test with a statement that will be exec'd
    cmd = """
        'with open("test_file.txt", "w") as f:
            f.write("Hello, World!")'
    """.strip()

    with StringIO() as buf, redirect_stdout(buf):
        shell.do_eval(cmd)
        output = buf.getvalue()
    assert output.strip() == "", f"Unexpected output for eval: {output}"

    # verify that the file was created
    with open("test_file.txt", "r") as f:
        content = f.read()
    assert content == "Hello, World!", f"Unexpected file content: {content}"
    
    # cleanup
    os.remove("test_file.txt")
    


if __name__ == "__main__":
    main()
    print("\033[1m\tOK\033[0m")
