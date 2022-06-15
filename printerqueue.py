from queue import *


def add_jobs(l):
    q = Queue(l)
    return q


if __name__ == "__main__":
    q = add_jobs(["boss", "underling", "minion"])
    print(q.length())
