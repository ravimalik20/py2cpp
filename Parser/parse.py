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
	def __init__(self,id,token):
		self.token=token
		self.id=id

	def __str__(self):
		return "[%d:%s]"%(self.id,self.token)

class Table:
	def __init__(self):
		self.table=[]
		self.top=-1

	def place(self,token):
		# Generate space for the token in the table.
		self.top+=1
		tk=Token(self.top,token)
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

	def find(self,token):
		for i in self.table:
			if i.token==token:
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

	def __str__(self):
		for i in self.table:
			print i
		return ""

# Literal Table
class LiteralTable(Table):
	def __init__(self):
		#self.table=[]
		#super(TerminalTable,self).__init__()
		Table.__init__(self)

	def __str__(self):
		for i in self.table:
			print i
		return ""

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

	def handle_string(self,quote,line,i,ust):
		'''Handles the extraction of a string literal from the given line.
		It returns the value of the counter of the line.		
		'''
		i=i+1
		self.place(quote)
		token=""
		while line[i]!=quote:
			token=token+line[i]
			i+=1;
		self.place(token,type_table['lit'])
		token=""
		self.place(quote,type_table['lit'])
		return i

	def type_token(self,token):
		for i in self.trm_table:
			if token==i.token:
				#print i.token
				return type_table['trm']		
		if token.isdigit():
			return type_table['lit']
		else:
			return type_table['ide']

	def place(self,token,type=None):
		if type==None:
			ty=self.type_token(token)
			if ty==type_table['trm']:
				token_obj=self.trm.find(token)
			elif ty==type_table['lit']:
				token_obj=self.lit.place(token)
			else:
				token_obj=self.ide.place(token)
		else:
			token_obj=self.lit.place(token)
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
						self.place(token)
						token=""
					break
				elif line[i]=="'":
					if len(token)!=0:
						self.place(token)
						token=""
					i=self.handle_string("'",line,i,self.ust)	# handle_string has to keep in mind to place the quotes in UST.
				elif line[i]=='"':
					if len(token)!=0:
						self.place(token)
						token=""
					i=self.handle_string('"',line,i,self.ust)
				elif line[i] in self.bchar:
					if len(token)!=0:
						self.place(token)
						token=""
					self.place(line[i])
				else:
					token=token+line[i]
				i+=1
		return self.ust

	def generate_file(self,f_name):
		f=open(f_name,"r")
		lines=f.readlines()

		return self.generate(lines)
	
if __name__=='__main__':
	# Generated all the three variables.
	trm=TerminalTable()
	lit=LiteralTable()
	ide=IdentifierTable()

	# Initialising the terminal Table.
	trm.generate('terminals.cpkl')

	# print the generated terminal table.
	print "Terminal Table",trm

	# Instantiating the parser.
	p=Parser(trm,lit,ide)

	#Generating the UST
	ust=p.generate_file(sys.argv[1])
	#ust=UniformSymbolTable()	
	#ust=ust.load('ust.cpkl')

	# Printing UST
	print "Uniform Symbol Table:",ust
	#ust.export('ust.cpkl')

	#lit=lit.load('lit.cpkl')
	print "Literal Table:",lit

	#ide=ide.load('ide.cpkl')
	print "Identifier Table",ide

	ust.export('UST.cpkl')
