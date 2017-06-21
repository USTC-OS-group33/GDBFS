#GDBFS实现 mongoDB部分文档



## mongoDB简记

MongoDB是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。他支持的数据结构非常松散，是类似json的bson格式，因此可以存储比较复杂的数据类型。Mongo最大的特点是他支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。
这里调用mongoDB的Python的API，从而实现对文件的基本操作。

## 安装mongoDB和pymongo

在这里我们可以直接通过命令行来安装，也可以使用手动方法安装：


1.命令行安装方式
	安装mongoDB：
	sudo apt-get install mongodb
	
	安装pymongo：
	python -m pip install pymongo
	或者：
	python -m pip install pymongo==3.1.1
	注意此法需要安装pip。

2.手动安装mongoDB
	MongoDB包下载地址：http://www.mongodb.org/downloads
	首先要从官网上下载你所需要的安装包
	在文件夹里创建mongoDB文件夹，命令如下：
　　　	cd usr/local/ 
	mkdir mongoDB
	cd mongoDB/
	然后将在上面下载的mongoDB包复制到mongoDB文件夹里面，并且将包解压，解压之后命名为mongoDB
	eg： tar -zxvf mongodb-linux-x86_64-3.2.8.tgz 
	     mv mongodb-linux-x86_64-3.2.8 mongodb
	解压之后跳转到mongodb下进行操作(cd mongodb/)
	db文件夹的作用是存放数据库目录，logs文件夹的作用是存放mongoDB的操作日志信息：
	 mkdir db
	mkdir logs
	添加完成之后，启动mongoDB，验证是否安装成功，这里指定的数据库目录选项为mongodb下创建的db，命令如下：
	./bin/mongod --dbpath /usr/local/kencery/mongoDB/mongodb/db

	注意：你可能会需要配置.conf文件，详细参数见下衔接：
	http://blog.csdn.net/fdipzone/article/details/7442162
	
mongoDB的官方文档给出了很多问题的详细解释：
https://www.mongodb.com/faq?jmp=footer



### pymongo的应用

这里调用了pymongo还有gridfs。
pymongo是用来连接mongoDB数据库，gridfs是用来存放大型文件。

1.pymongo：
通过直接调用函数即可实现连接，
这里不推荐使用admin：admin@//127.0.0/27017/的方式连接，因为这个衔接是默认的，可能会带来错误。
链接之后调用gridfs。

2.gridfs：
gridfs在pymongo文档中有提到：
http://api.mongodb.com/python/current/api/gridfs/#module-gridfs

我们通过调用gridfs完成读，写等基本操作。



	
