# To identify statements, verify them and categorise them.

import cPickle as cp
from parse import *

class Statement:
	stat_type={}

	def __init__(self,stat):
		self.statement=stat[:]
		self.type=-1

	def __str__(self):
		for i in self.statement:
			print i
		return ""

class SyntaxAnalyzer:
	def __init__(self):
		self.statements=[]
		self.bchar=['\n',';']

	def parse_statements(self,ust):
		stat=[]
		for i in ust.table:
			if i.token.token in self.bchar:
				if len(stat)!=0:
					self.statements.append(Statement(stat))
					stat=[]
			else:
				stat.append(i)

	def show(self):
		for i in self.statements:
			print "Statement"
			print i
				

if __name__=='__main__':
	f=open('ust.cpkl')

	ust=cp.load(f)

	f.close()

	sa=SyntaxAnalyzer()

	sa.parse_statements(ust)
	
	sa.show()
