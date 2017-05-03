# Design Note
### for GDBFS
##### (我们边商量边改，还有很多细节没考虑到)

* 每个节点都要有不同的ID，而节点名可以重复
* 由于节点名可以重复，在传统文件系统显示时，要一起显示出来。比如说以`name_id`的形式，因为传统文件系统不能区分文件名相同时谁是谁。而我们的客户端可以做到这点。
* 目前设计的是由五个py文件组成。`neo4j_support`提供对neo4j的基本操作的包装，包括对高级搜索的支持。`mongoDB_support`提供对 mongoDB 最基本的操作，包括对文件的基本操作，如 read write seek 等操作。`GDBFS`对两个数据库做一个封装，提供我们文件系统最基本的操作。`GDBFS_fuse`调用`GDBFS`模块来接驳fuse，`GDBFS_client`调用`GDBFS`模块来实现客户端界面操作。
