from LexicalAnalyser import Lexer

source = "estas son palabras "
analyser = Lexer(source)
c = ""
while not c == None:
	c = analyser.nextToken()
	if not c == None:
		print(c)