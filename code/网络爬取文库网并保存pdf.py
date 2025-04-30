"""
爬取步骤：
1.确定需求：
    爬取的内容及内容来源
2.发送请求：
    请求url地址--文章列表url
    请求方式--get
    请求参数字段添加--User-Agent
3.获取数据：
    获取数据--响应体文本数据（网页源代码）
4.解析数据
    解析方法：re正则表达式/css选择器/xpath
    解析提取内容--文章url
5.发送请求
    请求url地址--文章url
    请求方式--get
    请求参数字段添加--User-Agent
6.获取数据：
    获取数据--响应体文本数据（网页源代码）
7.解析数据：
    解析方法：re正则表达式/css选择器/xpath
    解析提取内容--提取文章内容/文章标题
8.保存数据：
    需要先把获取的内容保存为html文件，然后使用htmltopdf将html转成PDF

re正则可以直接提取字符串数据--response.text就是html字符串数据
parsel 需要先把html字符串转成可解析的对象
"""
import time

import requests  # 数据请求模块
import re  # 正则表达式模块
import parsel  # 数据解析模块
import os  # 文件操作模块
import pdfkit  # 转成pdf

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
{article}
</body>
</html>    
"""

html_filename = 'html\\'  # 定义文件夹名称
# 判断该文件夹是否存在，不存在则创建
if not os.path.exists(html_filename):
    os.mkdir(html_filename)

pdf_filename = 'pdf\\'  # 定义文件夹名称
# 判断该文件夹是否存在，不存在则创建
if not os.path.exists(pdf_filename):
    os.mkdir(pdf_filename)

for page in range(1, 10):
    # 文章列表的url地址
    url = f'https://www.chinawenwang.com/zlist-66-{page}.html'
    # 请求头【字典形式】 User-Agent：表示浏览器基本信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 发送请求
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    # 解析数据
    # 用re正则表达式获取文章url地址 .*? 可以匹配任意字符，除了"\n"
    # 如果需要匹配"\n“则需要在后面加上re.S
    # url_list = re.findall(' <h2><a href="(.*?)" class="juhe-page-left-div-link">(.*?)</a></h2>', response.text, re.S)
    # .*?-- .可以匹配任意字符（除了\n） *匹配前一个字符0个或多个 ? 非贪婪匹配模式
    # url_list = re.findall(' <h2><a href="(.*?)" class="juhe-page-left-div-link">(.*?)</a></h2>', response.text)
    url_list = re.findall(' <h2><a href="(.*?)" class="juhe-page-left-div-link">', response.text)
    # 正则匹配出来的数据，返回的是列表，这里返回的每个元素都是由文章标题和url地址组成的元组
    for link in url_list:
        response_1 = requests.get(url=link, headers=headers)
        # 将html字符串数据转成可解析对象
        selector = parsel.Selector(response_1.text)
        title = selector.css('.content-page-header-div h1::text').get()
        # 文件名中不允许包含一些特殊字符，需进行替换
        title = re.sub(r'[\/:*?"<>|]', '_', title)
        # print(f'title-->{title}')
        # 获取包含html标签
        content = selector.css('.content-page-main-content-div').get()
        article = html_str.format(article=content)
        html_path = html_filename + title + '.html'  # html文件的路径/文件名/后缀
        pdf_path = pdf_filename + title + '.pdf'  # pdf文件的路径/文件名/后缀
        try:
            with open(html_path, mode='w', encoding='utf-8') as f:
                f.write(article)
            # 配置wkhtmltopdf程序
            config = pdfkit.configuration(wkhtmltopdf='D:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            # 将html转成pdf
            pdfkit.from_file(html_path, pdf_path, configuration=config)
            print(f'{title}--保存成功')
            time.sleep(1)
        except Exception as e:
            print(e)
            continue
    if len(url_list) < 25:
        break
