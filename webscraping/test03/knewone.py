from bs4 import BeautifulSoup
import requests
import time

url = 'https://knewone.com/?page='

def get_page(url,data=None):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text,'lxml')
	# print(soup)
	titles = soup.select('h4.title > a')
	images = soup.select('a.cover-inner > img')
	links = soup.select('h4.title > a')
	# print(iamges)
	if data == None:
		for title,image,link in zip(titles,images,links):
			data = {
				'title':title.get('title'),
				'image':image.get('src'),
				'link':link.get('href'),
			}
			print(data)

def get_more_pages(start,end):
	for i in range(start,end+1):
		get_page(url+str(i))
		time.sleep(2)
get_more_pages(1,5)
