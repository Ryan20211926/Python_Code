import re
import os
# 读取Markdown文件
href_count =0
file_count =0
def find_href_link(filename):
    global  href_count
    current_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    # 正则表达式用于匹配图片链接
    image_pattern = re.compile(r'!\[.*\]\((https?:\/\/[^\)]+)\)')
    # 搜索所有匹配项
    print("序号：%s,当前%s文件"%(file_count,filename))
    for match in image_pattern.finditer(content):
        current_count +=1
        href_count+=1
        print("\t序号(%s)"%(current_count),match.group(1))
    else:
        if current_count>0:
            print("\t当前%s文件连接数:%s"%(filename,current_count))
def traverse_directory(directory):
    global file_count
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_count += 1
                file_path = os.path.join(root, file)
                # print(file_count,file_path)  # 这里可以根据需求对文件路径进行处理
                find_href_link(file_path)
if __name__ == '__main__':
    md_filepath = r"E:\Ryan\我的云笔记_new"# "Markdown 文件所在目录的路径: "
    traverse_directory(md_filepath)
    print("文件总链接数",href_count)
    print("文件总数",file_count)