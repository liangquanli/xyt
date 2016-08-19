#!/usr/bin/env python
# encoding: utf-8
from cProfile import Profile


def runcall(statement, filename=None, *args, **kwargs):
    """Run statement under profiler, supplying your own globals and locals,
    optionally saving results in filename.

    statement and filename have the same semantics as profile.run
    """
    prof = Profile()
    result = None
    try:
        try:
            result = prof.runcall(statement, *args, **kwargs)
        except SystemExit:
            pass
    finally:
        if filename is not None:
            prof.dump_stats(filename)
        else:
            result = prof.print_stats(-1)
    return result


def monitor_profile(func):
    import functools

    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):

        return runcall(func, "%s.stat" % func.__name__, *args, **kwargs)

        # def tmpfunc():
        #     return func(*args, **kwargs)
        # # 直接用run是不行的
        # cProfile.runctx("tmpfunc()", globals(), locals(), "%s.stat" % func.__name__)
    return func_wrapper
