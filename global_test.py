# -*- coding: UTF-8 -*- 

x = 50

def func():
    global x
    print 'x的值是', x 
    x = 2
    print'全局变量x改为', x

func()
print 'x的值是', x 


def scopetest():
    var=6;
    print(var)#
    def innerFunc():
        print(var)#look here
    innerFunc()
    
var=5 
print(var)
scopetest()
print(var)