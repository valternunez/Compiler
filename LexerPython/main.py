from lexer import *
import sys

if len(sys.argv) != 2:
    print("usage: main.py file")
else:
    lex = Lexer(sys.argv[1])
    with open(sys.argv[1]) as openfileobject:
        for line in openfileobject:
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
            print(lex.scan().toString())
