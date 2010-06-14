#!/usr/bin/python
# -*- coding: utf-8 -*-
import simplejson

#json
def read(filename):
	try:
		file = open(filename,'r')
		mt = simplejson.loads(file.read())
		file.close()
	except:
		mt = {}
	return mt


def write(filename,data):
	file = open(filename,'w')
	file.write(simplejson.dumps(data))
	file.close()
	
