# -*- coding: utf-8 -*-
import os
import shutil

def copy_folder(source_folder, target_folder):
    shutil.copytree(source_folder, target_folder)

source_folder = 'metapmf'  
start_value = 1.95
end_value = 2.10

num_copies = int((end_value - start_value) / 0.05) + 1

for i in range(num_copies):
    value = start_value + i * 0.05
    target_folder = "{:.2f}".format(value)

    copy_folder(source_folder, target_folder)

    print(f"Copied folder: {target_folder}")

def replace_string_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        content = file.read()

    if old_string not in content:
        print(f"skip: {file_path}")
        return

    content = content.replace(old_string, new_string)

    with open(file_path, 'w') as file:
        file.write(content)

    print(f"Replaced file: {file_path}")

def traverse_directory(folder_path):
    for root, dirs, files in os.walk(folder_path):
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

folder_path = '.'  

traverse_directory(folder_path)






