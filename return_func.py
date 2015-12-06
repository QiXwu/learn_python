# -*- coding: utf-8 -*-
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print f
print f()


#f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count1()
print f1()
print f2()
print f3()

#fix bugs
def count2():
    fs = []
    def f(j):
        def g():
            return j*j
    	return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()

print f1()
print f2()
print f3()
