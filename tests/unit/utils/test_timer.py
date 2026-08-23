from retaillake.utils.timer import Timer

import time


def test_timer_creation():
    timer = Timer()

    assert timer is not None


def test_timer_context_manager():

    with Timer() as timer:
        time.sleep(0.01)

    assert hasattr(timer, "elapsed")


def test_timer_elapsed_is_positive():

    with Timer() as timer:
        time.sleep(0.05)

    assert timer.elapsed >= 0


def test_timer_elapsed_is_float():

    with Timer() as timer:
        pass

    assert isinstance(timer.elapsed, float)


def test_timer_start_initialized():

    timer = Timer()

    with timer:
        pass

    assert timer.start is not None


def test_timer_multiple_usage():

    with Timer() as timer1:
        time.sleep(0.01)

    with Timer() as timer2:
        time.sleep(0.01)

    assert timer1.elapsed >= 0
    assert timer2.elapsed >= 0