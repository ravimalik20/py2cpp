from Parser import parse,syntax
from Translater import translate

import sys

if len(sys.argv)<2:
	print "File name to be converted not provided."
	sys.exit()

f_name=sys.argv[1]

trm_table=parse.TerminalTable()
trm_table.generate("Parser/terminals.cpkl")

ide_table=parse.IdentifierTable()

lit_table=parse.LiteralTable()

# Declaring parser instance
parser=parse.Parser(trm_table,ide_table,lit_table)

# Declaring syntax analyzer
syntax_analyzer=syntax.SyntaxAnalyzer()

# Declaring translator
translator=translate.Translator()

# Generating UST
ust=parser.generate_file(f_name)

# doing syntax analysis
syntax_analyzer.parse_statements(ust)

syntax_analyzer.pre_process_statements()

syntax_analyzer.classify()

# Translating statements
output=translator.translate(syntax_analyzer.statements)

for i in output:
	print i