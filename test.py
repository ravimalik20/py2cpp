import parse,syntax
import translate

import sys

if len(sys.argv)<3:
	print "File names not provided."
	sys.exit()

f_name_input=sys.argv[1]
f_name_output=sys.argv[2]

#################### Parser #########################

trm_table=parse.TerminalTable()
trm_table.generate("terminals.cpkl")

ide_table=parse.IdentifierTable()

lit_table=parse.LiteralTable()

# Declaring parser instance
parser=parse.Parser(trm_table,ide_table,lit_table)

ust=parser.generate_file(f_name_input)

#################### Parser #########################

###################### Syntax Analyzer ######################

# Declaring syntax analyzer
syntax_analyzer=syntax.SyntaxAnalyzer()

syntax_analyzer.parse_statements(ust)

syntax_analyzer.pre_process_statements()

syntax_analyzer.classify()

###################### Syntax Analyzer ######################

######################## Translator ######################

# Declaring translator
translator=translate.Translator()
output=translator.translate(syntax_analyzer.statements)

######################## Translator ######################

# Fetching Compulsary Includes
f=open("compulsary_includes","r")
includes=f.read()
f.close()

f=open(f_name_output,"w")

f.write(includes)
f.write("\nint main()\n{")
for i in output:
	f.write(i)

f.write("\nreturn 0;\n}")