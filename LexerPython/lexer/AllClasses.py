#Valter Nunez - A01206138

#Token Class
class Token:
    def __init__(self, tag):
        self.tag = tag
    #Getter
    def getToken(self):
        return self.tag

    def toString(self):
        return "TOKEN - VALUE = " + str(self.tag)

#CharacterString class
class CharacterString(Token):
    def __init__(self, value):
        super().__init__(Tag.CHARACTERSTRING)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "STRING - VALUE = " + str(self.value)

#Integer Class
class Integer(Token):
    def __init__(self, value):
        super().__init__(Tag.INTEGER)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "INTEGER - VALUE = " + str(self.value)
#Real class
class Real(Token):
    def __init__(self, value):
        super().__init__(Tag.REAL)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "REAL - VALUE = " + str(self.value)

#Tag Class
class Tag:
    EOF = 65535
    PROGRAM = 256
    CONSTANT = 257
    VAR = 258
    BEGIN = 259
    END = 260
    INTEGER = 261
    REAL = 262
    BOOLEAN = 263
    STRING = 264
    ASSIGN = 265
    WRITELN = 266
    READLN = 267
    WHILE = 268
    DO = 269
    REPEAT = 270
    UNTIL = 271
    FOR = 272
    TO = 273
    DOWNTO = 274
    IF = 275
    THEN = 276
    ELSE = 277
    NOT	= 278
    EQ = 279
    NEQ = 280
    GE = 281
    LE = 282
    FALSE = 283
    TRUE = 284
    DIV = 285
    MOD = 286
    AND = 287
    OR = 288
    MINUS = 289
    ID = 290
    CHARACTERSTRING = 291
    COMMENTS = 292
    ERROR = 293;



#Word Class
class Word(Token):
    def __init__(self, lexeme, tag):
        super().__init__(tag)
        self.lexeme = lexeme
    #Getter
    def getLexeme(self):
        return str(self.lexeme)

    def toString(self):
        return "WORD - LEXEME = " + self.lexeme

eq = Word("==", Tag.EQ)
ne = Word("<>", Tag.NEQ)
le = Word("<=", Tag.LE)
ge = Word(">=", Tag.GE)
minus = Word("minus", Tag.MINUS)
assign = Word(":=", Tag.ASSIGN)
true = Word("true", Tag.TRUE)
false = Word("false", Tag.FALSE)

words_list = [eq, ne, le, ge, minus, assign, true, false]


#InputFile Class
class InputFile:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.data = []
        self.position = 0
        self.size = 0
        self.lineNumber = 1
        self.columnNumber = 1
        aux = self.file.read()
        self.lines = 0
        for ch in aux:
            self.size += 1
            if ch == "\n":
                self.lines += 1
            self.data.append(ch)


    def getChar(self):
        self.position += 1
        c = self.data[self.position ]
        if c == "\n":
            self.columnNumber = 1
            self.lineNumber += 1
        else:
            self.columnNumber += 1
        return c

    def peekChar(self):
        return self.data[self.position]


    def isE0F(self):
        if self.lineNumber == self.lines:
            return True
        else:
            return False

