from nose.tools import *
from hawkweed.monads.io import IO, CachedIO

def test_io():
    with open("tests/test_file.txt") as f:
        linegen = IO(f.readline)
        res1 = linegen.ret()
        res2 = linegen.ret()
        assert_not_equal(res1, res2)

def test_cached_io():
    with open("tests/test_file.txt") as f:
        linegen = CachedIO(f.readline)
        res1 = linegen.ret()
        res2 = linegen.ret()
        assert_equal(res1, res2)
