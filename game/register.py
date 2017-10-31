"""
soft locked beta_0.1
"""
import os
count = 0
while True:
	if os.path.isfile('locked.log'): # 检查是否存在Locked文件，存在就锁定软件
		print('locked')
		break
	user_name = input('login:')
	password = input('password:')
	count+=1
	if user_name == 'yang' and password == '1234':
		pass
	else:
		if count == 3:
			open('locked.log','w').write(user_name)
			print('Locked by %s'%(user_name))
			break
		continue # 输入错误次数没有到三次时跳过继续执行
	print('welcome!')