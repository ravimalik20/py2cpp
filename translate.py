# Translator:
# Receives list of statement objects and outputs the list of string objects

from syntax import stat_type
from parse import type_table
from syntax import Statement


class Grammer:
	def __init__(self):
		self.if_=[]
		self.else_=[]
		self.loop_while=[]
		self.loop_for=[]
		self.declaration_function=[]
		self.declaration_class=[]

	def generate(self,f_name):
		'''Generate the grammer of the output source code'''

		f=open(f_name,"r")

		line=f.readline()
		while len(line)!=0:
			output=[]
			token=""
			a=0
			while a<len(line):
				#print line[a]
				if line[a]=='[':
					#print 2
					a+=1
					while line[a]!=']':
						token=token+line[a]
						a+=1
					head=token	# Grammer identifying element
					#print head
					token=""
					line=f.readline()
					b=0
					while b<len(line):
						if line[b]=="<":
							if len(token)!=0:
								output.append(token)
								token=""
							token=token+line[b]
							b+=1
							while line[b]!=">":
								token=token+line[b]
								b+=1
							token=token+">"
							output.append(token)
							token=""
						elif line[b]=="\n":
							if len(token)!=0:
								output.append(token)
								token=""
						else:
							token=token+line[b]

						b+=1
					# Placing the grammer into appropriate list
					if head=="if":
						self.if_=output[:]
					elif head=="else":
						self.else_=output[:]
					elif head=="loop_while":
						self.loop_while=output[:]
					elif head=="loop_for":
						self.loop_for=output[:]
					elif head=="declaration_function":
						self.declaration_function=output[:]
					elif head=="declaration_class":
						self.declaration_class=output[:]

				a+=1
			line=f.readline()
		f.close()

	def show(self):
		print "Grammer [if] :",self.if_
		print "Grammer [else] :",self.else_
		print "Grammer [loop_while] :",self.loop_while
		print "Grammer [loop_for] :",self.loop_for
		print "Grammer [declaration_function] :",self.declaration_function
		print "Grammer [declaration_class] :",self.declaration_class

