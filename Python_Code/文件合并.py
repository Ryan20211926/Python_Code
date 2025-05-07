import os
import random
import shutil
def copy_random_images(source_folder, destination_folder, count=2):
    """从每个子文件夹中随机复制指定数量的图片到目标文件夹。"""
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for subfolder in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder)
        if os.path.isdir(subfolder_path):
            images = [img for img in os.listdir(subfolder_path) if img.endswith(('.jpg', '.jpeg', '.png'))]
            random_images = random.sample(images, min(len(images), count))
            for img in random_images:
                source_path = os.path.join(subfolder_path, img)
                destination_path = os.path.join(destination_folder, img)
                shutil.copy2(source_path, destination_path)
if __name__ == '__main__':
    # 使用示例
    source_folder = r'C:\Users\Administrator\Desktop\obsidian\Ryan学习笔记0510\Ryan学习笔记\img'  # 源文件夹路径
    destination_folder = 'path/to/your/destination/folder'  # 目标文件夹路径
    count = 2  # 需要复制的图片数量
    copy_random_images(source_folder, destination_folder, count)