#encoding=UTF-8

import sys,os
import hashlib
import base64
import json


def invert_list(list):
	newlist = {}
	for key,value in list.iteritems():
		oldvalue = newlist.get(value,[])
		oldvalue.append(key)
		newlist[value] = oldvalue
	return newlist

photo_hashes = {}
with open('hashes.dump','r') as hashes_file:
	photo_hashes = json.load(hashes_file)
	hashes_file.close()

inverted_list = invert_list(photo_hashes)

filelist1 = {}
filelist2 = []
for key,value in inverted_list.iteritems():
	if len(value) > 1: 
		newlist = []
		newkey = ''
		for item in value: 
			newkey += item
			newlist.append(unicode(base64.b64decode(item),errors='replace'))
		newkey = hashlib.md5(newkey).hexdigest()
		filelist1[newkey] = newlist
		filelist2.append(newlist)
		

print len(filelist2)
for item in filelist2: print item

fp = open('result.txt','w')
json.dump(filelist1,fp)