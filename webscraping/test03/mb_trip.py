from bs4 import BeautifulSoup
import requests

headers = {
	'User_Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36',
	'Cookie':'TAUnique=%1%enc%3AQiAEhnMv%2Bmw9lvsTxM41vLCO8bmOmH%2BRriV%2BKKs7nYY2jHwltRJPGQ%3D%3D; TASSK=enc%3AAGv50HK1uGjXsrE4d87KZ3o5Yk0jMskPS25d1JLol2wd04tkEQXcPKJ%2Ftk468yOEk4AitLhg0%2BXUrAEQTMoC95shqPWLBtSpdLnl6ywZMFuqAV4G8bdjxhvkWOLH2%2FDziw%3D%3D; __gads=ID=a5eeadc4b0f82c6e:T=1506856197:S=ALNI_MYFLCmdpfz_H2tAYUh0ovo6ZvbMag; TAAuth3=3%3Aa2f14a61153bc9ebc4074398f84ba8c2%3AAJKdGmxWGIjiK2rfJkS0XJyrw33IHEAy%2Fsk98XGrm6uMfSQ%2FYsyisQoLGObpTIBZtQpabjEDA2H8rllSmfYtrT%2BAGoXRPRkSg0fA81WjHGyVNgJeDpfMGAxnVYk51Z5eNVHjYTrtXcl36K4%2F%2FiHIZqDAZ%2FoBmc%2B1IAj92KGx9mio4mD91wOPOgcl%2Fy%2F5KwCVQw%3D%3D; _ga=GA1.2.1763355713.1506856195; VRMCID=%1%V1*id.13416*llp.%2F-a_suppm%5C.www__2E__sogou__2E__com-a_supkw%5C.%257Bkwywordid%257D-a_supsc%5C.s-m13416-a_supai%5C.1634263037-a_supci%5C.95826543*e.1510402071878; _jzqy=1.1506856196.1509797298.2.jzqsr=sogou|jzqct=TripAdvisor.jzqsr=sogou|jzqct=tripadviser; _jzqckmp=1; _smt_uid=59d0cd04.422ef8dc; CommercePopunder=SuppressAll*1509797344880; ServerPool=B; ki_t=1506858526899%3B1509841247143%3B1509844808719%3B3%3B51; ki_r=; _jzqx=1.1506858525.1509844809.3.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.jzqsr=tripadvisor%2Ecn|jzqct=/attractions; _qzja=1.653991809.1506856196348.1509841048075.1509844808725.1509844956300.1509845761098..0.0.59.6; _qzjb=1.1509844808725.3.0.0.0; _qzjc=1; _qzjto=6.2.0; _jzqa=1.2904062268497291000.1506856196.1509841048.1509844809.6; _jzqc=1; _jzqb=1.3.10.1509844809.1; TAReturnTo=%1%%2FAttraction_Review-g60763-d267031-Reviews-Manhattan_Skyline-New_York_City_New_York.html; interstitialCounter=2; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C3%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7Cmds%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; MobileLastViewedList=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; taMobileRV=%1%%7B%2210028%22%3A%5B60763%5D%7D; roybatty=TNI1625!AFLEV0ay4g7cVGxeJAuri6Ayog8hdtsT7ImwUq1qgWXDx9Nnvb0%2BfrFdJ5b%2Bj5SRPi7AAOvZsv7ht4SJoAlYGyP8hcliNqlpZeNWwWc3CieeotvJD1Kf2dUZLw4g4%2FFNZ2UxdQtHLHnRldmuf251sJk5AF6JTzMeVDMjHHOF4BJW%2C1; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.105127_308l267031_308l60763_308; TASession=%1%V2ID.8B93A44E4E5ECBA25626FF4A7CF7A722*SQ.40*LP.%2FSaves*LS.DemandLoadAjax*GR.95*TCPAR.18*TBR.69*EXEX.46*ABTR.53*PHTB.27*FS.25*CPU.66*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.E069877FE3CBDE982782E1C2EF24E5EB*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.60763; TAUD=LA-1509841023095-1*RDD-1-2017_11_04*LG-4811625-2.0.F.*LD-4811626-.....; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1509797298,1509841048; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1509845858',
}

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST'

web_data = requests.get(url,headers=headers)
soup = BeautifulSoup(web_data.text,'lxml')

titles = soup.find_all('div',class_='listing_title')
imgs = soup.find_all('img',class_='photo_image',width = '180')
cates = soup.find_all('div',class_='p13n_reasoning_v2')

for title,img,cate in zip(titles,imgs,cates):
	data = {
		'title':title.get_text().strip(),
		'img':img.get('src'),
		'cate':list(cate.stripped_strings),
	}
	print(data)
