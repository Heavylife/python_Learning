from bs4 import BeautifulSoup
import requests
'''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_SORT_WRAPPER'
web_data = requests.get(url)
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
'''
headers = {
	'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	'Cookie': 'TAUnique=%1%enc%3AQiAEhnMv%2Bmw9lvsTxM41vLCO8bmOmH%2BRriV%2BKKs7nYY2jHwltRJPGQ%3D%3D; TASSK=enc%3AAGv50HK1uGjXsrE4d87KZ3o5Yk0jMskPS25d1JLol2wd04tkEQXcPKJ%2Ftk468yOEk4AitLhg0%2BXUrAEQTMoC95shqPWLBtSpdLnl6ywZMFuqAV4G8bdjxhvkWOLH2%2FDziw%3D%3D; __gads=ID=a5eeadc4b0f82c6e:T=1506856197:S=ALNI_MYFLCmdpfz_H2tAYUh0ovo6ZvbMag; TAAuth3=3%3Aa2f14a61153bc9ebc4074398f84ba8c2%3AAJKdGmxWGIjiK2rfJkS0XJyrw33IHEAy%2Fsk98XGrm6uMfSQ%2FYsyisQoLGObpTIBZtQpabjEDA2H8rllSmfYtrT%2BAGoXRPRkSg0fA81WjHGyVNgJeDpfMGAxnVYk51Z5eNVHjYTrtXcl36K4%2F%2FiHIZqDAZ%2FoBmc%2B1IAj92KGx9mio4mD91wOPOgcl%2Fy%2F5KwCVQw%3D%3D; taMobileRV=%1%%7B%2210028%22%3A%5B60763%5D%7D; _ga=GA1.2.1763355713.1506856195; ServerPool=B; VRMCID=%1%V1*id.13416*llp.%2F-a_suppm%5C.www__2E__sogou__2E__com-a_supkw%5C.%257Bkwywordid%257D-a_supsc%5C.s-m13416-a_supai%5C.1634263037-a_supci%5C.95826543*e.1510402071878; _jzqy=1.1506856196.1509797298.2.jzqsr=sogou|jzqct=TripAdvisor.jzqsr=sogou|jzqct=tripadviser; _jzqckmp=1; _smt_uid=59d0cd04.422ef8dc; CommercePopunder=SuppressAll*1509797344880; _jzqx=1.1506858525.1509801005.2.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.jzqsr=tripadvisor%2Ecn|jzqct=/tourism-g60763-new_york_city_new_york-vacations%2Ehtml; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_308l105127_308*RS.1; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C3%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmds%2C%2C-1%7CRBAPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; roybatty=TNI1625!ANILKowCt3NeF4BIxrXP%2BTa5P0tUnAv3N%2Fou4ge3falmom7wmNvUAWqYKREPooLbkfi110bfZ3MOUo9K3RlAm6HASwi1Vk6dkeNk9PouygYiStgLT3Di0RJ2LzfobnMEyULilWf61P7zS3%2FeEBeJRkuQX4JYGOHjk0P%2BYkhpQr1P%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1509797298; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1509801090; _qzja=1.653991809.1506856196348.1509797297576.1509801005006.1509801045441.1509801090217..0.0.48.4; _qzjb=1.1509801005006.3.0.0.0; _qzjc=1; _qzjto=7.2.0; _jzqa=1.2904062268497291000.1506856196.1509797298.1509801005.4; _jzqc=1; ki_t=1506858526899%3B1509797299504%3B1509801090270%3B2%3B44; ki_r=; TASession=%1%V2ID.37BC8F9833AFD25B7D5F7C07B4E808EB*SQ.49*MC.13416*LR.http%3A%2F%2Fwww%5C.sogou%5C.com%2Fbill_cpc%3Fv%3D1%26q%3DWJe0lllllylx%26query%3Dtripadviser%26ml%3D39%26mc%3D127%26ma%3D343%2C0%2C408%2C187%2C306%2C173%2C1903%2C974%26block%3D539%2C172%2C-1%2C-1*LP.%2F-a_suppm%5C.www__2E__sogou__2E__com-a_supkw%5C.%257Bkwywordid%257D-a_supsc%5C.s-m13416-a_supai%5C.1634263037-a_supci%5C.95826543*PR.1434%7CUserReview*LS.DemandLoadAjax*GR.44*TCPAR.28*TBR.15*EXEX.30*ABTR.82*PHTB.94*FS.54*CPU.74*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.E069877FE3CBDE982782E1C2EF24E5EB*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127; TAUD=LA-1509797271787-1*RDD-1-2017_11_04*LG-3814690-2.1.F.*LD-3814691-.....; _jzqb=1.3.10.1509801005.1',
}
url_save = 'https://www.tripadvisor.cn/Saves/869846'
web_data = requests.get(url_save,headers=headers)
soup = BeautifulSoup(web_data.text,'lxml')
print(soup)
titles = soup.select('div.saves-location-details ui_media > div.location_summary > a')
print(titles)
images = soup.select('div.carousel_images')
cates = soup.select('div.detail')
rates = soup.select('')
print(titles,images,cates)
'''


'''