# -*- coding: utf-8 -*-
import os
import shutil

def copy_folder(source_folder, target_folder):
    # 使用shutil模块复制整个文件夹
    shutil.copytree(source_folder, target_folder)

# 设置源文件夹路径和目标文件夹的起始值和结束值
source_folder = 'metapmf'  # 替换为实际的源文件夹路径
start_value = 1.95
end_value = 2.10

# 计算需要复制的文件夹个数
num_copies = int((end_value - start_value) / 0.05) + 1

# 循环复制文件夹
for i in range(num_copies):
    # 计算当前的数值
    value = start_value + i * 0.05

    # 构造目标文件夹的名称
    target_folder = "{:.2f}".format(value)  # 格式化为两位小数的字符串

    # 复制文件夹及其子文件
    copy_folder(source_folder, target_folder)

    print(f"已复制文件夹: {target_folder}")

def replace_string_in_file(file_path, old_string, new_string):
    # 读取文件内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 检查是否存在旧字符串
    if old_string not in content:
        print(f"文件中不存在目标字符串，跳过文件: {file_path}")
        return

    # 替换字符串
    content = content.replace(old_string, new_string)

    # 将替换后的内容写回文件
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"已替换文件: {file_path}")

def traverse_directory(folder_path):
    for root, dirs, files in os.walk(folder_path):
        # 排除名为'metapmf'的文件夹
        if 'metapmf' in dirs:
            dirs.remove('metapmf')
        
        for file in files:
            if file == 'disang.in':
                file_path = os.path.join(root, file)
                subdir_name = os.path.basename(root)
                replace_string_in_file(file_path, 'distance', subdir_name)

            if file == 'disang.in':
                file_path = os.path.join(root, file)
                subdir_name = os.path.basename(root)
                replace_string_in_file(file_path, 'force', '200.0')   
         
            if file == 'amber.slurm':
                file_path = os.path.join(root, file)
                subdir_name = os.path.basename(root)
                replace_string_in_file(file_path, 'umbrella_sampling_distance', subdir_name)
            
            if file == 'prod_sample.in':
                file_path = os.path.join(root, file)
                subdir_name = os.path.basename(root)
                replace_string_in_file(file_path, 'distance', subdir_name)

# 设置当前目录为文件夹路径
folder_path = '.'  # 当前目录

# 调用函数遍历文件夹并替换字符串
traverse_directory(folder_path)






