#Valter Nunez
#A01206138
#Parser Proyecto - Lexer

#Imports
import sys
#Token Class
class Token:
    def __init__(self, tag):
        self.tag = tag
    #Getter
    def getToken(self):
        return self.tag

    #Modificacion de strings para que jale con el parser.
    def toString(self):
        if self.tag == Tag.PROGRAM:
            return "program"
        elif self.tag == Tag.CONSTANT:
            return "constant"
        elif self.tag == Tag.VAR:
            return "var"
        elif self.tag == Tag.BEGIN:
            return "begin"
        elif self.tag == Tag.END:
            return "end"
        elif self.tag == Tag.INTEGER:
            return "integer"
        elif self.tag == Tag.REAL:
            return "number"
        elif self.tag == Tag.BOOLEAN:
            return "boolean"
        elif self.tag == Tag.STRING:
            return "string"
        elif self.tag == Tag.WRITELN:
            return "writeln"
        elif self.tag == Tag.READLN:
            return "readln"
        elif self.tag == Tag.WHILE:
            return "while"
        elif self.tag == Tag.DO:
            return "do"
        elif self.tag == Tag.REPEAT:
            return "repeat"
        elif self.tag == Tag.UNTIL:
            return "until"
        elif self.tag == Tag.FOR:
            return "for"
        elif self.tag == Tag.TO:
            return "to"
        elif self.tag == Tag.DOWNTO:
            return "downto"
        elif self.tag == Tag.IF:
            return "if"
        elif self.tag == Tag.THEN:
            return "then"
        elif self.tag == Tag.ELSE:
            return "else"
        elif self.tag == Tag.NOT:
            return "not"
        elif self.tag == Tag.DIV:
            return "DIV"
        elif self.tag == Tag.MOD:
            return "mod"
        elif self.tag == Tag.AND:
            return "and";
        elif self.tag == Tag.OR:
            return "or"
        elif self.tag == Tag.EQ:
            return "="
        elif self.tag == Tag.NEQ:
            return "<>"
        elif self.tag == Tag.LE:
            return "<="
        elif self.tag == Tag.GE:
            return ">="
        elif self.tag == Tag.MINUS:
            return "-"
        elif self.tag == Tag.ASSIGN:
            return ":="
        elif self.tag == Tag.ID:
            return "identifier"
        elif self.tag == Tag.EOF:
            return "$"
        elif self.tag == Tag.CHARACTERSTRING:
            return "string"
        elif self.tag == Tag.COMMENTS:
            return "TOKEN - VALUE = COMMENTS"
        else:
            return str(self.tag)

#CharacterString class
class CharacterString(Token):
    def __init__(self, value):
        super().__init__(Tag.CHARACTERSTRING)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def __str__(self):
        return "STRING - VALUE = " + str(self.value)

#Integer Class
class Integer(Token):
    def __init__(self, value):
        super().__init__(Tag.INTEGER)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def __str__(self):
        return "INTEGER - VALUE = " + str(self.value)
#Real class
class Real(Token):
    def __init__(self, value):
        super().__init__(Tag.REAL)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def __str__(self):
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

    def __str__(self):
        return "WORD - LEXEME = " + self.lexeme

eq = Word("==", Tag.EQ)
ne = Word("<>", Tag.NEQ)
le = Word("<=", Tag.LE)
ge = Word(">=", Tag.GE)
minus = Word("minus", Tag.MINUS)
assign = Word(":=", Tag.ASSIGN)
true = Word("true", Tag.TRUE)
false = Word("false", Tag.FALSE)

#InputFile Class
class InputFile:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.data = []
        self.position = 0
        self.size = 0
        self.columnNumber = 1
        self.lineNumber = 1
        aux = self.file.read()
        self.lines = 0
        for x in aux:
            self.size += 1
            if x == "\n":
                self.lines += 1
            self.data.append(x)


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
        if self.isEOF():
            sys.exit()
        return self.data[self.position]

    def isEOF(self):
        if self.lineNumber == self.lines + 1:
            return True
        else:
            return False

    def isEOL(self):
        return isEOF() or peekChar() == "\n"


