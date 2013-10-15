from translate import Translator

t=Translator()

t.show_grammer()

class Token:
	def __init__(self,id,name):
		self.name=name
		self.id=id

	def __str__(self):
		return "[%d:%s]"%(self.id,self.name)

class Statement:

	def __init__(self,stat):
		self.statement=stat[:]
		self.type=-1

	def __str__(self):
		for i in self.statement:
			print i
		return ""

	def __getitem__(self,index):
		return self.statement[index]

s=[Token(0,'if'),Token(0,'a'),Token(0,'<'),Token(0,'='),Token(0,'b'),Token(0,':')]

stat=Statement(s)

print stat

print t.translate_if(stat)

s=[Token(0,'else'),Token(0,':')]

stat=Statement(s)

print t.translate_else(stat)

s=[Token(0,'while'),Token(0,'a'),Token(0,'<'),Token(0,'b'),Token(0,'and'),Token(0,'c'),Token(0,'>'),Token(0,'d'),Token(0,':')]

stat=Statement(s)

print t.translate_loop_while(stat)

s=[Token(0,'class'),Token(0,'hello_world'),Token(0,':')]

stat=Statement(s)

print t.translate_declaration_class(stat)