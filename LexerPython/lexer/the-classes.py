#Valter Nunez - A01206138
# lexer


#CharacterString class
class CharacterString(Token):
    def __init__(self, value):
        super().__init__(Tag.CHARACTERSTRING)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "STRING - VALUE" + str(self.value)

#Integer Class
class Integer(Token):
    def __init__(self, value):
        super().__init___(Tag.INTEGER)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "INTEGER - VALUE" + str(self.value)
#Real class
class Real(Token):
    def __init__(self, value):
        super().__init__(Tag.REAL)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "REAL - VALUE" + str(self.value)

#Tag Class
class Tag:
    EOF = 66666
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

#Token Class
class Token:
    def __init__(self, tag):
        this.tag = tag
    #Getter
    def getToken(self):
        return self.tag

    def toString():
        return "TOKEN - VALUE = " + str(self.tag)

#Word Class
class Word(Token):
    def __init__(self, lexeme, tag):
        self.tag = tag
        self.lexeme = lexeme
    def __str__(self):
        return str(lexeme)

    eq = Word("==", Tag.EQ)
    ne = Word( "<>", Tag.NEQ )
	le= Word( "<=", Tag.LE  )
    ge = Word( ">=", Tag.GE )
	minus = Word( "minus", Tag.MINUS )
	assign = Word( ":=", Tag.ASSIGN )
	true = Word( "true",  Tag.TRUE  )
	false = Word( "false", Tag.FALSE )

    words_list[eq, ne, le, ge, minus, assign, true, false]


#InputFile Class
class InputFile:
    def __init__ InputFile(self, filename):
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
        c = self.data[self.position]
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




#Lexer Class
class Lexer:
    def __init__(self):
        self.words = {}
        addToDic(prewords, self.words)
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
        self.file = InputFile(filename)
        self.peek = ""
        pass

    def addToDic(dictionary, words):
        for i in dictionary:
            reserve(i, words)
        pass

    def reserve(w, words):
        words[w.lexeme] = w

    def isReserved (self, key):
        if key in self.word:
            pass

    def readch(self):
        self.peek = self.file.getChar()

    def readch(c):
        readch()
        if self.peek != c:
            return False
        return True

    def skipWhiteSpaces():
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
        readch()
        return CharacterString(cs)

    def readComments(self):
        prev = self.file.position
        current = self.file.position + 1
        while current < self.file.size and self.file.data[prev] != "*" and self.file.data[current] != ")":
            prev = current
            current += 1
        self.file.position = current + 1
        return Token(Tag.COMMENTS)


    def scan():
        skipWhiteSpaces()

        if self.peek == "(":
            if readch("*"):
                readch()
                return readComments()
            else
                return Token("(")

        elif self.peek == "<":
            if self.readch("="):
                return self.isReserved("<=")
            elif self.peek == ">":
                return self.isReserved("<>")
            else:
                return Token("<")

        elif self.peek == ">":
            if self.readch("="):
                return self.isReserved(">=")
            else:
                return Token(">")

        elif self.peek == "=":
            if self.readch("="):
                return self.isReserved("==")
            else:
                return Token("=")

        elif self.peek == ":":
            if self.readch("="):
                return self.isReserved(":=")
            else:
                return Token(":")

        elif self.peek == '"':
                return self.readCharacterString()


        if self.peek.isdigit():
            v = ""
            v += str(self.peek)
            self.readch()
            while self.peek.isdigit():
                v += str(self.peek)
                self.readCh()
            if self.peek != ".":
                return Integer(int(v))

            v += str(self.peek)
            while True:
                self.readch()
                if self.peek.isdigit() == False:
                    break
                v += str(self.peek)
            return Real(float(v))
