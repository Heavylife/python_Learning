# 生成器函数
def fibonacci(n):
	if n < 2:
		yield n
	else:
		yield fibonacci(n-1) + fibonacci(n-2)
