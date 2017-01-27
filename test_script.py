from LexicalAnalyser import Lexer

source = "letras [123] {14.21} 1a asd2 1.3 1.fsa+ 98 <>=<<>= ==/ //*/ df; dsfs. sdfs,"
analyser = Lexer(source)
analyser.reader()