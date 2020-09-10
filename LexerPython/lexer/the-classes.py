

#CharacterString class
class CharacterString(Token):
    def __init__(self, value):
        super().__init__(Tag.CHARACTERSTRING)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "STRING - VALUE" + str(value)

#Integer Class
class Integer(Token):
    def __init__(self, value):
        super().__init___(Tag.INTEGER)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "INTEGER - VALUE" + str(value)
#Real class
class Real(Token):
    def __init__(self, value):
        super().__init__(Tag.REAL)
        self.value = value
    #Getter
    def getValue(self):
        return self.value

    def toString(self):
        return "REAL - VALUE" + str(value)

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
    ERROR = 293;

#Token Class
class Token:
    def __init__(self, tag):
        this.tag = tag
    def __str__(self):
        return str(tag)
    def paString():  #QUE SWITCHEE EL tag
        switcher = {
            Tag.PROGRAM:"PROGRAM",
            Tag.CONSTANT: "CONSTANT",
            Tag.VAR: "VAR",
            Tag.BEGIN: "BEGIN",
            Tag.END: "END",
            Tag.INTEGER: "INTEGER",
            Tag.REAL: "REAL",
            Tag.BOOLEAN: "BOOLEAN",
            Tag.STRING: "STRING",
            Tag.WRITELN: "WRITELN",
            Tag.READLN: "READLN",
            Tag.WHILE: "WHILE",
            Tag.DO: "DO",
            Tag.REPEAT: "REPEAT",
            Tag.UNTIL: "UNTIL",
            Tag.FOR: "FOR",
            Tag.TO: "TO",
            Tag.DOWNTO: "DOWNTO",
            Tag.IF: "IF",
            Tag.THEN: "THEN",
            Tag.ELSE: "ELSE",
            Tag.NOT: "NOT",
            Tag.DIV: "DIV",
            Tag.MOD: "MOD",
            Tag.AND: "AND",
            Tag.OR: "OR",
            Tag.EQ: "EQ",
            Tag.NEQ: "NEQ",
            Tag.LE: "LE",
            Tag.GE: "GE",
            Tag.MINUS: "MINUS",
            Tag.ASSIGN: "ASSIGN",
            Tag.ID: "ID",
            Tag.EOF: "EOF",
        }
        return switcher.get(tag, "" + tag)

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
        we = 1

#Lexer Class
class Lexer:
    words = {}
    peek = ""
    def __init__(self):
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
        file = open(filename, "r")

    def reserve(w):
        words[w.lexeme] = w

    def skip_spaces(peek):


    def scan():
        input.replace(" ", "")
