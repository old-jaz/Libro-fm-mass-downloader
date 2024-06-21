import mutagen
import urllib
import urllib.request
import os
import json

base_dir = "C:\\Users\\Owner\\Desktop\\Audiobooks\\"

#read in metadata file
#for every filename, assign metadata to .mp3 file
#Download audiobook cover from libro.fm
class metadata_worker():
    def __init__(self, audiobook_filename, metadata):
        self.audiobook = mutagen.File(audiobook_filename)
        self.metadata = metadata
    def cover_downloader(self):
        cover_url = self.metadata['cover']
        urllib.request.urlretrieve(cover_url, base_dir + (self.metadata['isbn'] + '.png'))
    def assign_metadata(self):
        self.audiobook['Title'] = self.assign(self.metadata['title'])
        self.audiobook['Artist'] = self.assign(self.metadata['author'])
        self.audiobook['series'] = self.assign(self.metadata['series'])
        self.audiobook['number'] = self.assign(self.metadata['number'])
        self.audiobook['cover'] = self.assign(base_dir + (self.metadata['isbn'] + '.png'))
        self.audiobook['isbn'] = self.assign(self.metadata['isbn'])
    def run(self):
        self.cover_downloader()
        self.assign_metadata()
        self.audiobook.save()
    def assign(self, text):
        return mutagen.id3.TextFrame(encoding=3, text=[text])

f = open(base_dir + 'metadata.json')
metadata = json.load(f)
for filename in os.listdir(base_dir):
    if '.mp3' in filename:
        worker = metadata_worker(filename, metadata[filename[:-4]])
        worker.run()
        
