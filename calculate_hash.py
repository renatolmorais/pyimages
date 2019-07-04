#encoding=UTF-8

import sys,os
import hashlib
import base64
import json

#photo_files = ['photo1.jpg','photo5.jpg','photo2.jpg','photo3.jpg','photo4.jpg']
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

def calculate_hash(photo_files):
	photo_hashes = {}
	for filename in photo_files:
		b64name = base64.b64encode(filename)
		photo_hash = hashlib.sha224()
		with open(filename,'rb') as fp:
			while True:
				data = fp.read(BUF_SIZE)
				if not data: break
				b64content = base64.b64encode(data)
				photo_hash.update(b64content)
			fp.close()
		photo_hashes[b64name] = photo_hash.hexdigest()
	return photo_hashes

def crawl(init_path):
	filelist = []
	if os.path.isdir(init_path):
		dirlist = os.listdir(init_path) #
		for path in dirlist:
			filelist += crawl(init_path + "\\" + path)
	else:
		filelist.append(init_path)
	return filelist

if __name__ == '__main__':
	#init_path = 'D:\\Fotos e Videos\\Photos\\Aniversario Ana Luisa'
	init_path = 'D:\\Fotos e Videos\\Photos'
	#init_path = ''
	photo_files = crawl(init_path)
	#print photo_files

	photo_hashes = calculate_hash(photo_files)
	hashes_file = open(init_path + '\\' + 'hashes.dump','w')
	#print photo_hashes
	json.dump(photo_hashes,hashes_file)
	hashes_file.close()
	
