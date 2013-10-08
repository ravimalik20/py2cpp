# Test script for the parser module.

import parse
import syntax
import sys

# Checking command line arguments
f_name=None
try:
	f_name=sys.argv[1]
except:
	print "Please supply the name of the file to parse as a command line argument."
	sys.exit()

#################### Parsing the source code #############################

# Declared all the tables
trm=parse.TerminalTable()
lit=parse.LiteralTable()
ide=parse.IdentifierTable()

# Generating the terminal table from the file
trm.generate('terminals.cpkl')

# Declare the Parser instance
PS=parse.Parser(trm=trm,lit=lit,ide=ide)

# Generating Uniform Symbol Table from file.
ust=PS.generate_file(f_name)

# Print UST
print ust

############### Parsing Done now analyzing syntax ########################

# Declared the Syntax Analyzer.
SA=syntax.SyntaxAnalyzer()

# Identify statements from the UST.
SA.parse_statements(ust)

# Printing the statements identified.
SA.show()

# Pre-Processing the statements
print "After Pre-Processing:"
SA.pre_process_statements()

# Printing the now processed stataments
SA.show()

# Identifying types of statements
SA.classify()

# Printing the now processed stataments
print "After classifying statements:"
SA.show()
