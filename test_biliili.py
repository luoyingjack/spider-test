import json
import requests
import urllib3
urllib3.disable_warnings()
headers = {
    'Host':'bangumi.bilibili.com',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie':'finger=81df3ec0; LIVE_BUVID=AUTO1215271442898090; fts=1527144308; sid=i2tbtygk; buvid3=05ED7B3D-7167-44BB-9053-795055B16046101594infoc; rpdid=kspxiiwwlqdosimoppkww',
}
def loadhtml(url,name):
    response = requests.get(url=url, verify=False, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    content = json.loads(html, encoding='utf-8')
    a = content["result"]["data"]
    for i in a :
        try:
            vip = i["badge"]
        except Exception as e:
            vip = '免费'
        name_url = i["title"]
        url = i["link"]
        with open('./url_bilibili/%s.txt'%(name),'a',encoding='utf-8') as f:
            print(vip+"***"+name_url+"\n"+url,file=f)


if __name__ == "__main__":
    # 番剧
    url_1 = 'https://bangumi.bilibili.com/media/web_api/search/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=3&st=1&sort=0&page=%d&season_type=1&pagesize=20'
    # 国创
    url_2 = 'https://bangumi.bilibili.com/media/web_api/search/result?season_version=-1&is_finish=-1&copyright=-1&season_status=-1&pub_date=-1&style_id=-1&order=3&st=4&sort=0&page=%d&season_type=4&pagesize=20'
    type = int(input("番剧请输入1，国产请输入2："))
    page_start = int(input('请输入想要爬取起始页数：'))
    page_end = int(input('请输入想要爬取结束页数：'))

    if type == 1:
        for i in range(page_start,page_end+1):
            url = url_1%(i)
            name = '番剧'
            loadhtml(url,name)
    elif type == 2:
        for i in range(page_start, page_end+1):
            url = url_2 % (i)
            name = '国产'
            loadhtml(url,name)
