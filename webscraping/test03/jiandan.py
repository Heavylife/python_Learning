from bs4 import  BeautifulSoup
import urllib.request,time,requests

url = 'http://jandan.net/ooxx/page-'


def get_data(url):
	count = 0
	headers = {
		# 由于网站有反爬，所以需要这个参数，不然获取不到网页信息
		# 伪装成是人在浏览
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36Name'

	}
	download_links = []
	web_data = requests.get(url,headers=headers) # 请求网页
	soup = BeautifulSoup(web_data.text,'lxml') # 以'lxml'方式解析网页
	download_file = 'E://S/data_download/jiandan/ooxx/'

	for image in soup.find_all('img'):
		data='http:'+image.get('src')
		download_links.append(data)
		# print(download_links)

	for item in download_links:
		urllib.request.urlretrieve(item,download_file+item[-8:])
		count +=1
		print('Done {} pic'.format(count))

def get_datas(start,end): # 获取所有页面的url
	for i in range(start,end): # 需要爬取的页面
		urls = url+str(i)
		get_data(urls)
		time.sleep(2) # 间隔2S 防止被封
get_datas(80,90)