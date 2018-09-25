import urllib
import urllib.request

url = 'http://stu.1000phone.net/student.php/Index/index'
url_1 = 'http://stu.1000phone.net/student.php/Index/evaluate'
headers = {
    'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
    'Referer':'http://stu.1000phone.net/student.php/Public/login',
    'Accept-Language':'zh-CN',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; InfoPath.3)',
    'Accept-Encoding':'',
    'Host':'stu.1000phone.net',
    'Cookie':'PHPSESSID=s5s2vjoipatpa9sbqkse6ntgj0; StuInfo=think%3A%7B%22StuId%22%3A%2292309%22%2C%22StuNumber%22%3A%22SH170350009%22%2C%22IDcard%22%3A%22410222199504125533%22%2C%22StuName%22%3A%22%25E6%259D%258E%25E5%2582%25B2%25E6%259D%25B0%22%2C%22Cid%22%3A%221773%22%7D'
}
request = urllib.request.Request(url=url_1,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)


