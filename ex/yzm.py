import random

def yzm_fun():
	yzm = []  # 储存验证码
	yzm_str = ''
	while True:
		i = random.randint(65, 122)
		if 90<i<97:
			continue
		else:
			yzm.append(chr(i)) # 生成英文字母
			yzm.append(str(random.randrange(1,10)))
		if len(yzm) == 4: # 生成4个
			random.shuffle(yzm) # 打乱序列
			for i in yzm:
				print(i,end=' ')
				yzm_str = yzm_str+i
			user_yzm = input('请输入验证码：')
			if user_yzm.lower() == yzm_str.lower():
				print('验证成功')
				break
			else:
				print('验证码错误，请重新输入')
				yzm_fun() # 进入另外的一层循环
				break  # 必须加 ，跳出外层循环，因为yzm_fun()有循环，验证成功后的break只能跳出自己的循环

yzm_fun()