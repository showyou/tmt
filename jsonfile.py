#!/usr/bin/python
# -*- coding: sjis -*-
import json

#json�ǂݍ���
def read(filename):
	try:
		file = open(filename,'r')
		mt = json.read(file.read())
		file.close()
	except:
		mt = {}
	return mt

def write(filename,data):
	file = open(filename,'w')
	file.write(json.write(data))
	file.close()
	
