import cProfile
import io
import pstats
import time


def profiler(sort_by: str):
    """A profiler decorator, adapted from:
        https://docs.python.org/3/library/profile.html
    by:
        https://www.youtube.com/watch?v=8qEnExGLZfY

    Arguments:
        @profiler('time')
        def any_funcion():
            some logic

    Options:
    @profiler(options):
        options: 'calls', 'cumulative', 'file', 'ncalls', 'pcalls', 'line', 'name', 'nfl', 'stdname'

    Returns:
        profiler -- Prints profiling results
    """

    def profile(fnc):
        def inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            retval = fnc(*args, **kwargs)
            pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
            ps.print_stats()
            print(s.getvalue())
            return retval

        return inner

    return profile


def inner():
    time.sleep(0.01)
    print("Hello world!")


@profiler("cumtime")
def run():
    for _ in range(10):
        inner()


if __name__ == "__main__":
    run()
