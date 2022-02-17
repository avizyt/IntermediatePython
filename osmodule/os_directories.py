import os

dir_name = 'os_dir_eg'

print("Creating", dir_name)
os.mkdir(dir_name)

file_name = os.path.join(dir_name, 'example.txt')
print("Creating", file_name)
with open(file_name, 'wt') as f:
    f.write('it is an example file created by python os module.')

print("Cleaning up")
os.unlink(file_name)
os.rmdir(dir_name)