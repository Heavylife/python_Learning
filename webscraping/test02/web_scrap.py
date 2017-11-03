from bs4 import BeautifulSoup
info = []
# 打开本地网页文件
with open('web\index.html') as web_data:
	Soup = BeautifulSoup(web_data,'lxml')
	images = Soup.select('div.thumbnail > img') # 图片
	prices = Soup.select('div.caption > h4.pull-right') # 价格
	titles = Soup.select('div.caption > h4 > a') # 标题
	reviews = Soup.select('div.ratings > p.pull-right') # 评分数
	stars = Soup.select('div.ratings > p:nth-of-type(2)') # 星级 保留到上一级

	print(stars)
for image,price,title,review,star in zip(images,prices,titles,reviews,stars):
	data = {
		'image':image.get('src'),
		'price':price.get_text(),
		'title':title.get_text(),
		'review':review.get_text(),
		'star':len(list(star.find_all('span',class_="glyphicon glyphicon-star"))) # find_all() 第一个参数是标签，第二个是css样式 由于返回值是列表 就可以统计其出现的次数来确定星星多少次了
	}
	# print(data)
	info.append(data)
# 统计大于3星，评分数大于18的
for i in info:
	if int(i['star']) > 3 and int(i['review'][:2])> 18: # 评分人数大于18，星级大于3
		print(i['title'],i['price'])

