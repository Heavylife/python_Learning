import urllib.request
import http.cookiejar
import urllib.parse

def getList():
	url = 'http://cx.cnca.cn/rjwcx/checkCode/rand.do?d=1510062084718'

	headers = {
		'Referer':'http://cx.cnca.cn/rjwcx/web/cert/publicCert.do?progId=10&title=%E8%AE%A4%E8%AF%81%E7%BB%93%E6%9E%9C%0A%09%20%20%20%20%20%20%20%20',
		'User - Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	}

	urllib.request.urlretrieve('http://cx.cnca.cn/rjwcx/checkCode/rand.do?d=1510062084718', 'code.png')
	code = int(input('请输入验证码：'))
	data = {
		'certNumber':'',
		'orgName':'漳州灿坤实业有限公司',
		'queryType':'public',
		'checkCode':code,
	}

	data = urllib.parse.urlencode(data)
	req = urllib.request.Request(url,data,headers)
	html = urllib.request.urlopen(req).read()

	print(html)
