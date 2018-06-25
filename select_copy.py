import os, shutil, zipfile

shutil.copy('101_ObjectCategories.zip', 'copied_file.zip')

data = zipfile.ZipFile('copied_file.zip')
data.extractall('extract')
data.close()

for foldername, subfolders, filenames in os.walk('extract/101_ObjectCategories'):
    for filename in filenames:
        shutil.move(foldername + '/' + filename, 'res/' + foldername.split('/')[-1] + filename[5:])

shutil.rmtree('extract')
