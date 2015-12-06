# -*- coding: utf-8 -*-

# python 3可用：
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def _not_divisible(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列

# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

#求X以内素数
def jud(n):
	if n == 1:
		return False
	for i in range(2,n):
		if n % i ==0:
			return False
		else:
			pass
	return True

out = filter (jud,xrange(1,10))
print list(out)

#剔除X以内素数
y=filter(lambda x: any(map(lambda p: x % p == 0, range(2, x))), range(1, 10))

print y

# y=filter(lambda x: any(map(lambda p: x % p == 0, range(2, x))), range(2, 101))
# print y


# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# output = filter(is_palindrome, range(1, 1000))
# print(list(output))