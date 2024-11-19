import os
import shutil

if os.path.exists('./masa-mods-chinese.zip'):
    file_path = './masa-mods-chinese.zip'
    shutil.move(file_path, './[1.19-1.20]MASA全家桶汉化包' + '.zip')

if os.path.exists('./masa-mods-chinese-neo.zip'):
    file_path = './masa-mods-chinese-neo.zip'
    shutil.move(file_path, './[1.19-1.20]MASA全家桶汉化包-neo' + '.zip')