#!/usr/bin/python
# -*- coding: utf-8 -*-

# auto_cp.py 自动拷贝工具 version 0.0.1   2016-2-18


import os, shutil
import time
import re

class Autocp(object):
	#初始化方法，需要指定公共下载路径，和匹配类型，检查时间
	def __init__(self, down_load_dir, check_interval=60):
		self.pub_down_load = down_load_dir
		self.match_tuple = []
		self.check_interval = check_interval

	def add_match_tuple(self, tuple):
		self.match_tuple.append(tuple)
	def del_match_tuple(self, tuple):
		try:
			self.match_tuple.remove(tuple)
		except ValueError, e:
			print 'ValueError:', e
		else:
			print 'delete match tuple', tuple, 'successfully'
	def show_match_tuple(self):
		print 'show the match tuple list:'
		for tuple in self.match_list:
			print tuple

	def cp_newer_files(self):
		check_time = time.time()
		for tuple in self.match_tuple:
			dir = tuple[0]
			re_match = tuple[1]
			#print re_match
			for f in os.listdir(dir):
				if re.match(re_match, f):
					#print f
					filepath=os.path.join(dir, f)
					file_state = os.stat(filepath)
					interval = check_time - file_state.st_mtime
					#print f, file_state.st_mtime, check_time
					if interval <= self.check_interval:
						if os.path.exists(filepath):
							now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
							print 'copy file %s %s' % (filepath, now)
							dstpath=os.path.join(self.pub_down_load, f)
							shutil.copy(filepath, dstpath)


public_download_path = r'C:\Users\zyh\Desktop\FTP_PATH'
match_tuple1 = (r'Z:\bb1407\bin\ar71xx', r'BD.+\.bin')
match_tuple2 = (r'X:\octeon\OCTEON-SDK\linux\kernel\linux', r'vmlinux\.64')
match_tuple_list = [match_tuple1, match_tuple2]

def do_auto_cp():
	first_cp = Autocp(public_download_path)
	for tuple in match_tuple_list:
		first_cp.add_match_tuple(tuple)

	while True:
		first_cp.cp_newer_files()
		time.sleep(first_cp.check_interval)

if __name__ == '__main__':
	do_auto_cp()