class Lexer:
    def __init__(self, filename):
        self.file = InputFile(filename)
        self.words = {}
        addToDic(words_list, self.words)
        reserve(Word("program", Tag.PROGRAM), self.words)
        reserve(Word("constant", Tag.CONSTANT), self.words)
        reserve(Word("var", Tag.VAR), self.words)
        reserve(Word("begin", Tag.BEGIN), self.words)
        reserve(Word("end", Tag.END), self.words)
        reserve(Word("integer", Tag.INTEGER), self.words)
        reserve(Word("real", Tag.REAL), self.words)
        reserve(Word("string", Tag.STRING), self.words)
        reserve(Word("readln", Tag.READLN), self.words)
        reserve(Word("while", Tag.WHILE), self.words)
        reserve(Word("do", Tag.DO), self.words)
        reserve(Word("repeat", Tag.REPEAT), self.words)
        reserve(Word("until", Tag.UNTIL), self.words)
        reserve(Word("for", Tag.FOR), self.words)
        reserve(Word("to", Tag.TO), self.words)
        reserve(Word("downto", Tag.DOWNTO), self.words)
        reserve(Word("if", Tag.IF), self.words)
        reserve(Word("then", Tag.THEN), self.words)
        reserve(Word("else", Tag.ELSE), self.words)
        reserve(Word("not", Tag.NOT), self.words)
        reserve(Word("div", Tag.DIV), self.words)
        reserve(Word("mod", Tag.MOD), self.words)
        reserve(Word("and", Tag.AND), self.words)
        reserve(Word("or", Tag.OR), self.words)
        self.peek = ""
        pass


    #Basic validation of whether something is reserved or not(in dictionary or not)
    def isReserved (self, key):
        if key in self.words:
            return True
        return False

    #Reserve function (add stuff to dictionary)
    def reserve2(self,key):
        if key in self.words:return self.words[key]


    def readch(self):
        self.peek = self.file.getChar()

    def readch2(self, c):
        self.readch()
        if self.peek != c:
            self.file.position += 1 #Si no vuelves a leer el mismo segundo caracter otra vez
            return False
        self.file.position += 1
        return True

    #Delete blank spaces
    def skipWhiteSpaces(self):
        self.peek = self.file.peekChar()
        while self.peek.isspace():
            self.peek = self.file.getChar()


    def readCharacterString(self):
        cs = "" + self.peek
        self.peek = self.file.getChar()
        while self.peek != '"' :
            cs += self.peek
            self.peek = self.file.getChar()
        cs += self.peek
        self.readch()
        return CharacterString(cs)

    #Check the comments
    def readComments(self):
        prev = self.file.position
        current = self.file.position + 1
        while current < self.file.size and self.file.data[prev] != "*" and self.file.data[current] != ")":
            prev = current
            current += 1
        self.file.position = current + 1
        return Token(Tag.COMMENTS)

    #Main function that calls everything
    def scan(self):
        #Cancel all spaces to do the analysis correctly
        self.skipWhiteSpaces()
        #Lots of if's to check if the character is a reserved symbol one or not
        if self.peek == "(":
            if self.readch2("*"):
                self.readch()
                return readComments()
            else:
                return Token("(")

        elif self.peek == "<":
            if self.readch2("="):
                return self.reserve2("<=")
            elif self.peek == ">":
                return self.reserve2("<>")
            else:
                return Token("<")

        elif self.peek == ">":
            if self.readch2("="):
                return self.reserve2(">=")
            else:
                return Token(">")

        elif self.peek == "=":
            if self.readch2("="):
                return self.reserve2("==")
            else:
                return Token("=")

        elif self.peek == ":":
            if self.readch2("="):
                return self.reserve2(":=")
            else:
                return Token(":")

        elif self.peek == '"':
                return self.readCharacterString()



        #Check if characters is a Digit
        #For Integers
        if self.peek.isdigit():
            v = self.peek
            self.readch()
            while self.peek.isdigit():
                v += self.peek
                self.readch()
            if self.peek != ".":
                #cast to Int
                vAux = int(v)
                return Integer (vAux)
            #For Real Numbers
            x = v
            x += self.peek
            while True:
                self.readch()
                if not self.peek.isdigit():
                    break
                x += self.peek
            #Cast to float
            xAux = float(x)
            return Real(xAux)

        #Check if character is a Letter
        if self.peek.isalpha():
            b = self.peek
            self.readch()


        #Ending
        tok = Token(self.peek)
        self.readch();
        return tok;



def addToDic(dictionary, words):
    for i in dictionary:
        reserve(i, words)
    pass
def reserve(w, words):
    words[w.lexeme] = w
