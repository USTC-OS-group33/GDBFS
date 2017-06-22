#-*- coding:utf-8 -*-

import neo4j_support
import mongoDB_support 
import neo4jdb

# under mode 'old_style', fuse can only operate on hard relations
# under mode 'graph', fuse can operate on all relations, but may lead to problems
fuse_mode = 'old_style'   

# search distance
max_distance = 100


# database instance
Ndb=neo4jdb.neo4jdb()
Mdb=mongoDB_support.mongo_file()

def get_node_name(path):
    if(path[0] == '/'):
        path_list = path.split('/')
        name = path_list[len(path_list)-1]
    else:
        name = path
    return name

def stimulate_by_fuse(path):
    if path == "/":
        return ["root","demo"]
    if fuse_mode == 'old_style':
        node_id = neo4j_support.id_map(path, 'old_style')
        id_ls = neo4j_support.find_adj_nodes(node_id, 'hard_relation', 'old_fs_node')
    elif fuse_mode == 'graph':
        node_id = neo4j_support.id_map(path, 'graph')
        id_ls = neo4j_support.stimulate(node_id, max_distance, 'nolimit', 'nolimit')
    else:
        print "fuse_mode error"
        exit(1)
    name_ls = neo4j_support.get_nodes_name(id_ls)
    return name_ls


def is_dir(path):
    #node_id = neo4j_support.id_map(path, fuse_mode)
    ppt = neo4jdb.get_node_properties(path)
    print "\n\nin is_dir\npath =",path,"\nppt =",ppt,"\na\n"
    if ppt == 'attribute':
        return True
    else:
        return False

def create_node_fuse(node_property, path):
    #node_id = neo4j_support.id_map(path, fuse_mode)
    #if(node_id != 0):
        # object already exist
    #    return 0
    #node_id = neo4j_support.generate_new_id(path, node_property)
    if node_property == 'file':
        Ndb.create_file(path)
        # make relation
    else:
        # node_property == 'attribute'
        Ndb.create_category(path)
        # make relation    
    return 1

def write(path, data, offset):
    node_id = Ndb.get_file_id(path)
    if(node_id == 0):
        # write a empty file
        node_id = Mdb.write(data, path)
        # update node_id
    else:
        # write with id

    return 1

    
