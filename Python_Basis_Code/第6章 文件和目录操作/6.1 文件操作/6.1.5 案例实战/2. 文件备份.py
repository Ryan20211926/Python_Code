# coding:utf-8
# @Time    : 2025/4/28 13:01
# @Author  : Ryan
# @FileName: 2. 文件备份.py
# 1. 用户输入目标文件  如：sound.txt.mp3
old_name = input('请输入您要备份的文件名：')
# 2. 规划备份文件的名字
# 2.1 提取后缀 --
# 找到名字中的最右侧的点才是后缀的点
# 在右侧查找rfind()方法
# 获取文件全名中后缀.的位置
index = old_name.rfind('.')
# 4. 思考：有效文件才备份 .txt
if index > 0:
    # 提取后缀，这里提取不到，后面拼接新文件名字的时候就会报错
    postfix = old_name[index:]

# 2.2 组织新名字 = 原名字 + [备份] + 后缀
# 原名字就是字符串中的一部分子串 -- 切片[开始:结束:步长]
# new_name = old_name[:index] + '[备份]' + old_name[index:]
new_name = old_name[:index] + '[备份]' + postfix


# 3. 备份文件写入数据(数据和原文件一样)
# 3.1 打开 原文件 和 备份文件
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

# 3.2 原文件读取，备份文件写入
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了终止循环
while True:
    # 每次在原文件中读取的内容
    con = old_f.read(1024)
    # 表示读取完成了
    if len(con) == 0:
        # 终止读取
        break

    # 新文件写入读取的数据
    new_f.write(con)

# 3.3 关闭文件
old_f.close()
new_f.close()