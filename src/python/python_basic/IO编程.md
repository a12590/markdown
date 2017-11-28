1、IO
with open('/path/to/.','r') as f:
	print(f.read())
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，
要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。

2、前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、
视频等等，用'rb'模式打开文件即可：要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，
例如，读取GBK编码的文件：

with open('/path/to/.','rb',encoding = 'gbk')

3、你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
with open('/path/to/.','w') as f:
	f.write('..')
	
StringIO和BytesIO
很多时候，数据读写不一定是文件，也可以在内存中读写。
'中文'.encode('utf-8')

