#from pymongo import Connection
#from gridfs import GridFS
#from bson.code import Code
#from pymongo.errors import ConfigurationError
#import some packges 
import neo4j_support
import mongoDB_support 

# under mode 'strict', fuse can only operate on hard relations
# under mode 'graph', fuse can operate on all relations, but may lead to problems
fuse_mode = 'strict'   


def get_node_name(path):
    if(path[0] == '/'):
        path_list = path.split('/')
        name = path_list[len(path_list)-1]
    else:
        name = path
    return name


def get_node_id(name):
    node_id = name.split('_')
    node_id = node_id[len(node_id)-1]
    return int(node_id)


def stimulate_by_fuse(path):
    name = get_node_name(path)
    if fuse_mode == 'strict':
        node_id = get_node_id(name)
        id_ls = neo4j_support.find_adj_nodes(node_id, 'hard_relation')
    elif fuse_mode == 'graph':
        id_ls = neo4j_support.stimulate(name)
    else:
        print "fuse_mode error"
        exit(1)


def is_dir(path):
    name = get_node_name(path)
    node_id = get_node_id(name)
    ppt = neo4j_support.get_node_properties(node_id)
    if ppt == 'file':
        return False
    else:
        return True

def get_file(path):
    name = get_node_name(path)
    node_id = get_node_id(name)
    return mongoDB_support.get_file(node_id)



