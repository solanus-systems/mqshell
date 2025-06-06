
from mqshell import MQTTShell
from tests.utils import wait_for_connect


def main():
    """Test the 'reboot' command in the MQTT shell."""
    # Connect
    shell = MQTTShell()
    wait_for_connect(shell)
    # output = StringIO()

    # FIXME: the mqterm stub doesn't come back up after this
    # # Execute a soft reboot
    # with redirect_stdout(output):
    #     shell.do_reboot()
    # last = output.getvalue().strip().splitlines()[-1]
    # assert (
    #     last == "Performing soft reboot"
    # ), f"Expected 'reboot' response 'Performing soft reboot', got '{last}'"

    # # Wait a bit to ensure the reboot is processed
    # wait_for_connect(shell)

    # Execute a hard reboot
    # with redirect_stdout(output):
    #     shell.do_reboot("--hard")
    # last = output.getvalue().strip().splitlines()[-1]
    # assert (
    #     last == "Performing hard reboot"
    # ), f"Expected 'reboot' response 'Performing hard reboot', got '{last}'"

    # # Wait a bit to ensure the reboot is processed
    # wait_for_connect(shell)


if __name__ == "__main__":
    main()
    print("\033[1m\tOK\033[0m")
