from selenium import webdriver
import time

# account = input("请输入账号：")
# password = input("请输入密码：")
browser = webdriver.Chrome()
url = 'http://stu.1000phone.net/student.php/Public/login'

browser.get(url)
time.sleep(2)
browser.find_element_by_name("Account").send_keys('410222199504125533')
# browser.find_element_by_name("Account").send_keys(account)
browser.find_element_by_name("PassWord").send_keys('125533')
# browser.find_element_by_name("PassWord").send_keys(password)

browser.find_element_by_xpath('//div[@class="clearfix"]/button').click()

time.sleep(2)

browser.find_element_by_xpath('//ul[@class="submenu"]/li[position()=7]').click()

handles = browser.window_handles
browser.switch_to.window(handles[0])

browser.find_element_by_xpath('//tbody/tr/td[last()]/a').click()
time.sleep(2)
#填写评价 方括号中数字表示选项 1 为第一个选项 以此类推
#班主任评价
# browser.find_element_by_xpath('//input[@name="ew67wV"][1]').click()
# browser.find_element_by_xpath('//input[@name="7hMGSt"][1]').click()
# browser.find_element_by_xpath('//input[@name="BPJ5bQ"][1]').click()
# browser.find_element_by_xpath('//input[@name="ZzaH5k"][1]').click()
# browser.find_element_by_xpath('//input[@name="HV8Xel"][1]').click()
# browser.find_element_by_xpath('//input[@name="5t68tx"][1]').click()
# browser.find_element_by_xpath('//input[@name="432Gtr"][1]').click()
# browser.find_element_by_xpath('//input[@name="7KM2Ue"][1]').click()
# browser.find_element_by_xpath('//input[@name="HYOzt8"][1]').click()
#
# browser.find_element_by_id('NakdEA').send_keys("无")
# browser.find_element_by_id('addstudent').click()

#就业老师评价
# browser.find_element_by_xpath('//input[@name="NGso31"][1]').click()
# browser.find_element_by_xpath('//input[@name="vfoyu8"][1]').click()
# browser.find_element_by_xpath('//input[@name="vWGzB0"][1]').click()
# browser.find_element_by_xpath('//input[@name="gYVwdh"][1]').click()
# browser.find_element_by_xpath('//input[@name="3nnLRv"][1]').click()
# browser.find_element_by_xpath('//input[@name="6igUQl"][1]').click()
# browser.find_element_by_xpath('//input[@name="EGsa8o"][1]').click()
# browser.find_element_by_xpath('//input[@name="0F4jvG"][1]').click()
# browser.find_element_by_xpath('//input[@name="ytqNVr"][1]').click()
# #填写意见
# browser.find_element_by_id('fq3hTy').send_keys("无")
# browser.find_element_by_id('3v4JAF').send_keys("无")
# browser.find_element_by_id('addstudent').click()

#讲师评价
browser.find_element_by_xpath('//input[@name="WDgDBw"][1]').click()
browser.find_element_by_xpath('//input[@name="zTKCku"][1]').click()
browser.find_element_by_xpath('//input[@name="ic10lb"][1]').click()
browser.find_element_by_xpath('//input[@name="K2N8Cf"][1]').click()
browser.find_element_by_xpath('//input[@name="kKtEEF"][1]').click()
browser.find_element_by_xpath('//input[@name="mwrBBf"][1]').click()
browser.find_element_by_xpath('//input[@name="4HzU3n"][1]').click()
browser.find_element_by_xpath('//input[@name="Lp1pEJ"][1]').click()
browser.find_element_by_xpath('//input[@name="t2zJ83"][1]').click()
browser.find_element_by_xpath('//input[@name="yE7g2w"][1]').click()
browser.find_element_by_xpath('//input[@name="SzDgzZ"][1]').click()
browser.find_element_by_xpath('//input[@name="Arj3aA"][1]').click()
browser.find_element_by_xpath('//input[@name="xPzBtU"][1]').click()
#填写意见
browser.find_element_by_id('YIUrmG').send_keys("讲解清晰有条理")
browser.find_element_by_id('Nf8QDS').send_keys("无")

browser.find_element_by_id('addstudent').click()
#退出
browser.quit()
print("评价完成")