import requests
import re
# 目标网址
url = "https://www.cnblogs.com/yiruliu/p/14728088.html"
# F12 复制本地的UA信息
heads_data = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
# 调用访问请求
res_info = requests.get(url, headers=heads_data)
# print(res_info.text)
title_pattern = re.compile(r'<title>(.*?)</title>')
page_name = title_pattern.findall(res_info.text)[0]
print(page_name)
res_info.encoding = res_info.apparent_encoding
res = res_info.status_code
# 打印信息
if res == 200:
    with open('./%s.html'%(page_name), 'w', encoding='utf-8') as fp:
        fp.write(res_info.text)