# To identify statements, verify them and categorise them.

import cPickle as cp
from parse import *

class SyntaxAnalyzer:
	def __init__(self):
		self.statements=[]
		self.bchar=['\n',';']

	def parse_statements(self,ust):
		stat=[]
		for i in ust.table:
			if i.token.token in self.bchar:
				if len(stat)!=0:
					self.statements.append(stat)
					stat=[]
			else:
				stat.append(i)

	def show(self):
		for i in self.statements:
			print "Statement"
			for j in i:
				print j

if __name__=='__main__':
	f=open('ust.cpkl')

	ust=cp.load(f)

	f.close()

	sa=SyntaxAnalyzer()

	sa.parse_statements(ust)
	
	sa.show()
