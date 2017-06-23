from pymongo import MongoClient  
from gridfs import *  
def write_vfs():  
    client = MongoClient()  
    db = client.gdbfs
    fs = GridFS(db, 'col') 
    file_name='test'
    with open (file_name.decode('utf-8'),'rb') as myimage:  
       	da=myimage.read()	#read data
    for i in range(1,100) :
    	output=open('data','w')
    	output.write(da)  #write in data
write_vfs()
 
