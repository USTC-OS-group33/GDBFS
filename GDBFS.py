#from pymongo import Connection
#from gridfs import GridFS
#from bson.code import Code
#from pymongo.errors import ConfigurationError
#import some packges 
import neo4j_support
import mongoDB_support 

# under mode 'strict', fuse can only operate on hard relations
# under mode 'graph', fuse can operate on all relations, but may lead to problems
fuse_mode = 'old_style'   

# search distance
max_distance = 100

def get_node_name(path):
    if(path[0] == '/'):
        path_list = path.split('/')
        name = path_list[len(path_list)-1]
    else:
        name = path
    return name

def stimulate_by_fuse(path):
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
    node_id = neo4j_support.id_map(path, fuse_mode)
    ppt = neo4j_support.get_node_properties(node_id)
    if ppt == 'file':
        return False
    else:
        return True

def get_file(path):
    node_id = neo4j_support.id_map(path, fuse_mode)
    return mongoDB_support.get_file(node_id)



