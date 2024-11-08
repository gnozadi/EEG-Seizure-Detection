import pickle

import collections
import math

import numpy
import numpy as np
from scipy.stats import *


def mean(x):  # 1 - Statistical
    return np.mean(x, axis=1)


def median(x):  # 2 - Statistical
    return np.median(x, axis=1)


def std(x):  # 3 - Statistical
    return np.std(x, axis=1)


def skw(x):  # 4 - Statistical
    return skew(x, axis=1)


def krt(x):  # 5 - Statistical
    return kurtosis(x, axis=1)


def max(x):  # 6 - Statistical
    return np.max(x, axis=1)


def min(x):
    return np.min(x, axis=1)


def var(x):
    return np.var(x, axis=1)

def shannon_i(x):  # 7 - Entropy(1)
    shannon_entropy = 0
    counts = collections.Counter([item for item in x])
    n = len(x)
    for a in counts:
        n_i = counts[a]
        p_i = n_i / n
        entropy_i = p_i * (math.log(p_i, 2))
        shannon_entropy += entropy_i
    return shannon_entropy


def shannon(x):
    arr = []
    for i in range(len(x)):
        arr.append(shannon_i(x[i]))
    return np.array(arr)


def log_energy_i(x):  # 8 - Entropy(2)
    n = 4097
    i = 1
    sum = 0
    while i < n:
        s_n = math.pow(x[i], 2)
        if s_n != 0:
            sum += math.log(s_n, 10)
        i += 1
    return sum


def log_energy(x):
    arr = []
    for i in range(len(x)):
        arr.append(log_energy_i(x[i]))
    return np.array(arr)


def renyi_i(x):  # 9 - Entropy(3)
    counts = collections.Counter([item for item in x])
    a = 2
    sum = 0
    for a in counts:
        p_i = counts[a] / len(x)
        sum += p_i
    return 1 - sum


def renyi(x):
    arr = []
    for i in range(len(x)):
        arr.append(renyi_i(x[i]))
    return np.array(arr)


def norm_i(x):  # 10 - Entropy(4)
    h = 1.1
    sum = 0
    for i in range(len(x)):
        sum += math.pow(abs(x[i]), h)
    return sum


def norm(x):
    arr = []
    for i in range(len(x)):
        arr.append(norm_i(x[i]))
    return np.array(arr)


def ptp(x):
    min_i = np.min(x, axis=1)
    max_i = np.max(x, axis=1)
    return max_i - min_i


def zc_i(x):
    count = 0
    for i in range(len(x)):
        if x[i] == 0:
            count += 1
    return count


def zc(x):
    arr = []
    for i in range(len(x)):
        arr.append(zc_i(x[i]))
    return np.array(arr)


def negative_sum_i(x):
    sum = 0
    for i in range(len(x)):
        if x[i]<0:
            sum += x[i]
    return sum


def negative_sum(x):
    arr = []
    for i in range(len(x)):
        arr.append(negative_sum_i(x[i]))
    return np.array(arr)


def feature_engineering(x):
    out = np.vstack((median(x), mean(x), std(x), skw(x), krt(x), max(x), min(x), var(x), shannon(x),
                    log_energy(x), renyi(x), norm(x), ptp(x), zc(x), negative_sum(x)))
    return out.transpose()


def selectFeature(i, x):
    if i == 1:
        return median(x), 'median'
    elif i == 2:
        return mean(x), 'mean'
    elif i == 3:
        return std(x), 'standard deviation'
    elif i== 4:
        return skw(x), 'skewness'
    elif i == 5:
        return krt(x), 'kurtosis'
    elif i == 6:
        return max(x), 'max'
    elif i == 7:
        return min(x), 'min'
    elif i == 8:
        return var(x), 'variance'
    elif i == 9:
        return shannon(x), 'shannon'
    elif i == 10:
        return log_energy(x), 'log energy'
    elif i == 11:
        return renyi(x), 'renyi'
    elif i == 12:
        return norm(x), 'norm'
    elif i == 13:
        return ptp(x), 'point-to-point'
    elif i == 14:
        return zc(x), 'zero crossing'
    elif i == 15:
        return negative_sum(x), 'negative sum'
    else:
        return None


x = pickle.load(open('x.pkl', 'rb'))
print(feature_engineering(x).shape)