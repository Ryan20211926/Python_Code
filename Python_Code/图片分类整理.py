import os
import random
import shutil
from datetime import datetime
file_formats = ('.jpg', '.jpeg', '.png')

def get_file_mod_date(file_path):
    """获取文件的最后修改时间"""
    mod_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mod_time).strftime('%Y%m%d')

def copy_images(source_folder, destination_folder):
    """从每个子文件夹中随机复制指定数量的图片到目标文件夹。"""
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for subfolder in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder)
        if os.path.isdir(subfolder_path):
            images = [img for img in os.listdir(subfolder_path) if img.endswith(file_formats)]
            random_images = random.sample(images, len(images))
            for img in random_images:
                source_path = os.path.join(subfolder_path, img)
                destination_path = os.path.join(destination_folder, img)
                shutil.copy2(source_path, destination_path)
def rename_images(destination_folder,pic_tag):
    date_counter = {}
    # 遍历文件夹中的所有文件
    for filename in os.listdir(destination_folder):
        # 跳过非图片文件（这里简单判断，你可以根据需要添加更多扩展名）
        if not filename.lower().endswith(file_formats):
            continue
            # 获取文件的完整路径
        file_path = os.path.join(destination_folder, filename)
        # 获取文件的最后修改时间并格式化为字符串
        mtime = os.path.getmtime(file_path)
        formatted_date = datetime.fromtimestamp(mtime).strftime('%Y%m%d')
        # 检查当前日期是否已在字典中
        if formatted_date not in date_counter:
            date_counter[formatted_date] = 1
        else:
            date_counter[formatted_date] += 1
            # 构建新的文件名
        new_filename = f"{pic_tag}_{formatted_date}_{date_counter[formatted_date]:03d}{os.path.splitext(filename)[1]}"
        new_file_path = os.path.join(destination_folder, new_filename)
        # 重命名文件
        os.rename(file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")
def classify_photos(source_dir,pic_tag):
    """
    对source_dir目录下的照片文件进行分类
    :param source_dir: 包含照片文件的源目录
    :param target_base_dir: 分类后文件存储的基础目录
    :param pic_tag: 分类后文件存储的基础目录
    """
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(source_dir, filename)
            mod_date = get_file_mod_date(file_path)
            target_dir = os.path.join(source_dir, pic_tag,mod_date)
            # 如果目标目录不存在，则创建它
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                # 将文件移动到目标目录
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved {filename} to {target_dir}")
if __name__ == '__main__':
    # 使用示例
    source_folder = r'C:\Users\Administrator\Desktop\demo\tes11t'  # 源文件夹路径
    destination_folder = r'C:\Users\Administrator\Desktop\demo\all'  # 目标文件夹路径
    pic_tag ="旅行" #
    copy_images(source_folder, destination_folder)
    rename_images(destination_folder,pic_tag)
    classify_photos(destination_folder,pic_tag)

