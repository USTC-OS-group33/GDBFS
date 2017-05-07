#-*- coding:utf-8 -*-

# import some packges
import re
db = 'fake_neo4j'

# 这是避开数据库的干扰二测试GDBFS与GDBFS_fuse的功能，做一个展示所做的demo。
# 这里的假数据库用简单的文本实现

# find nodes which are directly pointed by the input node,
#  and return the id of those nodes as a list
# relation type: 'hard_relation' or 'soft_relation'
# target_node_type may can be 'old_fs_node' or 'nolimit' or ...
def find_adj_nodes(node_id, relation_type, target_node_type):
    fh = open("fake_database/fake_neo4j")
    content=fh.read()
    pat = str(node_id) + "-.+-(\d+)"
    id_ls = re.findall(pat, content)
    fh.close()
    return id_ls

def stimulate(node_id, node_idmax_distance, relation_type, target_type):
    return []

def get_node_properties(node_id):
    fh = open("fake_database/fake_neo4j")
    content=fh.read()
    pat = str(node_id)+"={'[\w.]+'-'(\w+)'"
    prop_ls = re.findall(pat, content)
    fh.close()
    print "\n\nin get_node_properties\nnode_id =",node_id,"\nprop_ls =",prop_ls
    if len(prop_ls) == 0:
        return -1
    else:
        return prop_ls[0]

def get_nodes_name(id_ls):
    fh = open("fake_database/fake_neo4j")
    content=fh.read()
    name_ls=[]
    for node_id in id_ls:
        pat = str(node_id)+"={'([\w.]+)'-'\w+'"
        name = re.findall(pat, content)
        name_ls += name
    return name_ls

def id_map(path, fuse_mode):
    if fuse_mode == 'old_style':
        # 这种模式下只要在传统的文件逻辑中找就好，一个path对应一个id，或者没找到。
        fh = open("fake_database/fake_neo4j")
        content=fh.read()
        pat="/([\w.]+)"
        name_ls = re.findall(pat,path)
        if name_ls[0] == "root":
            node_id = 1
        else:
            return 0
        for name in name_ls[1:]:
            id_ls = find_adj_nodes(node_id,0,0)
            search_name_ls = get_nodes_name(id_ls)
            if name in search_name_ls:
                node_id = id_ls[search_name_ls.index(name)]
            else:
                return 0
        return int(node_id)

    elif fuse_mode == 'graph':    
        # 在 graph 模式下，不能保证一个 path 对应一个id，因为节点可以重名。
        # 虽然这个关系有可能会找到多个id。但是不管怎样还是返回一个id吧。
        # 目前的想法是忽略这里的重名可能，毕竟只是展示用。
        # 这纯粹是为了在传统文件浏览器中看我们的整个逻辑结构，达到一个图形化演示的效果
        # 由客户端传回来的直接是id，就没有这个麻烦
        return 0
    else:
        return -1


def generate_new_id(path, node_property):
    return 0

