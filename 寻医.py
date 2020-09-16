import requests
from lxml import etree
from fake_useragent import UserAgent
import pandas as pd
headers = {
    "User-agent": UserAgent().random
}
# url='http://club.xywy.com/small_322.htm'
url='http://club.xywy.com/small_322.htm'
def urls():
    base_urls = []
    for i in range(1,10):
        page_url = 'http://club.xywy.com/list_322_all_{}.htm'
        response = requests.get(page_url.format(i), headers=headers)
        response.encoding = 'gbk'
        html = response.text #获取页面代码
        e = etree.HTML(html)
        c = e.xpath('//table//a[@target="_blank" and @class="btn-a hov_clor"]/@href')
        # print(c)
        # return c
        base_urls.append(c)
    return base_urls
    # print(base_urls)
# for x in urls():
#     print(x)
# bases_urls = urls()
def parase_url(url):
    response = requests.get(url, headers=headers)  # 请求页面
    response.encoding = 'gbk'
    html = response.text  # 获取页面代码
    e = etree.HTML(html)
    info = {}
    sexs = e.xpath('//span[@class="User_newbg User_fticon"]')
    c = e.xpath('normalize-space(//div[@class="graydeep User_quecol pt10 mt10"]/text())')
    infos = []
    for sex in sexs:
        infos.append(sex.tail.strip())
    info['性别'] = infos[0]
    info['年龄'] = infos[1]
    # if c == '':
    #     c = e.xpath('//div[@class="graydeep User_quecol pt10 mt10"]/text()')
    #     info['问题'] = c[1]
    # else:
    info['问题'] = c
    # print(info)
    return info

first_url = urls()
m=pd.DataFrame({'性别': 'x', '年龄': 'y', '问题': 'z'},index=[1],columns=['性别', '年龄', '问题']
)
x=0
for second_url in first_url:
    y=0+x
    x+=20
    for third_url in second_url:
        # print(third_url)
        try:
            # parase_url(third_url)
            # print(parase_url(third_url))
            y+=1
            z = pd.DataFrame(parase_url(third_url),index=[y],columns=['性别', '年龄', '问题'])
            m = m.append(z, ignore_index=True)
        except:
            continue
print(m)
m.to_excel('mms.xlsx')
''''''
