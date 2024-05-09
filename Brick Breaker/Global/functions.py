from time import time


def add_tuple(first: tuple, second: tuple):
    return [first[i] + second[i] for i in range(len(first))]


class Timer:
    def __init__(self, wait: float) -> None:
        self.wait = wait
        self.start_time = time
        self.waiting = True

    def start():
        pass
