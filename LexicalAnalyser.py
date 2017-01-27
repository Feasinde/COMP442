import re

class Lexer:
        s_source_program = ""
        i_index = -1

        ## Constructor takes the source program as a string
        def __init__(self, s_source_program):
                self.s_source_program = s_source_program

        ## Returns next character in the source program string.
        ## If first-time call, returns first character in the
        ## source program string
        def __nextChar(self):
                self.i_index+=1
                if self.i_index >= len(self.s_source_program): return " "
                return self.s_source_program[self.i_index]
        
        ## Returns previous character in the source program string
        def __backupChar(self):
                self.i_index-=1
                return self.s_source_program[self.i_index]

        ## Returns character immediately ahead of current character
        def __lookAhead(self):
                return self.s_source_program[self.i_index+1]

        ## Returns true if string is a reserved word
        def __isReservedWord(self, s_word):
                reserved_words = ["if",
                "then",
                "else",
                "for",
                "class",
                "int",
                "float",
                "get",
                "put",
                "return",
                "program",
                "and", "or", "not",
                ]
                if s_word in reserved_words: return True
                return False

        ## Resets source program string and index
        def reset(self, s_source_program):
                self.s_source_program = s_source_program
                self.i_index = -1

        def reader(self):
                for i in self.s_source_program:
                        type_token = self.nextToken()
                        if not type_token == None: print(type_token)

        def nextToken(self):
                s_type = ""
                c = self.__nextChar()
                ## Determine if c is a letter
                letter_match = re.search("[a-zA-Z]", c)
                if letter_match:
                        l_token = [c]
                        c = self.__nextChar()
                        ## Determine all alphanumeric characters in token
                        alphanumeric_match = re.search("[a-zA-Z0-9]",c)
                        while alphanumeric_match:
                                l_token.append(c)
                                c = self.__nextChar()
                                alphanumeric_match = re.search("[a-zA-Z0-9]",c)
                        c = self.__backupChar()
                        s_token = "".join(l_token)
                        ## Determine if s_token is a reserved word
                        if self.__isReservedWord(s_token): return ("RESWORD",s_token)
                        return ("ID",s_token)
                ## Determine if c is a number
                number_match = re.search("[0-9]",c)
                if number_match:
                        l_token = [c]
                        c = self.__nextChar()
                        ## Determine if there are any numbers after initial
                        ## number
                        number_match = re.search("[0-9]",c)
                        while number_match:
                                l_token.append(c)
                                c = self.__nextChar()
                                number_match = re.search("[0-9]",c)
                        ## Determine if there is a period. If not return
                        ## token as a NUM
                        if c == ".":
                                c_ahead = self.__lookAhead()
                                number_match = re.search("[0-9]",c_ahead)
                                if not number_match:
                                        c = self.__backupChar()
                                        s_token = "".join(l_token)
                                        return ("INT",s_token)
                                while number_match:
                                        l_token.append(c)
                                        c = self.__nextChar()
                                        number_match = re.search("[0-9]",c)
                                c = self.__backupChar()
                                s_token = "".join(l_token)
                                return ("FLOAT", s_token)
                        c = self.__backupChar()
                        s_token = "".join(l_token)
                        return ("INT", s_token)
                ## If c is a period, determine if it is the
                ##beginning of a fraction or a stand-alone punctuation mark
                if c == ".":
                        l_token = [c]
                        c = self.__nextChar()
                        if re.search("[0-9]",c):
                                l_token.append(c)
                                c = self.__nextChar()
                                while re.search("[0-9]",c):
                                        l_token.append(c)
                                        c = self.__nextChar()
                                c = self.__backupChar()
                                s_token = "".join(l_token)
                                return ("FRAC", s_token)
                        c = self.__backupChar()
                        return ("PUNCT", c)
                
                ## Determine if c is any punctuation mark of
                ## the following: ; : ,
                if c == ";" or c == ":" or c == ",": return ("PUNCT", c)

                ## Determine if c is one of the following
                ## operators: +, -, *
                if c == "+" or c == "-" or c == "*":
                        return ("OP", c)

                # Determine if c is the operator = or if it
                # is a part of the assign operator ==
                if c == "=":
                        c = self.__nextChar()
                        if c == "=": return ("OP", "==")
                        c = self.__backupChar()
                        return ("OP", "=")

                ## Determine if a character is the operator < or if it
                ## is a part of either the operator <= or <>
                if c == "<":
                        c = self.__nextChar()
                        if c == "=": return ("OP", "<=")
                        elif c == ">": return ("OP", "<>")
                        else:
                                c = self.__backupChar()
                                return ("OP",c)
                ## Determine if c is the operator > or if it
                ## is a part of the operator >=
                if c == ">":
                        c = self.__nextChar()
                        if c == "=": return ("OP", ">=")
                        c = self.__backupChar()
                        return ("OP", ">")

                ## Determine if c is the division operator / or
                ## if it is a part of a comment marker /* or //
                if c == "/":
                		c = self.__nextChar()
                		if c == "*": return("PUNCT", "/*")
                		if c == "/": return("PUNCT", "//")
                		c = self.__backupChar()
                		return ("OP", "/")

                ## Determine if c is a parenthesis, a curly bracket,
                ## or a bracket
                if c == "(" or c == "{" or c == "[": return ("PUNCT", c)
                if c == ")" or c == "}" or c == "]": return ("PUNCT", c)
