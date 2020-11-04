import sys
import lexer

class Parser:
    "Class to check gramar of the input and returns accepted or not"
    def _init_(self, filename):
        self.lexer = lexer.Lexer(filename)
        self.pila = []
        sel.pilaEstados = 0
        self.inputstring = []
        self.tabla = {}
        self.fillAction("table2.csv")
        self.fillInputString()

    def fillAction(self, table):
        arr = []
        file = open(table, 'r')
        Lines = file.readlines()
        mystate = 1
        keys = []
        vals = []
        for line in Lines:
            line = line.strip()
            line = str(line)
            if mystate == 1:
                keys = line.split(",")
                mystate = 2
            elif mystate == 2:
                x = line.split(",")
                for value in x:
                    vals.append([value])
                mystate = 3
            elif mystate == 3:
                x = line.split(",")
                for i in range(len(x)):
                    vals[i].append(x[i])
        for i in range(len(keys)):
            self.tabla[keys[i]] = vals[i]

    def fillInputString(self):
        self.lexer.start()
        self.lexer.readch()
        token = self.lexer.scan()
        self.inputstring.append(token)
        while self.lexer.reading:
            print("" + str(token))
            token = self.lexer.scan()
            self.inputstring.append(token)
        self.lexer.input.close()



    def analyze(self):
        state = self.pilaEstados.top()
        entrada = self.inputstring[0]
        action = self.tabla[entrada] [state]
        if action[0] == 'S':
            action.replace('S', '')
            action = int(action)
            self.pilaEstados.append(action)
            self.pila.append(entrada)
            self.inputstring.pop(0)
        elif action[0] == 'R':
            action.replace('R', '')
            action = int(action)
            file = open('grammar.txt', 'r')
            lines = file.readLines()
            file.close()
            count = 0
            reduce = ''





if len(sys.argv) != 2:
    print("usage: parser.py inputfile")
else:
    parser = Parser(sys.argv[1])
    print(parser.tabla)
    print(parser.inputstring)
