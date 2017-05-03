# import some packges


# find nodes which are directly pointed by the input node,
#  and return the id of those nodes as a list
# relation type: 'hard_relation' or 'soft_relation'
# target_node_type may can be 'old_fs_node' or 'nolimit' or ...
def find_adj_nodes(node_id, relation_type, target_node_type):
    return []

def stimulate(node_id, node_idmax_distance, relation_type, target_type):
    return []

def get_node_properties(node_id):
    return ''

def get_nodes_name(id_ls):
    return []

def id_map(path, fuse_mode):
    if fuse_mode == 'old_style':
        # 这种模式下只要在传统的文件逻辑中找就好，一个path对应一个id，或者没找到。
        return 0
    elif fuse_mode == 'graph':    
        # 在 graph 模式下，不能保证一个 path 对应一个id，因为节点可以重名。
        # 虽然这个关系有可能会找到多个id。但是不管怎样还是返回一个id吧。
        # 目前的想法是忽略这里的重名可能，毕竟只是展示用。
        # 这纯粹是为了在传统文件浏览器中看我们的整个逻辑结构，达到一个图形化演示的效果
        # 由客户端传回来的直接是id，就没有这个麻烦
        return 0
    else:
        return -1

