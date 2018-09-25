from selenium import webdriver
import time

url = 'http://www.biquge.com.tw/'
key = input("请输入书名：")
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
browser = webdriver.Chrome()
browser.get(url)
#传入搜索关键字
browser.find_element_by_id('wd').send_keys(key)
# print(browser.current_url)
#点击搜索
browser.find_element_by_id('sss').click()
time.sleep(2)
# print(browser.current_url)
#手柄切换
handles = browser.window_handles
# print(handles)
browser.switch_to.window(handles[1])
time.sleep(2)
# print(browser.current_url)
#点击阅读第一章
browser.find_element_by_xpath('//div[@id="list"]/dl/dd[1]/a').click()
handles = browser.window_handles
# print(handles)
browser.switch_to.window(handles[1])
#死循环爬取内容，直到遇到vip章节
while True:
    #防止爬取过程中出现莫名错误
    try:
        title = browser.find_element_by_xpath('//div[@class="bookname"]/h1').text
        content = browser.find_element_by_id('content').text.replace('\n', '')
        with open('./book/%s.txt'%(key),'a',encoding='utf-8') as f:
            f.write(title)
            f.write(content.replace('    ', '\n')+'\n\n')
            print(title)
        time.sleep(2)
        browser.find_element_by_xpath('//div[@class="bottem1"]/a[4]').click()
    except Exception:
        print("程序结束")
        browser.quit()
        break
