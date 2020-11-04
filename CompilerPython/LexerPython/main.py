from lexer import *
import sys

if len(sys.argv) != 2:
    print("usage: main.py file")
else:
    lex = Lexer(sys.argv[1])

    with open(sys.argv[1]) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(lex.scan().toString())
