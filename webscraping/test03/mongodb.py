import pymongo

client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
walden = client['walden'] # 建立名称
sheet_line = walden['sheet_line'] # 创建表单

path = 'C:/Users/Administrator/Desktop/walden.txt'
with open(path,'r') as f:
	lines = f.readlines()
	for index,line in enumerate(lines):
		data = {
			'index':index,
			'line':line,
			'words':len(line.split())
		}
		sheet_line.insert_one(data)

for item in sheet_line.find({'words':{'$lt':5}}):
	print(item)