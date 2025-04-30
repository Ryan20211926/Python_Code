import os
filename_dict = {}
filename_counts = {}  # 统计文件数量
filename_paths ={} # 统计文件路径
def count_files(path):
    for root, dirs, files in os.walk(path):
        if ".obsidian" in root:
            pass
        else:
            for item in files:
                # print(item, os.path.join(root, item))
                file_path = os.path.join(root, item)
                filename_counts[item] = filename_counts.get(item, 0) + 1
                if item in filename_paths.keys():
                    filename_paths[item].append(file_path)
                else:
                    filename_paths[item] = filename_paths.get(item,[file_path])
                filename_dict[item] = {"count": filename_counts[item],"path":filename_paths[item]}
    # print(filename_dict)
    return filename_dict
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"文件 {file_path} 已成功删除。")
    else:
        print(f"文件 {file_path} 不存在。")
if __name__ == '__main__':
    path = r'E:\Ryan\我的云笔记'
    path_del = r'E:\Ryan\我的云笔记\img'
    # path = r'D:\Ryan\我的云笔记'
    file_resule = count_files(path)
    i =1
    for k,v in file_resule.items():
        # print(k,v)
        if v.get('count',0)>1:
            print("序号：",i,k,"  ------  ",v)
            i+=1
            # print(os.path.join(path_del,k))
            delete_file(os.path.join(path_del,k))
            # print(k,v['path'])