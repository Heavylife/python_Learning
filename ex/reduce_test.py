from functools import reduce
def f(x,y):
	return x+y

r1=reduce(f,[1,2,3,4,5])
print(r1)
# 这种情况可以用lambda f函数只用一次
ff = lambda x,y:x+y
r2=reduce(ff,[1,2,3,4,5])
print(r2)

r3=reduce(lambda x,y:x+y,[1,2,3,4,5])
print(r3)
foo=[2,18,9,22,17,24,8,12,27]
r4=filter(lambda x:x%3==0,foo)
r5=map(lambda x:x*2+10,foo)
r6=reduce(lambda x,y:x+y,foo)
print(r4)
print(r5)
print(r6)