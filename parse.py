# Parser Generator for the Python Source Code
#
# Author: Ravi Malik

# Token:
#	String containing token
#	Id in the corresponding table 
# 
# Terminal Table: 
#	List of Tokens
#
# Identifier Table:
# 	List of Tokens
#
# Literal Table:
#	List of Tokens
#
# Type Table: Mapping of type string to an integer representation : Implemented via a hash table
#
# Uniform Symbol Table:
#	Id in UST	
#	Token
#	Type : stored as an int and refered from the type table
#
# Parser: Accepts a terminal table, literal table, identifier table and gives the uniform symbol table
#
# Procedure to follow while developing:
#
# *1. Define all the objects.
# *2. Generate the Terminal Table.
# *3. Read the source file and seperate all the tokens.
# *4. Place the tokens into the UST, donot identify the type of tokens yet.
# 5. Now traverse over the UST and identify the type of each token.
# 6. Parsing Complete.

import cPickle as CP
import sys

class Token:
	def __init__(self,id,name):
		self.name=name
		self.id=id

	def __str__(self):
		return "[%d:%s]"%(self.id,self.name)

class Table:
	def __init__(self):
		self.table=[]
		self.top=-1

	def place(self,token_name):
		# Generate space for the token in the table.
		self.top+=1
		tk=Token(self.top,token_name)
		self.table.append(tk)

		return tk

	def export(self,f_name):
		f=open(f_name,'w')
		CP.dump(self,f)
		f.close()

	def load(self,f_name):
		f=open(f_name,'r')
		tb=CP.load(f)
		f.close()
		return tb

	def __str__(self):
		for i in self.table:
			print i
		return ""

# Terminal Table
class TerminalTable:
	def __init__(self):
		self.table=[]
		#super(TerminalTable,self).__init__()
		#Table.__init__(self)

	def generate(self,f_name):
		if len(self.table)!=0:
			print "Table not empty!! Cannot Generate!!"
			return None
		else:
			# Loading the terminals(str)
			f=open(f_name,"r")
			terms=CP.load(f)
			f.close()

			# Generating the actual terminal table which is a collection of token objects.
			for i in range(0,len(terms)):
				self.table.append(Token(i,terms[i]))

			print "Terminal Table generated from file %s!!"%f_name

	def find(self,token_name):
		for i in self.table: 
			if i.name==token_name:
				return i
		return None

	def __str__(self):
		for i in self.table:
			print i
		return ""

# Identifier Table
class IdentifierTable(Table):
	def __init__(self):
		#self.table=[]
		#super(TerminalTable,self).__init__()
		Table.__init__(self)

	

# Literal Table
class LiteralTable(Table):
	def __init__(self):
		#self.table=[]
		#super(TerminalTable,self).__init__()
		Table.__init__(self)


type_table={'trm':1,'lit':2,'ide':3,1:'trm',2:'lit',3:'ide'}

# Element of a UST
class USTElement:
	def __init__(self,id,token,type):
		self.id=id
		self.token=token
		self.type=type

	def __str__(self):
		return "%d:%s:%s"%(self.id,self.token,type_table[self.type])

# Uniform Symbol Table
class UniformSymbolTable:
	def __init__(self):
		self.table=[]
		self.top=-1

	def place(self,token,type):
		self.top+=1

		# At present token is stored as a string but it has to be a token object. For that we have to find the type of the token.
		u=USTElement(self.top,token,type)	
		self.table.append(u)

	def export(self,f_name):
		f=open(f_name,'w')
		CP.dump(self,f)
		f.close()

	def load(self,f_name):
		f=open(f_name,'r')
		tb=CP.load(f)
		f.close()
		return tb

	def __str__(self):
		for i in self.table:
			print i
		return " "

class Parser:
	def __init__(self,trm,lit,ide):
		# All the tables.
		self.trm=trm
		self.lit=lit
		self.ide=ide
		
		self.trm_table=trm.table
		self.lit_table=lit.table
		self.ide_table=ide.table

		# List of break charachters.
		self.bchar=[' ',
			'\n','~','`','!','@','#','$','%','^','*','(',')','-','+','=','{','}','[',']',':',';','"',"'",'<','>',",",'.','/',
			'\t',
		] 

	def __handle_string(self,quote,line,i,ust):
		'''Handles the extraction of a string literal from the given line.
		It returns the value of the counter of the line.		
		'''
		i=i+1
		self.__place(quote)
		token=""
		while line[i]!=quote:
			token=token+line[i]
			i+=1;
		self.__place(token,type_table['lit'])
		token=""
		self.__place(quote,type_table['lit'])
		return i

	def __type_token(self,token_name):
		for i in self.trm_table:
			if token_name==i.name:
				#print i.token
				return type_table['trm']		
		if token_name.isdigit():
			return type_table['lit']
		else:
			return type_table['ide']

	def __place(self,token_name,type=None):
		if type==None:
			ty=self.__type_token(token_name)
			if ty==type_table['trm']:
				token_obj=self.trm.find(token_name)
			elif ty==type_table['lit']:
				token_obj=self.lit.place(token_name)
			else:
				token_obj=self.ide.place(token_name)
		else:
			token_obj=self.lit.place(token_name)
			ty=type
		self.ust.place(token_obj,ty)

	def generate(self,lines):
		'''lines must contain an ending \n char.'''
		self.ust=UniformSymbolTable()
		for line in lines:
			i=0
			n=len(line)
			token=""
			while i<n:
				if line[i]=="#":
					if len(token)!=0:
						self.__place(token)
						token=""
					break
				elif line[i]=="'":
					if len(token)!=0:
						self.__place(token)
						token=""
					i=self.__handle_string("'",line,i,self.ust)	# handle_string has to keep in mind to place the quotes in UST.
				elif line[i]=='"':
					if len(token)!=0:
						self.__place(token)
						token=""
					i=self.__handle_string('"',line,i,self.ust)
				elif line[i] in self.bchar:
					if len(token)!=0:
						self.__place(token)
						token=""
					self.__place(line[i])
				else:
					token=token+line[i]
				i+=1
		return self.ust

	def generate_file(self,f_name):
		f=open(f_name,"r")
		lines=f.readlines()

		return self.generate(lines)
