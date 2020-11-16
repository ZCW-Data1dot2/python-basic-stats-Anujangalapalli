import unittest

from statzcw.basicstat import *


class Basicstat_Test(unittest.TestCase):
    def test_basicstat(self):
        data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
        data1 = [1.0, 2.0, 2.0, 4.0, 5.0]

        assert zcount(data0) == 5
        assert zmean(data0) == 3.0
        assert zvariance(data0) == 2.0
        assert zmedian(data0) == 3.5
        assert zmedian(data1) == 3.0

    def stat_test(self):
        data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
        data1 = [1.0, 2.0, 2.0, 4.0, 5.0]
        try:
            assert zvariance(data0) == 2.5
            assert zstddev(data0) == 3
            assert zstderr(data1) == 2.0
            assert zcorr(data0, data1) == 1.21
        except AssertionError as e:
            print(e)

