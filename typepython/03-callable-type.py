# https://mypy.readthedocs.io/en/stable/kinds_of_types.html
# * Callable types


def add(a: int, b: int) -> int:
    return a + b

print(add(1, "3"))