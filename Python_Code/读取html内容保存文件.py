import requests
import re
import pdfkit
import time
from playwright.sync_api import Playwright, sync_playwright, expect

# 目标网址
url = "https://www.cnblogs.com/yiruliu/p/14728088.html"
# F12 复制本地的UA信息
heads_data = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
def run(playwright: Playwright,path="screenshot.png") -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.screenshot(path=path, full_page=True)  # 截图
    print(page.title())
    page.wait_for_timeout(1000)
    context.close()
    browser.close()
# 调用访问请求
res_info = requests.get(url, headers=heads_data)
# print(res_info.text)
title_pattern = re.compile(r'<title>(.*?)</title>')
page_name = title_pattern.findall(res_info.text)[0]
print(page_name)
res_info.encoding = res_info.apparent_encoding
res = res_info.status_code
# 打印信息
html_path = './%s.html'%(page_name)
pdf_path = './%s.pdf'%(page_name)
img_path = '%s.png'%(page_name)
title = page_name
if res == 200:
    try:
        with open(html_path, mode='w', encoding='utf-8') as f:
            f.write(res_info.text)
        with sync_playwright() as playwright:
            run(playwright,img_path)
        # 配置wkhtmltopdf程序
        config = pdfkit.configuration(wkhtmltopdf='D:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        # 将html转成pdf
        pdfkit.from_file(html_path, pdf_path, configuration=config)
        print(f'{title}--保存成功')
        time.sleep(1)
    except Exception as e:
        print(e)

