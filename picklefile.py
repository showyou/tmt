#!/usr/bin/python
# -*- coding: sjis -*-
import cPickle as pickle

#pickleで読み書き
def read(filename):
	file = open(filename,'r')
	data = pickle.load(file)
	file.close()
	return data

def write(filename,data):
	file = open(filename,'w')
	pickle.dump( data,file )
	file.close()

