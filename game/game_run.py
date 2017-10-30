user_names = ['aaa']
game_man = {'HP':100,'GJL':70,'FYL':56} # 储存英雄属性
game_direction = ['w','s','a','d'] # 方向上下左右
while True:
	user_logup = input('请输入账号：')
	if user_logup in user_names:
		print('欢迎登陆')
		user_input_name = input('请输入游戏角色名称：')
		if not user_input_name :
			game_man['name'] = 'Player1'
		else:
			game_man['name'] = user_input_name
		print(game_man)

		game_manx = 4
		game_many = 5 # 角色的初始坐标
		# 判断英雄行驶方向
		while True:
			user_direction = input('请输入英雄行驶的方向（wsad：上下左右）：')
			if user_direction == 'w':
				game_many = game_many - 1
			elif user_direction == 's':
				game_many = game_many + 1
			elif user_direction == 'a':
				game_manx = game_manx - 1
			elif user_direction == 'd':
				game_manx = game_manx + 1
			else:
				print('英雄没有移动')

			# 地图
			for i in range(10):
				for j in range(10):
					if i == game_many and j == game_manx: # 打印角色初始位置
						print('*',end='\t')
					else:
						print('#',end='\t')
				print()
	else:
		print('您输入的账号不存在')
		user_login = input('请注册账号：') #暂时不考虑密码
		user_names.append(user_login)
		continue