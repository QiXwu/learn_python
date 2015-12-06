# -*- coding: utf-8 -*-

# from __future__ import division

from functools import reduce
# def str2int(s):
# 	def char2num(s):
#  	 	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# 	return reduce(lambda x, y: x * 10 + y, map(char2num, s))


CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

#字符串转整数
def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

#首字母大写
def normalize(name):
	return name.capitalize()
	#return name.upper()[0]+name.lower()[1:]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print L2

#可以接受一个list并求积
from functools import reduce
def prod(L):
	return reduce(lambda x,y : x * y , L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


#字符串转小数

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = {}
    point[0] = 0
    def to_float(f, n):
        if n == -1:
            point[0] = 1.0
            return f
        if point[0] == 0:
            return f * 10 + n
        else:
            point[0] = point[0] * 10
            return f + n / point[0]
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))