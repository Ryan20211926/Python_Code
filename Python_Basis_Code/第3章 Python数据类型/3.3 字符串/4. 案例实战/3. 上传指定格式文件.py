# coding:utf-8
# @Time    : 2025/4/29 12:38
# @Author  : Ryan
# @FileName: 3. 上传指定格式文件.py
"""
"""
# 文件上传 只能上传图片(jpg,png,bmp,gif)
path = input('请选择文件:')  # 用户输入文件路径，例如 C:\foo\bar\desk_background.jpg
# 分析：要上传的文件的路径path----》文件名----》通过文件名再判断是否是图片类型
p = path.rfind('\\')  # 找到路径中最后一个反斜杠的位置
filename = path[p+1:]  # 通过切片截取出文件名
# 判断是否是图片类型？
if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('bmp') or filename.endswith('gif'):
    print('是图片允许上传！')
else:
    print('不是图片格式，只能上传图片！')

#

# 可上传的文件类型列表
allowed_extensions = ['jpg', 'jpeg', 'png', 'bmp', 'gif']

# 文件上传 只能上传图片(jpg,png,bmp,gif)
path = input('请选择文件:')  # 用户输入文件路径，例如 C:\foo\bar\desk_background.jpg

# 分析：要上传的文件的路径path----》文件名----》通过文件名再判断是否是图片类型
p = path.rfind('\\')  # 找到路径中最后一个反斜杠的位置

filename = path[p+1:]  # 通过切片截取出文件名

# 获取文件扩展名
file_extension = filename.split('.')[-1].lower()

# 判断是否是图片类型？
if file_extension in allowed_extensions:
    print('是图片允许上传！')
else:
    print('不是图片格式，只能上传图片！')