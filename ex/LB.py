def hello_conf(prefix): # 闭包函数 内嵌函数必须调用上一级函数的变量
	def hello(name):
		print(prefix,name)
	return hello  # 必须返回内嵌函数
a = hello_conf('Good Morning!') # a为函数hello
print(a.__name__) # hello
print(id(a)) # 2036476639840
a('yy')
a('wf')

b = hello_conf('Good Afternoon!')
print(a.__name__) # hello
print(id(b)) # 2036476639976  地址不一样
b('jack')

c = hello_conf('Good Morning!') # c为函数hello
print(c.__name__) # hello
print(id(c)) # 2728478866152