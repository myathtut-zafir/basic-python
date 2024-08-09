import os
import shutil

# f=open('test.txt','w+')
# f.write('this is test file')
# f.close()

# print(os.listdir())

# shutil.move('/Users/myathtut/Desktop/Code/basic-python/test.txt','/Users/myathtut/Desktop/Code/basic-python/file')
# send2trash.send2trash('/Users/myathtut/Desktop/Code/basic-python/file/test.txt')

print(os.getcwd())
file_path='/Users/myathtut/Desktop/Code/basic-python'
for folder,sub_folders,files in os.walk(file_path):
    print(f"currently at {folder}")
    print('\n')
    print(f"sub at {sub_folders}")
    print(f"files at {files}")
