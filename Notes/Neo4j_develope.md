#GDBFS实现 neo4j部分文档



## Neo4j简记

Node: 拥有零或多个label,以及零或多个property.
Relationship: 有且仅有一个type, 以及零或多个property.

label和type均为无值的字符串  
property是一个[字符串:值]对,其中值可以是其他基本数据类型.



## 节点和关系的分类

    Node:
        1. File Node:
            label: "file"
            property: name,length,id,etc
        2. Attribute Node:
            label: "attribute"
            property: attribute name, attribute
        3. Category Node:
            label: "category"
            property: category name
    
    Relationship:
        1. Static Relationship:
            type: "Static"
            property: simularity, distance, etc
        2. Dynamic Relationship:
            type: "Dynamic"
            property: simularity, distance, etc
            
### 为什么需要属性节点
文件节点本身的property用于存储文件的固有属性, 它们是静态的.  
属性节点存储的是动态属性.

### 属性节点之间是什么结构
Category之间形成的是一个偏序集.