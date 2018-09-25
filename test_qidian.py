from selenium import webdriver
import time

url = 'https://www.qidian.com/'
key = input("请输入书名：")
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
browser = webdriver.PhantomJS()
browser.get(url)
#传入搜索关键字
browser.find_element_by_id('s-box').send_keys(key)
# print(browser.current_url)
#点击搜索
browser.find_element_by_id('search-btn').click()
time.sleep(2)
# print(browser.current_url)
#手柄切换
handles = browser.window_handles
# print(handles)
browser.switch_to.window(handles[1])
time.sleep(2)
# print(browser.current_url)
#点击选择书籍
browser.find_element_by_xpath('//a[@data-eid="qd_S04"][1]').click()
time.sleep(2)
handles = browser.window_handles
# print(handles)
browser.switch_to.window(handles[2])
# print(browser.current_url)
time.sleep(2)
#点击阅读
browser.find_element_by_id("readBtn").click()
handles = browser.window_handles
#点击关闭提示框
try:
    browser.find_element_by_id("j_closeGuide").click()
except Exception:
    pass
#死循环爬取内容，直到遇到vip章节
while True:
    #防止爬取过程中出现莫名错误
    try:
        title = browser.find_elements_by_class_name("j_chapterName")[0].text
        content = browser.find_elements_by_xpath('//div[@class="read-content j_readContent"]//p')
        #判断是否为vip章节
        vip = browser.find_elements_by_class_name('vip-limit-wrap')
        if vip:
            print("以下是vip章节")
            break
        else:
            with open('./book/%s.txt'%(key),'a',encoding='utf-8') as f:
                f.write(title + '\n')
                for i in content:
                    f.write(i.text+'\n')
                print(title)
            time.sleep(2)
            browser.find_element_by_id("j_chapterNext").click()
    except Exception:
        print("程序结束")
        browser.quit()
        break
