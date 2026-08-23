from retaillake.runtime.recovery import RecoveryManager


def test_recovery():

    recovery = RecoveryManager()

    recovery.initialize()

    print("Recovery Test Passed")


if __name__ == "__main__":

    test_recovery()