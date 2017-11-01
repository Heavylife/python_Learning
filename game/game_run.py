from printmap import print_map
import random
user_names = ['aaa']
game_man = {'HP':100,'GJL':70,'FYL':56} # 储存英雄属性
game_direction = ['w','s','a','d'] # 方向上下左右
def apple(hp):
	hp += 10
	return hp
def bomb(hp):
	hp -= 10
	return hp

def move(eventlist): # 操作方向
	game_manx = random.randint(1, 9)
	game_many = random.randint(1, 9)
	print_map(game_manx, game_many)  # 打印坐标位置

	while True:
		user_direction = input('请输入英雄行驶的方向（wsad：上下左右）：')
		if user_direction == 'w' and game_many > 1:
			game_many = game_many - 1
		elif user_direction == 's'and game_many < 9:
			game_many = game_many + 1
		elif user_direction == 'a' and game_manx > 1:
			game_manx = game_manx - 1
		elif user_direction == 'd' and game_manx < 9:
			game_manx = game_manx + 1
		else:
			print('超出边界，重新输入移动方向')
			continue
		print_map(game_manx, game_many)  # 打印坐标位置
		randomEvent(game_manx, eventlist)
		if game_man['HP'] == 0:
			print('您的血条为0，GAME OVER!')
			break
# 随机事件产生
def randomEvent(game_manx,eventlist):
	for i in range(1,10):
		if game_manx == i:
			random_event = random.choice(eventlist)
			if random_event == apple:
				game_man['HP']=apple(game_man['HP'])
				print('恭喜您捡到一个苹果，HP+10，现在为 %d'%game_man['HP'])
			elif random_event == bomb:
				game_man['HP']=bomb(game_man['HP'])
				print('可喜可贺您踩到一个砸蛋，HP-10，现在为 %d'%game_man['HP'])
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

		eventlist = [apple, bomb] # 用于随机事件
		move(eventlist)
		break
	else:
		print('您输入的账号不存在')
		user_login = input('请注册账号：') #暂时不考虑密码
		user_names.append(user_login)
		continue