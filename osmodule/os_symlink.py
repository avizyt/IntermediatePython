import os

link_name = '/tmp/' + os.path.basename(__file__)

print(f"Creating link {link_name} => {__file__}")
os.symlink(__file__, link_name)

stat_info = os.lstat(link_name)
print('Permission: ', oct(stat_info.st_mode))

print('Point to: ', os.readlink(link_name))
# clean up
os.unlink(link_name)
