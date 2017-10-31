
def print_map(x, y):
	print('——————————您的英雄在 * 处——————————')
	for i in range(10):
		for j in range(10):
			if i == y and j == x:  # 打印角色初始位置
				print('*', end='\t')
			else:
				print('#', end='\t')
		print()
