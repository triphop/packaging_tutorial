import platform


def add_one(number):
    return number + 1


def get_host_name() -> str:
    return platform.node()
