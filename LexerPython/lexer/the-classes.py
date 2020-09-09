


class CharacterString(Token):
    def __init__(self, value):
        self.tag = Tag.CHARACTERSTRING
        self.value = value
    def __str__(self):
        return str(value)

class Integer(Token):
    def __init__(self, value):
        self.tag = Tag.INTEGER
        self.value = value
    def __str__(self):
        return str(value)

class Real(Token):
    def __init__(self, value):
        self.tag = Tag.REAL
        self.value = value
    def __str__(self):
        return str(value)

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
