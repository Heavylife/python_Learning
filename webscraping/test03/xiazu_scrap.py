from bs4 import BeautifulSoup
import requests
import time
url = 'http://dl.xiaozhu.com/fangzi/20155190103.html'
# urls = ['http://dl.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,14)]

def get_data(url): # 获取单页详情的信息
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text,'lxml')
	data = {}

	titles = soup.select('div.pho_info > h4 > em')
	addresses = soup.select('div.pho_info > p > span')
	prices = soup.select('div.day_l > span')
	images = soup.select('img#curBigImage')
	mem_imgs = soup.select('div.member_pic > a > img') # 照片
	mem_icos = soup.select('div.member_pic > div') # 性别
	#print(titles,addresses,prices,images,mem_imgs,mem_icos)

	for title,address,price,image,mem_ico,mem_img in zip(titles,addresses,prices,images,mem_icos,mem_imgs):
		data = {
			'title':title.get_text(),
			'address':address.get_text().strip(),
			'price':price.get_text(),
			'image':image.get('src'),
			'mem_ico':mem_ico.get('class'),
			'mem_imgs':mem_img.get('src'),
		}
		# print(type(mem_ico.get('class'))) 检测数据类型
		m_sex = mem_ico.get('class')
		if m_sex[0] == 'member_ico':
			m_sex[0] = 'male' # 男性
		else:
			m_sex[0] = 'fmale' # 女性
	return data
def get_page_links(numbers): # 输入爬取的页面数量
	all_pages = [] # 存储所有的详情页面
	time.sleep(3)

	for i in range(numbers):
		each_page = 'http://dl.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) # 找到要爬的所有页面
		# print(each_page)
		wb_data = requests.get(each_page)
		soup = BeautifulSoup(wb_data.text,'lxml') # 解析每个页面，发现详情页面http://dl.xiaozhu.com/fangzi/3216928829.html
		# id号存在div.favorite这个标签中
		# print(soup)

		links = soup.select('div.favorite') # #page_list > ul > li:nth-child(8) > div.favorite.lodge_9647413763.wsc_ico
		for link in links:
			link_id = link.get('al')
			all_pages.append('http://dl.xiaozhu.com/fangzi/{}.html'.format(link_id)) # 将所有的详情页面存储起来
		for each_page_xi in all_pages: # 遍历所有的详情页面并且爬取信息
			all_data = get_data(each_page_xi)

get_page_links(1)