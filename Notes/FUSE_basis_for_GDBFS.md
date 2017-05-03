# FUSE basis for GDBFS

### 1. 安装fusepy与如何使用fusepy挂载文件系统
安装FUSE（fusepy）：
```
pip install https://pypi.python.org/packages/source/f/fusepy/fusepy-2.0.4.tar.gz
```

如果没装pip的话要可以此时按照提示装pip
安装好后，对于写好的py文件（比如样例 `loopback.py`），就能将文件系统mount在mountpoint上。

`python loopback.py <root> <mountpoint>`

这里的`<root>` `<mountpoint>`都是用户自己设置的路径（路径不含尖括号），要注意mountpoint应是空目录。这个样例是把root的文件都映射到mountpoint。

fusepy支撑的loopback文件系统mount后需要保持terminal不关掉。
若要unmount这个文件系统，新打开一个terminal，输入  
`fusermount -u <mountpoint>`  
其中`<mountpoint>`是你挂载他的地方。


### 2. 利用FUSE实现文件系统

参考项目：
A FUSE filesystem for GridFS written in Python：
<https://github.com/stuartcarnie/gridfsfusepy>

Simple fusepy filesystem examples (include loopback.py):
<https://github.com/terencehonles/fusepy/tree/master/examples>

GridFS + FUSE (python)：  
<https://github.com/anthonyrisinger/gridfuse>

我们优先实现以下10个基本功能，有了这些功能，我们已经可以做到一个较为完整的文件系统了。
实现了这些函数后，我们日常对文件的操作（在文件浏览器中双击打开，用程序打开，各种形式的读写等等，都可以了）。这应该是文件系统的基本。
具体的函数功能以及如何实现，参考上述链接的例子应该就能完成。
```
create(self, path, mode)
getattr(self, path, fh=None)
read(self, path, size, offset, fh)
open(self, path, flags)
truncate(self, path, length, fh=None
write(self, path, data, offset, fh)
readdir(self, path, fh)
release(self, path, fh)
utimens(self, path, times=None)
mkdir(self, path, mode)
```




