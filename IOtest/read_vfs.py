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

def vfs_read(): 
    #it uses to test vfs 
    #start=time.time()
    for i in range(100):
         with open ('test','r') as myimage:  
       		r=myimage.read()

    #end=time.time()
    #print end-start
    #cost=cost+end-start

sta=time.time()
ls=[]
for i in range(N):
    th=Thread(target=vfs_read,args=(file))
    ls.append(th)
e=len(ls)
while True:
    for x in ls:
        if not x.is_alive():
            e-=1
    if e<=0:
        break
end=time.time()
print "vfs:"
vt=end-sta
print vt	#the num of time

