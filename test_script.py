from LexicalAnalyser import Lexer

source = "dsfd/*l4534lfsdfsdl dfds   45"
analyser = Lexer(source)
for i in range(20):
    print(analyser.nextToken())
