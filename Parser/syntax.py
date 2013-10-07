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
			if i.token.name in self.bchar:
				if len(stat)!=0:
					self.statements.append(Statement(stat))
					stat=[]
			else:
				stat.append(i)

	def pre_process_statements(self):
		'''Remove the spaces from within the statements but not from the starting'''
		for i in range(0,len(self.statements)):
			# Assumed index of the first non space charachter.
			a=0
			while self.statements[i].statement[a].token.name==" " or self.statements[i].statement[a].token.name=="\t":
				a+=1  
			#print "A:%d"%a 
			j=a
			n=len(self.statements[i].statement)
			while j<n:
				if self.statements[i].statement[j].token.name==" " or self.statements[i].statement[j].token.name=="\t":
					#print "Del"					
					del self.statements[i].statement[j]
					n-=1
				else:
					j+=1
				
	def show(self):
		for i in self.statements:
			print "Statement"
			print i

