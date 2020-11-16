import math
from itertools import count
from typing import List

data = [1.0, 2.0, 3.0, 4.0, 5.0]
list2 = [1.0, 2.0, 2.0, 4.0, 5.0]


def zcount(list: List[float]) -> float:
    return len(list)


def zmean(list: List[float]) -> float:
    mean = sum(list) / zcount(list)
    return float(mean)



def zmode(list: List[float]) -> float:

    mode = max(set(list), key=list.count)
    return mode


def zmedian(list: List[float]) -> float:

    sortedlist = sorted(list)
    n = len(list)
    index = (n -1) //2
    if n % 2 == 0:
        return float(sortedlist[index])
    else:
        return float((sortedlist[index] + sortedlist[index +1]) / 2.0)

def zvariance(list: List[float]) -> float:


    mean = zmean(list)

    return sum((x - mean) ** 2 for x in list) / zcount(list)


def zstddev(list: List[float]) -> float:

    var = zvariance(list)
    std_dev = math.sqrt(var)
    return round(std_dev, 2)


def zstderr(list: List[float]) -> float:
    return zstddev(list) / math.sqrt(zcount(list))


def zcorr(list: List[float], list2: List[float]) -> float:
    sum = 0
    for i in range(0, len(list)):
        sum += ((list[i] - zmean(list)) *(list2[i]-zmean(list2)))
    cov = sum / (zcount(list)-1)
    corr = cov / (zstddev(list) * zstddev(list2))
    return round(corr, 2)

