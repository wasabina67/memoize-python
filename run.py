import time
from typing import Callable, Dict, TypeVar

T = TypeVar("T")


def memoize(f: Callable[[T], T]) -> Callable[[T], T]:
    cache: Dict[T, T] = {}

    def _wrapper(n: T) -> T:
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return _wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    start = time.time()

    for i in range(500):
        print(fibonacci(i + 1))

    elapsed_time = round(time.time() - start, 3)
    print(f"\nElapsed time: {elapsed_time}")


if __name__ == "__main__":
    main()
