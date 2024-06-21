import os
import json
import shutil
import mutagen
working_dir = 'C:\\Users\\Owner\\Desktop\\Audiobooks\\'
with open(working_dir + 'metadata.json','r',encoding='utf8') as f:
    metadata = json.load(f)
    print(len(metadata))
    print(type(metadata))
    count = 0
    for file in os.listdir(working_dir):
        if '.mp3' not in file:
            continue
        else:
            print(metadata[file[0:-4]])            