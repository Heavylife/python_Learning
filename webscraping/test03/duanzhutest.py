import requests
import pymongo
from bs4 import BeautifulSoup

def get_page(url,urls):
	url = 'http://bj.xiaozhu.com/fangzi/4697847613.html'
	headers = {
		'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
		'Cookie':'_ga=GA1.2.718212504.1507276078; gr_user_id=1ff97680-8618-4008-a049-f68a92390e0f;abtest_ABTest4SearchDate=b; xzuuid=c5035fd3;__utmt=1;__utma=29082403.718212504.1507276078.1509859698.1510322736.5;__utmb=29082403.4.10.1510322736;__utmc=29082403;__utmz=29082403.1510322736.5.3.utmcsr=sogou|utmccn=%E5%93%81%E7%89%8C%E8%AF%8D|utmcmd=cpc|utmctr=%E6%88%90%E9%83%BD%20%E5%B0%8F%E7%8C%AA%E7%9F%AD%E7%A7%9F|utmcct=sem; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=75418872-ed0d-4cbb-afba-fcac01c4e53f',
		'Referer': urls
	}

	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	#print(soup)

	titles = soup.select('h4 em')[0].text
	#print(titles)
	prices = soup.select('div.day_l > span')[0].text
	#print(prices)
	addresses = soup.select('span.pr5')[0].text.strip()
	#print(addresses)
	host_names = soup.select('h6 a[title]')[0].text
	#print(host_names)
	host_males = soup.select('div.member_pic > div')[0].get('class')[0]
	#print(host_males)

	data = {
		'price':prices,
		'title':titles,
		'address':addresses,
		'host_name':host_names,
		'host_male':host_males,
	}
	return data

def get_items(data):
	client = pymongo.MongoClient('localhost',27017)
	duanzhu = client['duanzhu']
	sheet_line = duanzhu['sheet_line']  # 创建表单

	for item in data:
		sheet_line.insert_one(item)
	for item in sheet_line.find({'price': {'$lt': 500}}):
		print(item)
def get_pages(start,end):

	for i in range(start,end+1):
		urls = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i))

		wb_datas = requests.get(urls)
		soup = BeautifulSoup(wb_datas.text,'lxml')

		pages = soup.find_all('a',target="_blank",class_='resule_img_a')
		for url in pages:
			url = url.get('href')
			data = get_page(url,urls)
			get_items(data)
get_pages(1,2)