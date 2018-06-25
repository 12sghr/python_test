import os, shutil, zipfile

shutil.copy('101_ObjectCategories.zip', 'copied_file.zip')

data = zipfile.ZipFile('copied_file.zip')
data.extractall('test')
data.close()
