import zipfile
import shutil

# f=open('fileone.txt','w+')
# f.write('ONE FILE')
# f.close()


# f=open('filetwo.txt','w+')
# f.write('TWO FILE')
# f.close()

# comp_file=zipfile.ZipFile('comp_file.zip','w')
# comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

# zip_obj=zipfile.ZipFile('comp_file.zip','r')
# zip_obj.extractall('extract')

dir_to_zip='/Users/myathtut/Desktop/Code/basic-python/extract'
output='example'
shutil.make_archive(output,'zip',dir_to_zip)
shutil.unpack_archive('example.zip','final','zip')


