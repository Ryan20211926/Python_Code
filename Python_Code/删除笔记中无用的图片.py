import re
import os
# 读取Markdown文件
href_count =0
file_count =0
href_list =[]
del_img_list = []
del_img_count =0
total_chuli_count =0
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"文件 {filename} 删除成功！")
    else:
        print(f"文件 {filename} 不存在。")

def find_href_link(filename):
    global  href_count
    current_count = 0
    Ryan_current_count = 0
    other_current_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    # 正则表达式用于匹配图片链接
    image_pattern = re.compile(r'!\[.*\]\((https?:\/\/[^\)]+)\)')
    # 搜索所有匹配项
    print("序号：%s,当前%s文件" % (file_count, filename))
    for match in image_pattern.finditer(content):
        current_count +=1
        href_count+=1
        href_info = match.group(1)
        # print(href_info.find("ryan-1257879454.cos.ap-beijing"))
        # print("当前文件:%s" % filename)
        if href_info.find("ryan-1257879454.cos.ap-beijing")>0:
            Ryan_current_count+=1
            href_img_info = href_info.replace("https://ryan-1257879454.cos.ap-beijing.myqcloud.com/img/", "")
            print("\t序号(%s):我的图片" % (Ryan_current_count),href_img_info,href_info)
            href_list.append(href_img_info)
        else:
            other_current_count +=1
            global total_chuli_count
            total_chuli_count += 1
            print("\t序号(%s):需要处理的" % (other_current_count), href_info)
    # else:
    #     print("当前文件:%s的总连接数:%s"%(filename,current_count))
    # print("序号：%s,当前%s文件" % (file_count, filename))
    # else:
        # print("序号：%s,当前%s文件" % (file_count, filename))
        # if current_count>0:
            # print("序号：%s,当前%s文件" % (file_count, filename))
            # print("\t当前%s文件连接数:%s"%(filename,current_count))

def traverse_directory(directory):
    global file_count
    for root, dirs, files in os.walk(directory):
        for file in files:
            # print(root,file)
            # print((".obsidian" not in file))
            if file.endswith('.md') and (".obsidian" not in root) :
                file_count += 1
                file_path = os.path.join(root, file)
                # print(file_count,file_path)  # 这里可以根据需求对文件路径进行处理
                find_href_link(file_path)
def del_img(img_path):
    for root, dirs, files in os.walk(img_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file in href_list:
                print("我的图片是有用的，img文件目录",file_path)
            else:
                print("图片无用删除吧，img文件目录",file_path)
                global del_img_count
                del_img_count +=1
                del_img_list.append(file)
                # delete_file(file_path)
    else:
        print("需要删除的图片信息：总共%s张，详情如下：%s" % (del_img_count, del_img_list))
if __name__ == '__main__':
    md_filepath = r"E:\Ryan\我的云笔记"# "Markdown 文件所在目录的路径: "
    traverse_directory(md_filepath)
    print("文件总数:%s,文件总链接数:%s,需要上传到服务器的图片：%s"%(file_count,href_count,total_chuli_count))
    # href_list = list(set(href_list))
    print("图片链接被引用:合计%s张，详情:%s"%(len(href_list),href_list))
    print("图片链接被引用:合计%s张，详情:%s"%(len(href_list),sorted(href_list)))
    img_path =r"E:\Ryan\我的云笔记\img" # img下的目录
    for root, dirs, files in os.walk(img_path):
        print(f"img目录下的图片数：{len(files)},图片名称列表：{files}")
    # del_img(img_path)
    # 需要删除的图片信息：总共62张