class Translator:
	def __init__(self):
		self.grammer=Grammer()
		self.grammer.generate('output_grammer')
		self.__arithmetic_ide_table=[]

	def show_grammer(self):
		self.grammer.show()

	def __process_condition(self,condition):
		condition=self.translate_arithmetic(Statement(condition))
		return condition

	def translate_if(self,statement):
		if statement[0].token.name!="if":
			print "Not an if statement!!"
		else:
			condition=""
			cond=[]
			a=1
			while statement[a].token.name!=":":
				#condition+=statement[a].token.name
				cond.append(statement[a])
				a+=1
			# Process condition
			condition=self.__process_condition(cond)[:-1]

			# import grammer into a temp location
			if_grammer=self.grammer.if_[:]
			# find the index of the condition place holder
			i=if_grammer.index("<condition>")
			# fill in the place holder
			if_grammer[i]=condition

			stat=""
			for i in if_grammer:
				stat+=i

			return stat

	def translate_else(self,statement):
		if statement[0].token.name!="else":
			print "Not an else statement!!"
		else:
			# import grammer into a temp location
			else_grammer=self.grammer.else_[:]
			
			stat=""
			# generating string out of the processed grammer
			for i in else_grammer:
				stat+=i

			return stat

	def translate_loop_while(self,statement):
		if statement[0].token.name!="while":
			print "Not a while statement!!"
		else:
			# importing loop_while grammer
			loop_while_grammer=self.grammer.loop_while[:]
			# extracting condition out of python statement
			cond=[]
			condition=""
			a=1
			while statement[a].token.name!=":":
				condition+=statement[a].token.name
				cond.append(statement[a])
				a+=1
			# Process condition
			condition=self.__process_condition(cond)[:-1]

			# fetching the index of condition in grammer
			i=loop_while_grammer.index("<condition>")

			# filling in the place holder
			loop_while_grammer[i]=condition

			# Converting processed grammer to actual statement
			stat=""
			for i in loop_while_grammer:
				stat+=i

			return stat

	def __translate_loop_for(self,statement):
		pass

	def __translate_declaration_function(self,statement):
		pass

	def translate_declaration_class(self,statement):
		if statement[0].token.name!="class":
			print "Not a class declaration statement!!"
		else:
			# importing declaration_class grammer
			declaration_class_grammer=self.grammer.declaration_class[:]

			# extracting class_name from the statement
			class_name=""
			a=1
			while statement[a].token.name!=":":
				class_name+=statement[a].token.name
				a+=1

			# fetching index of the class_name placeholder in grammer
			i=declaration_class_grammer.index("<class_name>")

			# filling the placeholder
			declaration_class_grammer[i]=class_name

			# converting processed grammer to string
			stat=""
			for i in declaration_class_grammer:
				stat+=i

			return stat

	def translate_arithmetic(self,statement):
		declarations=""
		stat=""
		# flag showing if the current statement has an assignment or not
		assign=0
		a=0
		n=len(statement.statement)

		while a<n:
			if statement[a].token.name=="int" or statement[a].token.name=="float":
				stat+="(%s)"%statement[a].token.name
			elif statement[a].type==type_table['ide']:
				try:
					if statement[a+1].token.name=="=":
						if statement[a].token.name in self.__arithmetic_ide_table:
							pass
						else:
							declarations+="\nVar %s;\n"%statement[a].token.name
							self.__arithmetic_ide_table.append(statement[a].token.name)
						stat+="%s.put("%statement[a].token.name
						assign=1
						a+=1
					elif statement[a+1].token.name=="(":
						stat+=statement[a].token.name
					elif statement[a+1].token.name=="%":
						stat+="fmod(GET(%s),GET(%s))"%(statement[a].token.name,statement[a+2].token.name)
						a+=2
					else:
						if statement[a].token.name in self.__arithmetic_ide_table:
							pass
						else:
							declarations+="\nVar %s;\n"%statement[a].token.name
							self.__arithmetic_ide_table.append(statement[a].token.name)
						stat+="GET(%s)"%statement[a].token.name
				except IndexError:
					if statement[a].token.name in self.__arithmetic_ide_table:
						pass
					else:
						declarations+="\nVar %s;\n"%statement[a].token.name
						self.__arithmetic_ide_table.append(statement[a].token.name)
					stat+="GET(%s)"%statement[a].token.name
			elif statement[a].token.name=="and":
				stat+=" && "
			elif statement[a].token.name=="or":
				stat+=" || "
			elif statement[a].token.name=="not":
				stat+=" ! "
			else:
				stat+=" %s "%statement[a].token.name

			a+=1

		out=declarations+stat
		if assign==1:
			out+=");"
		else:
			out+=";"

		return out

	def translate_standard_output(self,statement):
		a=0
		while statement[a].token.name==" " or statement[a].token.name=="\t":
			a+=1
		if statement[a].token.name!="print":
			print "Not a Standard Output Statement!!"
		else:
			stat=statement.statement[a+1:]
			stat=self.__process_condition(Statement(stat))
			
			out=""
			for i in stat:
				if i==",":
					out+="<<"
				else:
					out+=i

			out="cout<<"+out

			return out

	def translate(self,statements):
		output=[]
		out=""
		for i in statements:
			out=""
			if i=='BLOCK_START':
				out="{"
			elif i=='BLOCK_END':
				out="}"
			elif i.type==stat_type['if']:
				out=self.translate_if(i)
			elif i.type==stat_type['else']:
				out=self.translate_else(i)
			elif i.type==stat_type['loop_while']:
				out=self.translate_loop_while(i)
			elif i.type==stat_type['declaration_class']:
				out=self.translate_declaration_class(i)
			elif i.type==stat_type['arithmetic']:
				out=self.translate_arithmetic(i)
			elif i.type==stat_type['standard_output']:
				out=self.translate_standard_output(i)
			output.append(out+"\n")

		return output