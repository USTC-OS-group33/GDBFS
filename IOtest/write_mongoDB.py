from pymongo import MongoClient  
from gridfs import *  
def write_mongoDB():  
    client = MongoClient()  
    db = client.gdbfs
    fs = GridFS(db, 'col') 
    file_name='test'
    with open (file_name.decode('utf-8'),'rb') as myimage:  
       	data=myimage.read()	#read data
    for i in range(1,100) :
       	fs.put(data,filename='md')  #write in data
write_mongoDB()
 
