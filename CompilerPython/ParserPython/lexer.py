# Valter Nunez
# A01206138
# Lexer 2.0

class Tag:

        EOF = 65535
        NUMBER = 290
        ID = 291
        ERROR = 292

class Token:
    def __init__(self, tag = 0):
        self.tag = tag

    def __str__(self):
        if self.tag == Tag.EOF:
            return "TOKEN, symbol = EOF"
        else:
            return "TOKEN, symbol = " + chr(self.Tag)

class Word:
    def __init__(self, lexeme, tag):
        self.tag = tag
        self.lexeme = lexeme

    def __str__(self):
        return "WORD, lexeme = " + self.lexeme

class Number (Token):

    def __init__(self, value):
        self.tag = Tag.NUMBER
        self.value = value

    def __str__(self):
        return "NUMBER, value = " + str(self.value)

class Lexer:
    def __init__(self, filename):
        self.input = open(filename, "r")
        self.reading = True
        self. lastr = True
        self.peek = ''
        self.words = {}
        self.lineNumber = 1

    def readCh(self):
        self.peek = self.input.read(1)
        if self.peek:
            return self.peek
        self.reading = False
        return self.peek

    def skipWhiteSpaces(self):
        while self.peek == "" or self.peek ==   "\t" or self.peek == "\n":
            if self.peek == "\n":
                self.lineNumber = self.lineNumber + 1
            self.readCh()

    #ESTO QUE
    def scan2(self):
        mytoken = self.scan()
        print(mytoken)
        return mytoken


    def scan(self):
        self.skipWhiteSpaces()

        if self.peek.isdigit():
            st = ""+self.peek
            self.readch()
            while self.reading and (self.peek.isdigit() or self.peek == '.'):
                st = st + self.peek
                self.readch()
            return Number(float(st))

        elif self.peek.isalpha():
            st = ""+self.peek
            self.readch()
            while self.reading and (self.peek.isalpha() or self.peek.isdigit()):
                st = st + self.peek
                self.readch()
            st = st.lower()
            if st in self.words:
                return self.words[st]#Word(st, Tag.ID)
            w = Word(st, Tag.ID)
            self.words[st] = w
            return w

        else:
            if self.peek == '':
                return Token(65535) #End of File
            tok = Token(ord(self.peek))
            self.readch()
            return tok
