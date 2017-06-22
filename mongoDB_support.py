#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
	from pymongo import MongoClient
except ImportError:
	print("failed to import pymongo,please install it!")
	exit(1)	
	 # 检查是否安装并运行成功pymongo，未成功则退出

from bson.objectid import ObjectId  
from gridfs import *

class mongo_file:

	def read(file_name,offset,size): 
		#读文档
        	client = MongoClient()  
    		db = client.gdbfs 
    		fs = GridFS(db, 'col') 
		#connect
   		temp = fs.get_version(file_name, 0) 

 
    		if temp:
			temp.seek(offset)
			return temp.read(size)
			#返回文件内容
    		
		else:
			#数据库中不存在该文件
			print("connot find this file!")
			exit(-1)



	def write(data,file_name):   
		#写文档
    		client = MongoClient()  
    		db = client.gdbfs
    		fs = GridFS(db, 'col') 
		#connect
       		id = fs.put(data,filename=file_name)  

       		return id



	def insert(file_name):   
		#本地上传文件
    		client = MongoClient()  
    		db = client.gdbfs
    		fs = GridFS(db, 'col') 
		#connect

    		with open (file_name.decode('utf-8'),'rb') as myimage:  
       			data=myimage.read()
       			id = fs.put(data,filename=file_name) 
 
       		return id
	
	
	def existfile(file_id):		
		#检查是否存在文档
		client = MongoClient()  
		db = client.gdbfs
		fs = GridFS(db, 'col') 
		#connect
		t=fs.exists(ObjectId(file_id))
	
		return t


	def length(file_name):  
		#获得文件大小
    		client= MongoClient()
    		db = client.gdbfs
    		fs = GridFS(db, 'col')
		#connect
    		file = fs.get_version(file_name, 0)  

    		if file:
			return file.length

    		else :
    		#找不到文件	
			print("this file doesn't exist! please check it again!")

			exit(-1)


	def delFile(file_id):  
		#删除文件
    		client = MongoClient() 
    		db = client.gdbfs  
    		fs = GridFS(db, 'col') 
		#connect 
    		fs.delete(ObjectId(file_id))  


	def getlist():
		#获取文件列表
		client = MongoClient()  
		db = client.gdbfs
		fs = GridFS(db, 'col')
		#connect
		t=fs.list()
		return t


	def Rename(file_id,new_filename):  
		#重命名
    		client = MongoClient()  
    		db = client.gdbfs 
    		col = GridFSBucket(db)
		#connect
    		col.rename(ObjectId(file_id),new_filename)


	def read_id(file_id,offset,size):
		#read file by id
		my_db = MongoClient().gdbfs
		col = GridFSBucket(my_db)
		# Get _id of file to read

		file = open('myfile','wb+')
		fs.download_to_stream(file_id, file)
		file.seek(offset)
		contents = file.read(size)

		return contents
	

