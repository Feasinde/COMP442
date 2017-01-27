from LexicalAnalyser import Lexer

source = "antes/*  sda   */despues"
analyser = Lexer(source)
analyser.reader()