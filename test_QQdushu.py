# -*- coding: utf-8 -*-  
__author__ = 'jack'
__date__ = '2018/6/13 16:52'

from selenium import webdriver
import time

url = 'http://book.qq.com/'
key = input("请输入书名：")
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Cookie':'RK=lTj92Jllen; pgv_pvi=9994931200; tvfe_boss_uuid=7c6542d1f7741d77; eas_sid=N1A582n1l9I8m878l4D5U7A9Z8; pac_uid=1_511794867; luin=o0511794867; lskey=000100002baacc94004b08583e88125c9e6d4af48cbb82116e0cd8b2d7bdb0b21a884604165dc944ea654df9; o_cookie=511794867; PHPSESSID=m38v59lf8foisi4lhg2tlokos4; pgv_si=s9524129792; _qpsvr_localtk=0.013174500612973317; ied_rf=book.qq.com/search/index/type/all/wd/%E9%BE%99%E6%97%8F%E2%85%A4.html; uin=o0511794867; skey=@bBxuIU3Fs; pt2gguin=o0511794867; ptisp=cnc; ptcz=5f778e388e78d724504395ffa3aa11d9592bb40f4124f88f83aa75ea6466da28; wxuid=511794867; pubtoken=czo4OiJNTmFUUUpZciI7; csguid=511794867; pgv_pvid=673432676; pgv_info=pgvReferrer=&ssid=s7762619376'
}
browser = webdriver.Chrome()

browser.get(url)
#传入搜索关键字
browser.find_element_by_id('searchInputBySite').send_keys(key)
# print(browser.current_url)
#点击搜索
browser.find_element_by_id('searchBySiteBtn').click()
time.sleep(2)
# print(browser.current_url)
#手柄切换
# handles = browser.window_handles
# print(handles)
# browser.switch_to.window(handles[1])
time.sleep(2)
# print(browser.current_url)
#点击阅读第一章
browser.find_element_by_xpath('//div[@id="searchResult"]/div[1]//a[@class="active"]').click()
handles = browser.window_handles
# print(handles)
browser.switch_to.window(handles[1])
time.sleep(3)
#死循环爬取内容
while True:
    #防止爬取过程中出现莫名错误
    try:
        title = browser.find_element_by_xpath('//h1[@class="story_title"]').text
        content = browser.find_elements_by_xpath('//div[@class="bookreadercontent"]//p')
        with open('./book/%s.txt'%(key),'a',encoding='utf-8') as f:
            f.write('\n'+title+'\n')
            for i in content[:-1]:
                f.write(i.text+'\n')
            print(title)
        time.sleep(2)
        browser.find_element_by_id('rightFloatBar_nextChapterBtn').click()
    except Exception:
        print("程序结束")
        browser.quit()
        break
