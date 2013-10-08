# To identify statements, verify them and categorise them.

import cPickle as cp
from parse import *

stat_type={
	-1:None,
	1:'if',
	2:'else',
	3:'loop_while',
	4:'loop_for',
	5:'declaration_function',
	6:'declaration_list',
	7:'declaration_tupple',
	8:'declaration_dictionary',
	9:'declaration_class',
	10:'standard_output',
	'if':1,
	'else':2,
	'loop_while':3,
	'loop_for':4,
	'declaration_function':5,
	'declaration_list':6,
	'declaration_tupple':7,
	'declaration_dictionary':8,
	'declaration_class':9,
	'standard_output':10,
}

class Statement:

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

	def classify(self):
		'''Classify the statements into different types'''
		a=0
		while a<len(self.statements):
			b=0
			# Skipping to first non space charachter
			while self.statements[a].statement[b].token.name==' ' or self.statements[a].statement[b].token.name=='\t':
				b+=1
			# Main Classification logic goes here
			if self.statements[a].statement[b].token.name=='if':
				self.statements[a].type=stat_type['if']
			elif self.statements[a].statement[b].token.name=='else':
				self.statement[a].type=stat_type['else']
			elif self.statements[a].statement[b].token.name=='for':
				self.statements[a].type=stat_type['loop_for']
			elif self.statements[a].statement[b].token.name=='while':
				self.statements[a].type=stat_type['loop_while']
			elif self.statements[a].statement[b].token.name=='def':
				self.statements[a].type=stat_type['declaration_function']
			elif self.statements[a].statement[b].token.name=='class':
				self.statements[a].type=stat_type['declaration_class']
			elif self.statements[a].statement[b].token.name=='print':
				self.statements[a].type=stat_type['standard_output']
			a+=1
	def show(self):
		for i in self.statements:
			print "Statement"
			print "Type:",stat_type[i.type]
			print i

