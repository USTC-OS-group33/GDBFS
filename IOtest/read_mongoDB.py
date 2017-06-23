#!/usr/bin/env python
#-*- coding:utf-8 -*-

import thread
from threading import Thread
import time
from pymongo import MongoClient  
from bson.objectid import ObjectId  
from gridfs import *
N=1000	#the num of LWP
cost=0
file='test'

def mongodb_read():
    #start=time.time()
    client = MongoClient()  
    db = client.gdbfs 
    fs = GridFS(db, 'col') 
    file_name="test"
    for i in range(100):
    	file = fs.get_version(file_name, 0)  
	r=file.read()

    
#end=time.time()
#print end-start
#cost=cost+end-start

sta=time.time()
ls=[]
for i in range(N):
    th=Thread(target=mongodb_read,args=(file))
    ls.append(th)
e=len(ls)
while True:
    for x in ls:
        if not x.is_alive():
            e-=1
    if e<=0:
        break
end=time.time()
print "mongodb:"
mt=end-sta
print mt	#the num of time
	


