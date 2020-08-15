from selenium import webdriver
import time
from docx import Document
url = 'https://item.jd.com/100006976889.html'
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get(url)
# for i in range(2, 100):   #也可以设置一个较大的数，一下到底
js = "var q=document.documentElement.scrollTop={}".format(5000)  #javascript语句
chrome.execute_script(js)
chrome.find_element_by_xpath('//li[@data-anchor="#comment"]').click()
time.sleep(2)
# js1 = "var q=document.documentElement.scrollTop={}".format(9500)
# chrome.execute_script(js1)
# time.sleep(5)
# js2 = "window.scrollTo(10000,10000)"
# chrome.execute_script(js2)
js1 = "var q=document.documentElement.scrollTop={}".format(9250)
js2 = "var q=document.documentElement.scrollTop={}".format(8000)
chrome.execute_script(js1)
document = Document()  #生成一个空的docx对象
for i in range(1, 4):
    print('------------正在打印第{}页-----------'.format(i))
    # time.sleep(5)
    texts = chrome.find_elements_by_xpath('//p[@class="comment-con"]')
    for text in texts:
        # with open('text', 'ab+') as f:
        #     f.write(bytes(text))
        # print(text.text)
        document.add_paragraph(text.text)
    document.save('spider.docx')
    element = chrome.find_element_by_xpath('//div[@class="ui-page"]/a[@class="ui-pager-next" and @clstag="shangpin|keycount|product|pinglunfanye-nextpage"]')
    chrome.execute_script("arguments[0].click();", element)
    chrome.implicitly_wait(5)
    # js2 = "var q=document.documentElement.scrollTop={}".format(8200)
    # chrome.execute_script(js2)
