#-*- coding:utf-8 -*-


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
    if(path[0] == '/' and len(path)>1):
        path_list = path.split('/')
        name = path_list[len(path_list)-1]
    elif(path[0]=='/' and len(path)==1):
        name=path
    else:
        name = path
    return name

def get_parent(path):
    i=len(path)-1
    if(path[i]=='/'):
        i=i-1
    while True:
        if(path[i]!='/'):
            i=i-1
        else:
            break
    return path[0:i]

def stimulate_by_fuse(path):
    if path == "/":
        return ["root","demo"]
    if path=="/demo":
        return Ndb.find_adj_nodes(client_pos,Ndb.S_REL_TYPE)
    if fuse_mode == 'old_style':
        # node_id = neo4j_support.id_map(path, 'old_style')
        name_ls = Ndb.find_adj_nodes(get_node_name(path),Ndb.S_REL_TYPE)
    
    else:
        print "fuse_mode error"
        exit(1)
    # name_ls = neo4j_support.get_nodes_name(id_ls)
    return name_ls


def is_dir(path):
    #node_id = neo4j_support.id_map(path, fuse_mode)
    print "\n\n\nin is_dir\npath =",path
    ppt = Ndb.get_node_label(get_node_name(path))
    print "\nppt =",ppt,"\na\n"
    
    if ppt == 'category':
        return True
    else:
        return False

def create_node_fuse(node_property, path):
    #node_id = neo4j_support.id_map(path, fuse_mode)
    #if(node_id != 0):
        # object already exist
    #    return 0
    #node_id = neo4j_support.generate_new_id(path, node_property)
    name=get_node_name(path)
    if node_property == 'file':
        Ndb.create_file(*[name])
        # make relation
    else:
        # node_property == 'attribute'
        Ndb.create_category(name)
        # make relation    
    parent_path=get_parent(path)
    p_name=get_node_name(parent_path)
    print "\n\n\nparent_path=",p_name,"path=",path,"\nend\n\n"
    Ndb.create_relation(p_name,name,Ndb.S_REL_TYPE, 50)    ### to do
    return 1

def write(path, data, offset):
    # node_id = Ndb.get_file_id(path)
    #if(node_id == 0):
        # write a empty file
    node_id = Mdb.write(data, path)
        # update node_id
    

    return len(data)


def get_file_length(name):
    return Mdb.length(name)


#Ndb.create_relation('root','dir2',Ndb.S_REL_TYPE,5)
#Ndb.remove_file('axs')
#Ndb.remove_category(*['dir1'])
#print Ndb.find_adj_nodes('/root',Ndb.S_REL_TYPE)
#print Ndb.get_node_label('/root')
#Mdb.write('asdasddsads\nasdasdas\nasds   d','/root/file1')


