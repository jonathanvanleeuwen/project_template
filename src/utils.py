import signal


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