class Lexer:
    def __init__(self, filename):
        self.lineNumber = 0
        self.input = open(filename, "r")
        self.words = {}
        self.peek = ""
        self.active = True

    def reserve(self, key):
        self.words[key.lexeme] = key

    #Basic validation of whether something is reserved or not(in dictionary or not)
    def isReserved (self, key):
        if key in self.words:
            return True
        return False

    def readch(self):
        self.peek = self.input.read(1)
        if self.peek:
            if self.peek =="'":
                self.peek = '"'
            return self.peek
        self.active = False
        return self.peek

        def readch2(self, c):
            self.readch()
            if self.peek != c:
                self.file.position += 1 #Si no vuelves a leer el mismo segundo caracter otra vez
                return False
            self.file.position += 1
            return True

    def reserveWords(self):
        self.reserve(Word("program", Tag.PROGRAM))
        self.reserve(Word("constant", Tag.CONSTANT) )
        self.reserve(Word("var", Tag.VAR) )
        self.reserve(Word("begin", Tag.BEGIN) )
        self.reserve(Word("end", Tag.END) )
        self.reserve(Word("integer", Tag.INTEGER) )
        self.reserve(Word("real", Tag.REAL) )
        self.reserve(Word("boolean", Tag.BOOLEAN) )
        self.reserve(Word("string", Tag.STRING) )
        self.reserve(Word("writeln", Tag.WRITELN) )
        self.reserve(Word("readln", Tag.READLN) )
        self.reserve(Word("while", Tag.WHILE) )
        self.reserve(Word("do", Tag.DO) )
        self.reserve(Word("repeat", Tag.REPEAT) )
        self.reserve(Word("until", Tag.UNTIL) )
        self.reserve(Word("for", Tag.FOR) )
        self.reserve(Word("to", Tag.TO) )
        self.reserve(Word("downto", Tag.DOWNTO) )
        self.reserve(Word("if", Tag.IF) )
        self.reserve(Word("then", Tag.THEN) )
        self.reserve(Word("else", Tag.ELSE) )
        self.reserve(Word("not", Tag.NOT) )
        self.reserve(Word("div", Tag.DIV) )
        self.reserve(Word("mod", Tag.MOD) )
        self.reserve(Word("and", Tag.AND) )
        self.reserve(Word("or", Tag.OR) )

    #Reserve function (add stuff to dictionary)
    #def reserve(self,key):
        #if key in self.words:return self.words[key]
    #Delete blank spaces
    def skipWhiteSpaces(self):
        while self.peek == " " or self.peek == "\t" or self.peek == "\n":
            if self.peek == "\n":
                self.lineNumber = self.lineNumber + 1
            self.readch()

    #Detect and read my beloved strings
    def readCharacterString(self):
        cs = "" + self.peek
        self.readch()
        while self.peek != '"' :
            cs += self.peek
            self.readch()
        cs += self.peek
        self.readch()
        return CharacterString(cs)

    #Check the comments
    def readComments(self):
        prev = self.peek
        self.readch()
        while self.active:
            if prev == '*' and self.peek == ')':
                self.readch()
                break
            prev = self.peek
            self.readch()
        return Token(Tag.COMMENTS);

    #Main function that calls everything
    def scan(self):
        #Cancel all spaces to do the analysis correctly
        self.skipWhiteSpaces()
        #Lots of if's to check if the character is a reserved symbol one or not
        if self.peek == '(':
            self.readch()
            if self.peek =='*':
                return self.readComments()
            return Token('(')

        elif self.peek == '<':
            self.readch()
            if self.peek == '=':
                self.readch()
                return le
            elif self.peek == '>':
                self.readch()
                return ne
            else:
                return Token('<')

        elif self.peek == '>':
            self.readch()
            if self.peek == '=':
                self.readch()
                return le
            elif self.peek == '>':
                self.readch()
                return ne
            else:
                return Token('<')

        elif self.peek == '=':
            self.readch()
            if self.peek == '=':
                self.readch()
                return eq
            else:
                return Token('=')

        elif self.peek == ':':
            self.readch()
            if self.peek == '=':
                self.readch()
                return assign
            else:
                return Token(':')

        elif self.peek == '"':
            return self.readCharacterString()

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

        if self.peek.isalpha():
            b = self.peek
            self.readch()
            while self.peek.isalpha() or self.peek.isdigit():
                b +=  self.peek
                self.readch()
            b = b.lower()
            if b in self.words:
                return self.words[b]#Word(st, Tag.ID)
            w = Word(b, Tag.ID)
            self.reserve(w)
            return w

        tok = Token(self.peek)
        self.readch()
        return tok
