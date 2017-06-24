from __future__ import print_function
from py2neo import *
import sys
import GDBFS
import neo4jdb

class client():

    def __init__(self):

        self.ndb = neo4jdb.neo4jdb()



    def change_demo_path(self):

        # self.ndb._db.run('CREATE (p:path {name=\"\"}) RETURN p' )

        while True:
            print ('>>>', end='')
            path = sys.stdin.readline()
            self.ndb._db.run('MATCH (p:path) SET p.name=\"%s\"' % (path))
