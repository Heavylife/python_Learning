import time
def deco(func):
	def wrapper():
		startT = time.time()
		func()
		endT = time.time()
		print("It's %f ms" % ((endT - startT) * 1000))
	return wrapper
@deco # 等同myfunc =deco(myfunc)
def myfunc():
	print('start......')
	time.sleep(1.7)
	print('End.....')

print('myfunc is ',myfunc.__name__)
#myfunc =deco(myfunc)   变成装饰器函数
print('myfunc is ',myfunc.__name__)
myfunc() # 单独执行