import math


def get_distance_between(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def is_closer_than(a: tuple[float, float], b: tuple[float, float], radius: int) -> bool:
    return get_distance_between(a, b) <= radius
