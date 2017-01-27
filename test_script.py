from LexicalAnalyser import Lexer

source = "letras [123] {14.21} 1a asd2 1.3 1.fsa+ 98 <>=<<>= ==/ //*/ df; dsfs. sdfs,1.a"
analyser = Lexer(source)
for i in range(10):
    print(analyser.nextToken())
