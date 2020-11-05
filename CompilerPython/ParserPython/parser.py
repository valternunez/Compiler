#Valter Nunez
#A01206138
#Parser Proyecto
#Proyecto realizado en conjunto con Martin Vivanco

#Imports
import sys
import lexer

#Class del Parser como tal
class Parser:

    #Constructor
    def _init_(self, filename):
        self.lexer = lexer.Lexer(filename) #Obtener lexer de su archivo
        self.stack = []
        sel.stackstates = 0  #Se guardan los e
        self.inputstring = [] #Columna de Input
        self.table = {} #Tabla final
        self.fillAction("table2.csv") #Uso de table desde archivo de comas
        self.fillInputString()

    #Llenado de la table Action.
    #state 1 -> Para llenar las lalves
    #state 2 -> Crear arrelgos donde vas a meter los valores
    #state 3 -> Meter los valores ahora si en los arreglos creadoes en el 2
    def fillAction(self, table):
        arr = [] #Inicializacion
        file = open(table, 'r') #abrir archivo para lectura
        Lines = file.readlines() #Leectura por linea del archivo. Por row pues
        state = 1 #Inicializacion para los states
        keys = [] #Arreglo de llaves
        vals = [] #Arreglo de valores
        for line in Lines: #Lectura row por row
            line = line.strip() #Remover espacios al inicio y final del string
            line = str(line) #Convertir valor a string
            if state == 1: #Revisar si el state es 1.
                keys = line.split(",") #Separar los strings por cada coma encontrada (Estamos usando el csv que es por comas)
                state = 2 #Cambiar ahora a state 2
            elif state == 2: #Ahora revisa state dos.
                x = line.split(",") #Separar los string por comas
                for value in x:
                    vals.append([value])
                state = 3 #Cambiar ahora a state 3
            elif state == 3: #Ahora revisa state tres.
                x = line.split(",") #Separar los strings por comas
                for i in range(len(x)):
                    vals[i].append(x[i])
        for i in range(len(keys)):
            self.table[keys[i]] = vals[i]
        file.close() #Cerrar archivo

    #Generar la columna Input String
    def fillInputString(self):
        self.lexer.start() #Correr el lexer
        self.lexer.readCh() #Read first Char
        token = self.lexer.scan()
        self.inputstring.append(token)
        while self.lexer.reading:
            print("" + str(token))
            token = self.lexer.scan()
            self.inputstring.append(token)
        self.lexer.input.close() #Cerrar el Lexer


    #Funcion principal para hacer el parseo
    def analyze(self):
        state = self.stackstates.top() #El primer state es el del tope de la stack
        entrada = self.inputstring[0] #El primer valor dentro del Input String se va a revisar
        action = self.table[entrada] [state]
        if action[0] == 'S': #Todos los Shifts empiezan con S, entonces solo necesitamos saber que es S para que sepamos que es un shift.
            action.replace('S', '') #Borras la S para que solo quede el numero del state a revisar (nada de string pues)
            action = int(action) #Convertir los valores numericos a numeros como tal (ints)
            self.stackstates.append(action) #Appendear el numero del state a la stack de states.
            self.stack.append(entrada) #Appendear el valor del input sting
            self.inputstring.pop(0) #Sacar el valor del input string
        elif action[0] == 'R': #Todos los Reduce empiezan con R, entonces solo neceistamos aber que es una R para saber que es un reduce.
            action.replace('R', '') #Borras la R para que solo quede el numero del state a revisar (nada de string pues)
            action = int(action) #Convertir los valores numericos a numeros como tal (ints)
            file = open('grammar.txt', 'r') #Leer la gramatica para saber que state es el que vamos a revisar para la sustitucion.
            lines = file.readLines() #Lectura por Lineas (rows)
            file.close() #Cerrar archivo
            count = 0 #Inizializar contador
            reduce = '' #Inicializar reduce
            for line in lines: #Leer cada row
                if count == action: #Revisar que estas en la linea correcta, dada por el reduce.
                    reduce = line
                    print(line)
                count = count + 1 #Avanzas, linea por linea, hasta llegar a la linea de la gramtica correcta.
            reduce  = reduce.strip() #Eliminar los espacios al inicio y final del string.
            reduce = reduce.split(' ') #Separar por espacios
            print (reduce) #Imprimir el valor
            while reduce[-1] != '->': #Buscamos en la gramatica el igual para hacer la sustitucion
                self.stackstates.pop() #Sacas del stack de los estados el de hasta arriba.
                if reduce.pop() != self.stack.pop(): #Si no es igual el pop del reduce y el del stack, hay un problema.
                    print("ERROR") #Mandar error
                    sys.exit() #Matas el programa
            reduce.pop() #Sacas el valor de hasta arriba del reduce
            self.stack.append(reduce.pop()) #de lo que sacas del reduce, lo appenead al stack.
            self.stackstates.append(int(self.table[self.stack[-1]][self.stackstates[-1]])) #A los estados tambien haces append del valor final del stack y stack states.


if len(sys.argv) != 2: #Revisar que se obtengan, si o si, 2 argumentos para correr el programa.
    print("usage: parser.py inputfile") #Usage
else: #Si si te dan dos argumentos, vas a correr el parser.
    parser = Parser(sys.argv[1]) #Mandas a parser el segundo argumento
    print(parser.table) #Imprimes la tabla
    print(parser.inputstring) #Imprimes el input string.
