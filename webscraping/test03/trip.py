from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_SORT_WRAPPER'
url_saves = 'https://www.tripadvisor.cn/Saves/869846'
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]

headers = {
	'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	'Cookie':'TAUnique=%1%enc%3AQiAEhnMv%2Bmw9lvsTxM41vLCO8bmOmH%2BRriV%2BKKs7nYY2jHwltRJPGQ%3D%3D; TASSK=enc%3AAGv50HK1uGjXsrE4d87KZ3o5Yk0jMskPS25d1JLol2wd04tkEQXcPKJ%2Ftk468yOEk4AitLhg0%2BXUrAEQTMoC95shqPWLBtSpdLnl6ywZMFuqAV4G8bdjxhvkWOLH2%2FDziw%3D%3D; __gads=ID=a5eeadc4b0f82c6e:T=1506856197:S=ALNI_MYFLCmdpfz_H2tAYUh0ovo6ZvbMag; TAAuth3=3%3Aa2f14a61153bc9ebc4074398f84ba8c2%3AAJKdGmxWGIjiK2rfJkS0XJyrw33IHEAy%2Fsk98XGrm6uMfSQ%2FYsyisQoLGObpTIBZtQpabjEDA2H8rllSmfYtrT%2BAGoXRPRkSg0fA81WjHGyVNgJeDpfMGAxnVYk51Z5eNVHjYTrtXcl36K4%2F%2FiHIZqDAZ%2FoBmc%2B1IAj92KGx9mio4mD91wOPOgcl%2Fy%2F5KwCVQw%3D%3D; taMobileRV=%1%%7B%2210028%22%3A%5B60763%5D%7D; _ga=GA1.2.1763355713.1506856195; VRMCID=%1%V1*id.13416*llp.%2F-a_suppm%5C.www__2E__sogou__2E__com-a_supkw%5C.%257Bkwywordid%257D-a_supsc%5C.s-m13416-a_supai%5C.1634263037-a_supci%5C.95826543*e.1510402071878; _jzqy=1.1506856196.1509797298.2.jzqsr=sogou|jzqct=TripAdvisor.jzqsr=sogou|jzqct=tripadviser; _jzqckmp=1; _smt_uid=59d0cd04.422ef8dc; CommercePopunder=SuppressAll*1509797344880; _jzqx=1.1506858525.1509801005.2.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.jzqsr=tripadvisor%2Ecn|jzqct=/tourism-g60763-new_york_city_new_york-vacations%2Ehtml; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_308l105127_308*RS.1; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C3%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmds%2C%2C-1%7CRBAPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7C; ki_t=1506858526899%3B1509797299504%3B1509802128461%3B2%3B49; ki_r=; ServerPool=B; roybatty=TNI1625!ABLUTWhcs%2Fh5q2VJE8p5JajZqf1%2Fa%2Bxb1zBCFS3AkzvRaKWODJ5PtZiN87IPCWPCn9HrUYHu53cMB9HZOT%2BtKjA3iyp8JOOhJudvOpGCVRmxz9P53kdfux04AaxcoLe4506kXKkp4VmaIKYY0zLNYYgjQPjd1EibSY7voipgfrgM%2C1; TASession=%1%V2ID.8B93A44E4E5ECBA25626FF4A7CF7A722*SQ.8*LP.%2FSaves*LS.DemandLoadAjax*GR.95*TCPAR.18*TBR.69*EXEX.46*ABTR.53*PHTB.27*FS.25*CPU.66*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.E069877FE3CBDE982782E1C2EF24E5EB*FA.1*DF.0*TRA.true; TAUD=LA-1509841023095-1*RDD-1-2017_11_04*LG-27259-2.1.F.*LD-27260-.....; _qzja=1.653991809.1506856196348.1509801005006.1509841048075.1509841048075.1509841074904..0.0.55.5; _qzjb=1.1509841048074.2.0.0.0; _qzjc=1; _qzjto=2.1.0; _jzqa=1.2904062268497291000.1506856196.1509801005.1509841048.5; _jzqc=1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1509797298,1509841048; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1509841075; _jzqb=1.2.10.15098410',

}

def get_attractions(url,data=None):
	web_data = requests.get(url)
	time.sleep(3)
	soup = BeautifulSoup(web_data.text,'lxml')
	titles = soup.select('div.listing_title > a[target="_blank"]')
	cates = soup.select('div.p13n_reasoning_v2')
	images = soup.select('img[width="180"]')
	# print(titles,cates,images)
	for title,cate,image in zip(titles,cates,images):
		data = {
			'title':title.get_text(),
			'cate':list(cate.stripped_strings),
			'image':image.get('src'),
		}
		print(data)

def get_favs(url,data=None):
	web_data = requests.get(url_saves,headers=headers)
	soup = BeautifulSoup(web_data.text,'lxml')
	#print(soup)
	titles = soup.select('a.title')
	images = soup.select('div.carousel_images')
	cates = soup.select('div.detail')

	if data == None:
		for title,image,cate in zip(titles,images,cates):
			data = {
				'title':title.get_text(),
				'image':image.get('src'),
				'cate':list(cate.stripped_strings)
			}
			print(data)
for single_url in urls:
	get_attractions(single_url)