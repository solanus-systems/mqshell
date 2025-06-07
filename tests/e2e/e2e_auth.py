"""Test authenticated connection."""

import os

from mqshell import MQTTShell
from tests.utils import wait_for_connect


def main():
    # FIXME: in CI the connection times out
    # See also https://github.com/solanus-systems/amqc/issues/16
    if os.getenv("CI") == "true":
        print("\033[1m\tSKIP\033[0m")
        return

    shell = MQTTShell(username="test_user", password="test_pass", use_ssl=True)
    wait_for_connect(shell)


if __name__ == "__main__":
    main()
    print("\033[1m\tOK\033[0m")
