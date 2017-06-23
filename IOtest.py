import thread
from threading import Thread
import time
import mongoDB_support

N=10
cost=0
Mdb=mongoDB_support.mongo_file()


def vfs_read(file):
    #start=time.time()
    for i in range(1000):
        fh=open('test','r')
        r=fh.read()
        fh.close()
        fh=open('test1','r')
        r=fh.read()
        fh.close()
    #end=time.time()
    #print end-start
    #cost=cost+end-start
"""
file='test'
sta=time.time()
for i in range(N):
    thread.start_new_thread(vfsread,(file,))
end=time.time()
print end-sta
"""

def mongodb_read(file):
    #start=time.time()
    for i in range(1000):
        r=Mdb.read('ptest',0,43823832)
        r=Mdb.read('ptest1',0,43823832)
    #end=time.time()
    #print end-start
    #cost=cost+end-start

file='test'
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
print mt

#fh=open('test1','r')
#Mdb.write(fh.read(),'ptest1')
#fh.close()



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
print vt
print vt/mt