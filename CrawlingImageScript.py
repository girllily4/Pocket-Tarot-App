import requests
import re



'''
Date: February 20, 2019
Name: Yiwen Liu
Function: encoding html using requests library
Return: HTML Text
'''
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"

'''
Function: Download Image
'''
def getImage(html):
	# find all image's url
	listImageUrl = re.findall(r'//.+\.gif', html)
	image = listImageUrl[0]
	with open('0 愚人.gif','ab') as handler:
		handler.write('http:'+image)
		handler.close()
	#ir = requests.get(image)
	#sz = open('')
	print(image)

	# Download Image
	# for url in listImageUrl:
	# 	file = open(str(i)+'.gif','wb')
	# 	r = requests.open('http:' + url)
	# 	buf = r.read()
	# 	file.write(buf)
	# 	i += 1
	# 	print(buf)

	
#def getImage(url):
	#pic_content = requests.get(url,stream=True).content
    #open('filename','wb').write(pic_content)

if __name__== "__main__":

	url = "https://www.meiguoshenpo.com/taluopai/jieshi/"
	html = getHtmlText(url)
	getImage(html)
	#输出结果
	print()