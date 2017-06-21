from pymongo import MongoClient  
from bson.objectid import ObjectId  
from gridfs import *
def read(file_id,offset,size):  
    client = MongoClient()  
    db = client.gdbfs 
    fs = GridFS(db, 'col') 
    file = fs.get_version(file_id, 0)  
    if file:
	file.seek(offset)
	return file.read(size)
    else:
	print("connot find this file!")
	exit(-1)
