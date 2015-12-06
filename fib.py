#菲波纳切数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b 
        a, b = b, a + b
        n = n + 1
    #return 'OK'    


g = fib(6)

while True:
    try:
    	x = next(g)
    	print x
    except StopIteration :
		print ('Generator return value:')
		break

#杨辉三角
def triangles():
    l = [1]
    yield l
    l = [1,1]
    yield l    
    while True:        
        l1 = l[1:]        
        for n in range(len(l1)):
            l[n] = l1[n]+l[n]
        l = [1]+l
        yield l
#杨辉三角
def triangles():
    c = [1]
    while 1:
        yield c
        a,b=[0]+c,c+[0]
        c=[a[i]+b[i] for i in range(len(a))]

yh = triangles()