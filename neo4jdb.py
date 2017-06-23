
from __future__ import print_function
from py2neo import *
import sys
import shlex
import uuid




# Base Operations
class neo4jdb():

    MAX_LENGTH = 1e9
    D_REL_TYPE = 1
    S_REL_TYPE = 0
    NOT_FOUND = -1
    FOUND = 0


    def __init__(self, **kwargs):
        # login
        authenticate('localhost:7474', 'neo4j', '123456')
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

            elif command[0] == 'chrl':
                self.change_relationship(*command[1:])

            elif command[0] == 'exit':
                break


    def create_file(self, *file_name):
        file_nodes = frozenset([Node('file', name=x, id=0) for x in file_name])
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
        relationships = self._db.run('MATCH (a)-[r:D_REL]->(b) RETURN r').data()
        for relation in relationships:
            print('\t', relation['r'])
        relationships = self._db.run('MATCH (a)-[r:S_REL]->(b) RETURN r').data()
        for relation in relationships:
            print('\t', relation['r'])

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

    def change_relationship(self, *cmd):

        flags = ['+', '-']
        op = None
        pos = None
        rname = None
        for i in range(len(cmd)):
            if cmd[i][0] in flags:
                pos = i
                rname = cmd[i][1:]
                op = cmd[i][0]
        if op == '+':
            if pos == 1:
                # src_node = self._db.run('MATCH (f:file) WHERE f.name=\"%s\" RETURN f' % cmd[0]).data()
                for fname in cmd[2:]:
                    # dst_node = self._db.run('MATCH (f:file) WHERE f.name=\"%s\" RETURN f' % fname).data()
                    self._db.run('MATCH (s:file),(t:file) WHERE s.name=\"%s\" AND t.name=\"%s\" CREATE (s)-[r:D_REL {name:\"%s\"}]->(t) RETURN r' % (cmd[0],fname,rname))
            elif pos == len(cmd) - 2:
                for fname in cmd[0:pos]:
                    self._db.run('MATCH (s:file),(t:file) WHERE s.name=\"%s\" AND t.name=\"%s\" CREATE (s)-[r:D_REL {name:\"%s\"}]->(t) RETURN r' % (fname, cmd[-1], rname))
            else:
                pass
        else:
            if pos == 1:
                # src_node = self._db.run('MATCH (f:file) WHERE f.name=\"%s\" RETURN f' % cmd[0]).data()
                for fname in cmd[2:]:
                    # dst_node = self._db.run('MATCH (f:file) WHERE f.name=\"%s\" RETURN f' % fname).data()
                    self._db.run('MATCH (s:file)-[r:D_REL]->(t:file) WHERE s.name=\"%s\" AND t.name=\"%s\" AND r.name=\"%s\" DELETE  r' % (cmd[0],fname,rname))
            elif pos == len(cmd) - 2:
                for fname in cmd[0:pos]:
                    self._db.run('MATCH (s:file)-[r:D_REL]->(t:file) WHERE s.name=\"%s\" AND t.name=\"%s\" AND r.name=\"%s\" DELETE  r' % (fname, cmd[-1], rname))
            else:
                pass


    def get_node_label(self, node_name):
        node_label = self._db.run('MATCH (n) WHERE n.name=\"%s\" RETURN labels(n)' % (node_name)).data()
        if len(node_label) == 0:
            return []
        else:
            return node_label[0][u'labels(n)'][0]

    def get_file_id(self, fname):
        fid = self._db.run('MATCH (f:file) WHERE f.name=\"%s\" RETURN f.id' % (fname)).data()[0][u'f.id']
        return fid

    def create_relation(self, s_name, t_name, r_type, init_value):
        if r_type == self.D_REL_TYPE:
            self._db.run('MATCH (s),(t) WHERE s.name=\"%s\" AND t.name=\"%s\" CREATE (s)-[r:D_REL {length:%f}]->(t) RETURN r' % (s_name, t_name, init_value))
        elif r_type == self.S_REL_TYPE:
            self._db.run('MATCH (s),(t) WHERE s.name=\"%s\" AND t.name=\"%s\" CREATE (s)-[r:S_REL {length:%f}]->(t) RETURN r' % (s_name, t_name, init_value))
        else:
            pass

    def delete_relation(self, s_name, t_name, r_type):
        if r_type == self.D_REL_TYPE:
            self._db.run('MATCH (s)-[r:D_REL]->(t) WHERE s.name=\"%s\" AND t.name=\"%s\"  DELETE  r' % (s_name, t_name))
        elif r_type == self.S_REL_TYPE:
            self._db.run('MATCH (s)-[r:S_REL]->(t) WHERE s.name=\"%s\" AND t.name=\"%s\"  DELETE  r' % (s_name, t_name))

    def change_relation(self, s_name, t_name, new_length):
        exist = self._db.run('OPTIONAL MATCH (s)-[r]->(t) WHERE s.name=\"%s\" AND t.name=\"%s\" RETURN r' % (s_name, t_name)).data()[0][u'r']
        if exist == None:
            return self.NOT_FOUND
        else:
            self._db.run('MATCH (s)-[r]->(t) WHERE s.name=\"%s\" AND t.name=\"%s\" SET r.length=%f RETURN r' % (s_name, t_name, new_length) )
            return self.FOUND

    def find_adj_nodes(self, src_name, r_type):
        adj_node_list = []
        if r_type == self.D_REL_TYPE:
            adj_node_list = self._db.run('MATCH (s)-[r:D_REL]->(t) WHERE s.name=\"%s\" RETURN t.name' % (src_name)).data()
        elif r_type == self.S_REL_TYPE:
            adj_node_list = self._db.run('MATCH (s)-[r:S_REL]->(t) WHERE s.name=\"%s\" RETURN t.name' % (src_name)).data()
        else:
            pass
        for k in range(len(adj_node_list)):
            adj_node_list[k] = adj_node_list[k][u't.name']
        return adj_node_list


if __name__ == '__main__':

    G = neo4jdb()
    #G.cli()

    # print(G.get_node_label("Stu"))
    # print(G.get_file_id("Zhang"))
    # G.change_relation("Zhang", "Bi", 0)
    # G.create_relation("Zhang", "Stu", G.D_REL_TYPE, 500)
    # G.cli()
    # print(G.find_adj_nodes("Zhang", G.D_REL_TYPE))
    print (G.get_node_label("Stu"))