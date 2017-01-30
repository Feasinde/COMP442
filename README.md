#LexicalAnalyser

Simple lexer that takes a string or a text file and outputs a list of tokens according to the lexical specification given in the assignment sheet.

#Usage

LexicalAnalyser is a Python module with a command-line interface. Simply run the script from the shell and specify whether the input is a string or a text file, and whether you want the output on the shell or in a file.

##Example of use:

`$ python3 LexicalAnalyser.py -s 'HOLA MUNDO'`

The above line takes the string 'HOLA MUNDO' and outputs the two constituent tokens, 'HOLA' and 'MUNDO'.

`$ python3 LexicalAnalyser.py -s 'BONJOUR LE MONDE' -o output.txt`

The above line takes the string 'BONJOUR LE MONDE' and outputs its constituents to the file `output.txt`.

`$ python3 LexicalAnalyser.py -f hello_world.txt`

The above line takes the file `hello_world.txt` and outputs its constituent tokens.

`$ python3 LexicalAnalyser.py -f hello_world.txt -o output.txt`

The above line takes the file `hello_world.txt` and outputs its constituent tokens to the file `output.txt`.
