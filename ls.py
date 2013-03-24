class ls:
    def __init__(self,dir):
	self.dir=dir
	import os
	files=os.listdir(self.dir)
	for i in files:
	    print i
a=ls('D:\django')
