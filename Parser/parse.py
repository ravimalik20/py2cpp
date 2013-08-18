# Parser to parse the python source code and create the uniform symbol table.
# 
# Author : Ravi Malik

import cPickle as cp

class Token:
	'''Token Object'''

	def __init__(self):
		self.id=-1
		self.token=""

class Terminal(Token):
	'''Terminal Object'''
	def __init__(self,i,t):
		self.id=i
		self.token=t

class Literal(Token):
	'''Literal Object'''
	def __init__(self,i,t):
		self.id=i
		self.token=t


class Identifier(Token):
	'''Identifier Object'''
	def __init__(self,i,t):
		self.id=i
		self.token=t

class TerminalTable:
	'''Terminal Table'''

	def __init__(self,f_name):		
		self.trm_tab=[]

		f=open(f_name,"r")
		trm=cp.load(f)
		
		i=0
		while i<len(trm):
			t=Terminal(i,trm[i])
			self.trm_tab.append(t)
			i=i+1

	def __str__(self):
		t=""
		for i in self.trm_tab:
			t=t+"["+str(i.token)+"]"
		return t

if __name__=='__main__':
	tt=TerminalTable("terminals.cpkl")

	print tt
