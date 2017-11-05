from bs4 import BeautifulSoup
import time,requests

# url = 'http://zhuanzhuan.58.com/detail/927173710593245195z.shtml?fullCate=5%2C38484%2C23094&fullLocal=1&from=pc&PGTID=0d305a36-0000-10ef-b57a-d257788c1612&ClickID=1'

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36Query String Parametersview sourceview URL encoded',
	'Cookie':'f=n; userid360_xml=483E0AB3B5990A9DABB27BC598EBC3F3; time_create=1512482091686; ipcity=cd%7C%u6210%u90FD; myfeet_tooltip=end; id58=c5/ns1naHXua+rSYjZIyAg==; als=0; wmda_uuid=a8aa1331b8196a7b1f76fa11b810bfab; wmda_new_uuid=1; commontopbar_myfeet_tooltip=end; bj58_id58s="TnR1aVV1QjNVbVFjODczMg=="; gr_user_id=c4a268dc-7d4b-4535-92ff-990e8923d56e; wmda_visited_projects=%3B1731916484865%3B2286118353409%3B1409632296065; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1508217296; Hm_lvt_e15962162366a86a6229038443847be7=1508217297; __utma=253535702.1774438488.1508217113.1508217113.1508221577.2; __utmz=253535702.1508221577.2.2.utmcsr=my.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/index/; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1508217343,1508846568; _ga=GA1.2.1774438488.1508217113; final_history=30501411873468%2C31772027898161%2C31407478756555%2C23578130502048%2C30644156025923; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1509107360; ppStore_fingerprint=FC2E59607A2DE91781ABAFE6878BD6731B01CDAA904BBD25%EF%BC%BF1509107359840; city=bj; 58home=bj; commontopbar_ipcity=cd%7C%E6%88%90%E9%83%BD%7C0; f=n; bj58_new_session=1; bj58_init_refer="http://bj.58.com/"; bj58_new_uv=3; sessionid=742d9560-0934-48c0-a5f4-39715a50d673; 58tj_uuid=747fdfe7-e341-4e2b-9d84-694fb9d1811e; new_session=0; new_uv=5; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.sogou.com%252Flink%253Furl%253DDOb0bgH2eKgAPooCRB_vL24YafSeot-j; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; xxzl_deviceid=mxzo0JMgCYttN3HjGpdBxW%2B2A3OyOGKzJuOu7gLVZo%2BbO5m1O8rgqWnMlqXqzG8b'
}
def get_onpage(url):
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')

	class_strs = soup.select('span:nth-of-type(4) > a')  # 类别
	titles = soup.select('div.box_left_top > h1')
	prices = soup.select('div.price_li > span > i')
	addresses = soup.select('div.palce_li > span > i')

	for class_str,title,price,address in zip(class_strs,titles,prices,addresses):
		data = {
			'class_str':class_str.get_text(),
			'title':title.get_text(),
			'price':price.get_text(),
			'address':address.get_text(),
		}
		print(data)
def get_pages():
	# infolist > div:nth-child(5) > table > tbody > tr:nth-child(18) > td.img > a
	urls = 'http://bj.58.com/pbdn/?PGTID=0d305a36-0000-1ddd-eb14-53c5a0a1a030&ClickID=1'
	links = []
	wb_data = requests.get(urls,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	# print(soup)
	link_ids = soup.find_all('a',onclick="clickLog('from=zzpc_infoclick');") # 发现这个里面有详情页面的特殊信息


	for link_id in link_ids:
		link = link_id.get('href').split('/')
		id = link[-1]
		links.append(id)
	links = set(links)  # 由于获取页面元素没选好 有相同元素 去掉相同的元素
	links = list(links)
	for i in links:
		url = 'http://zhuanzhuan.58.com/detail/'+str(i)
		get_onpage(url)
get_pages()




