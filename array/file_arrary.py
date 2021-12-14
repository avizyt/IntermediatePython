import os

file_path = "D:/python"
files_in_folder = []
# with open(file_path) as file_object:
#     for file in file_object:
#         files_in_folder.append(file)
#     print(files_in_folder)

dir_list = os.listdir(file_path)
for file in dir_list:
    files_in_folder.append(file)
print(files_in_folder)