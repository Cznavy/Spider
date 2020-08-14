import requests
import re
import os
from fake_useragent import UserAgent
headers = {
    "User-agent": UserAgent().random
}
dir_name = 'Image1'  # 设置文件夹的名字
if not os.path.exists(dir_name):  # os模块判断并创建
    os.mkdir(dir_name)
for i in range(30, 120, 30):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%A3%8E%E6%99%AF&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E9%A3%8E%E6%99%AF&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1597107443831='.format(i)
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    base_urls = re.findall(r'"thumbURL":"(.*?).jpg"', html)
    for base_url in base_urls:
            filename = base_url.split('/')[-1]+'.jpg'
            with open(dir_name+'/'+filename, 'wb') as f:
                htmls = requests.get(base_url)
                f.write(htmls.content)