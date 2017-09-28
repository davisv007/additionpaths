import functools


def memoize(func):
    cache = func.cache = {}

    @functools.wraps(func)
    def memoized_func(*args):
        key = str(args)
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]

    return memoized_func


@memoize
def recursive(n):
    return sum([recursive(n - i) for i in range(1, 4) if n - i >= 0]) if n != 0 else 1


def main():
    print(recursive(100))


main()
