_running = True


def is_running():
    return _running


def stop():
    global _running
    _running = False