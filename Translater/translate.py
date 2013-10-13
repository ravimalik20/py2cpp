# Translator:
# Receives list of statement objects and outputs the list of string objects

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

	def show_grammer(self):
		self.grammer.show()
		
