"""Test utilities"""

import time
from contextlib import redirect_stdout
from io import StringIO

from mqshell import MQTTShell


def wait_for_connect(shell: MQTTShell):
    """Wait for confirmation that the shell has connected"""
    output = StringIO()
    tries = 0
    max_tries = 10
    with redirect_stdout(output):
        while tries < max_tries:
            shell.do_connect("test/device localhost")
            last = output.getvalue().strip().splitlines()[-1]
            if "MQTerm v" in last:
                break
            time.sleep(1)
            tries += 1
    if "MQTerm v" not in last:
        raise TimeoutError(f"Failed to connect after {max_tries} attempts")
