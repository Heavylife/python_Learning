from bs4 import BeautifulSoup
info = [] # 储存信息
with open('web/new_index.html','r') as web_data:
	Soup = BeautifulSoup(web_data,'lxml')
	images = Soup.select('div.main-content > ul > li > img')
	titles = Soup.select('div.main-content > ul > li > div.article-info > h3 > a')
	rates = Soup.select('div.main-content > ul > li > div.rate > span')
	cates = Soup.select('div.main-content > ul > li > div.article-info > p.meta-info') # 因为评价不止一个 所以用上一级标签
	descs = Soup.select('div.main-content > ul > li > div.article-info > p.description')
	# print(images,titles,rates,cates,descs,sep='\n****************************\n')
for image,title,rate,cate,desc in zip(images,titles,rates,cates,descs):
	data = {
		'image':image.get('src'),
		'title':title.get_text(),
		'rate':rate.get_text(),
		'cate':list(cate.stripped_strings),
		'desc':desc.get_text()
	}
	info.append(data)
for i in info:  # 遍历字典info i的值是顺序取其中的字典
	if float(i['rate']) > 3:
		print(i['title'],i['cate'])



