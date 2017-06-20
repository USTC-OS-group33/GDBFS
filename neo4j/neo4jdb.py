from __future__ import print_function
from py2neo import *
import sys
import shlex
import uuid




# Base Operations
class neo4jdb():


    def __init__(self, **kwargs):
        # login
        authenticate('localhost:7474', 'neo4j', '970316')
        self._db = Graph()


    def cli(self):

        print ('GDBFS Navigator')

        while True:
            print ('>>>', end='')
            command = shlex.split(sys.stdin.readline())

            if command[0] == 'mk':
                self.create_file(*command[1:])

            elif command[0] == 'mkpt':
                if len(command[0]) > 1:
                    if command[1] == '-c' or command[1] == '--category':
                        self.create_category(*command[2:])
                    elif command[1] == '-a' or command[1] == '--attribute':
                        self.create_attribute(*command[2:])

            elif command[0] == 'rm':
                if len(command) > 1 and command[1] == '-a':
                    self.remove_all_node()
                else:
                    self.remove_file(*command[1:])

            elif command[0] == 'rmpt':
                self.remove_category(*command[1:])

            elif command[0] == 'ls':
                self.list()

            elif command[0] == 'chpt':
                if len(command) > 1:
                    if command[1] == '-c' or command[1] == '--category':
                        self.change_category(*command[2:])
                    elif command[1] == '-a' or command[1] == '--attribute':
                        self.change_attribute(*command[2:])

            elif command[0] == 'find':
                self.find_file(*command[1:])

            elif command[0] == 'exit':
                break


    def create_file(self, *file_name):
        file_nodes = frozenset([Node('file', name=x, id=uuid.uuid3(uuid.NAMESPACE_URL, x)) for x in file_name])
        self._db.create(Subgraph(file_nodes))

    def create_category(self, *category_name):
        category_nodes = frozenset([Node('category', name=x) for x in category_name])
        self._db.create(Subgraph(category_nodes))

    def remove_all_node(self):
        self._db.delete_all()

    def remove_file(self, *file_name):
        file_nodes = frozenset([self._db.run('MATCH (p:file) WHERE p.name=\"%s\" RETURN p' % (name)).data()[0]['p'] for name in file_name])
        self._db.delete(Subgraph(file_nodes))

    def remove_category(self, *category_name):
        category_nodes = frozenset([self._db.run('MATCH (p:category) WHERE p.name=\"%s\" RETURN p' % (name)).data()[0]['p'] for name in category_name])
        self._db.delete(Subgraph(category_nodes))

    def list(self):
        print ('files:')
        file_nodes = self._db.run('MATCH (p:file) RETURN p').data()
        for node in file_nodes:
            print ('\t', node['p']['name'])

        print ('\n')

        print ('categories:')
        category_nodes = self._db.run('MATCH (p:category) RETURN p').data()
        for node in category_nodes:
            print ('\t', node['p']['name'])

        print ('\n')

        print ('relationships:')
        relationships = self._db.run('MATCH (a:file)-[r:IS_A]->(b:category) RETURN r').data()
        for relation in relationships:
            print ('\t', relation['r'])

    def change_category(self, *cmd):
        add_categories = []
        minus_categories = []
        files = []
        for str in cmd:
            if str[0] == '+':
                add_categories.append(str[1:])
            elif str[0] == '-':
                minus_categories.append(str[1:])
            else:
                files.append(str)
        for p in add_categories:
            cnode = self._db.run('MATCH (a:category) WHERE a.name=\"%s\" RETURN a' % (p)).data()[0]['a']['name']
            if cnode:
                for fnode in files:
                    self._db.run('MATCH (a:file),(b:category) WHERE a.name=\"%s\" AND b.name=\"%s\" CREATE (a)-[:IS_A]->(b)' % (fnode, cnode))
        for p in minus_categories:
            cnode = self._db.run('MATCH (a:category) WHERE a.name=\"%s\" RETURN a' % (p)).data()[0]['a']['name']
            if cnode:
                for fnode in files:
                    self._db.run('MATCH (a:file)-[r:IS_A]->(b:category) WHERE a.name=\"%s\" AND b.name=\"%s\" DELETE r' % (fnode, cnode))

    def find_file(self, *cmd):
        op = ('(',')', '&', '|', '^', '-')
        eval_lst = list(cmd)
        i = 0
        set_lst = []
        for j, token in enumerate(eval_lst):
            if token not in op:
                node_list = self._db.run('MATCH (f:file)-[:IS_A]->(p:category) WHERE p.name=\"%s\" RETURN f' % (token)).data()
                for k in range(len(node_list)):
                    node_list[k] = node_list[k]['f']
                set_lst.append(set(node_list))
                eval_lst[j] = 'set_lst[%d]' % (i)
                i = i + 1
            else:
                pass
        eval_str = ' '.join(eval_lst)
        print (eval(eval_str))




if __name__ == '__main__':

    G = neo4jdb()
    G.cli()