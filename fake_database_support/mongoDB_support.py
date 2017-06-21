#-*- coding:utf-8 -*-

import os
from pymongo import 
from gridfs import 
from bson.code import 
from pymongo.errors import ConfigurationError
import some packges


fake_mongoDB='fake_database/fake_mongoDB'


class File:
    
    def read(self, size, offset):
            fh = open(self.path, "rb")
            fh.seek(offset)
            data = fh.read(size)
            fh.close()
            print "\n\nin mongoDB read, path =",self.path,"size =",size,"offset =",offset
            return data

    def is_exist(self):
        try:
            fh = open(self.path, "rb")
            fh.close()
        except IOError:
            return False
        else:
            return True

    def length(self):
        return os.path.getsize(self.path)

def get_file(node_id):
    file = File(node_id)
    return file
