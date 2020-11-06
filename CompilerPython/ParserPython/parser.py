#Valter Nunez
#A01206138
#Parser Proyecto
#Proyecto realizado en conjunto con Martin Vivanco
#Referencia de parseo - https://www.youtube.com/watch?v=1_qjmZXFaNw&feature=youtu.be

#Imports
import sys
import lexer

#Class del Parser como tal
class Parser:
    #Constructor
    def __init__(self, filename):
        self.lexer = lexer.Lexer(filename) #Obtener lexer de su archivo
        self.stack = [] #declaracion del stack
        self.stackstates = [0]  #Se guardan los e
        self.inputstring = [] #Columna de Input
        self.table = {} #Tabla final
        self.linecounter = []
        self.actionTable("table.csv") #Uso de table desde archivo de comas para llenar la tabla de Action
        self.isTable() #Llenado de la tabla input string

    #Llenado de la table Action.
    #state 1 -> Para llenar las llaves
    #state 2 -> Crear arrelgos donde vas a meter los valores
    #state 3 -> Meter los valores ahora si en los arreglos creadoes en el 2
    def actionTable(self, table):
        file = open(table, "r")
        row = file.readlines() #Leectura por linea del archivo. Por row pues
        state = 1 #Inicializacion para los states
        keys = [] #Arreglo de llaves
        vals = [] #Arreglo de valores
        for line in row: #Lectura row por row
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
            if keys[i] == "coma": #como tenemos un archivo de comas, la , como tal se pierde en la tabla. Por lo tanto, se cambio ese simbolo por la palabra coma en el .csv  Ahora lo regresamos.
                keys[i] = ","
            self.table[keys[i]] = vals[i]
        file.close() #Cerrar archivo

    #Generar la columna Input String
    def isTable(self):
        self.lexer.reserveWords() #Reservar palabras en el lexer
        self.lexer.readch() #empezar lectura
        aux = '' #inizialicacion cadena
        token = self.lexer.scan() #Correr como tal el lexer y guardar el valor del tag que te deveuelve en token.
        while self.lexer.active: #Mientras siga leyendo el lexer
            if token.toString() != "TOKEN - VALUE = COMMENTS": #Si es algo valido (o sea no un comentario pues)
                self.inputstring.append(token.toString()) #Agregar el valor del tag dado por Token.toString() en lexer.
                aux += token.toString() + ' '
                self.linecounter.append(self.lexer.lineNumber) #Ir manejando el counter de la linea
            token = self.lexer.scan()
        if token.toString() != '': #Manejo de epsilon
            self.inputstring.append(token.toString())
        self.inputstring.append('$') #agregar el EOF
        self.lexer.input.close() #cerrar

    #Funcion que se llama cuando hay algun error
    def errorHandler(self):
        print("ERROR! LINE " + str(self.linecounter[-len(self.inputstring)]) + " HAS AN ISSUE THAT DOES NOT ALLOW COMPILATION.")#Se muestra la linea donde se esta dando el error
        sys.exit() #Matar el programa.

    #Funcion principal para hacer el parseo
    def analyze(self):
        neverDieGang = 0 #Contador de loop para ir analizando.
        while neverDieGang < 2500: #Despues de esta cantidad de pasos, ya no analizas.
            neverDieGang += 1 #Un ++, basicamente.
            state = self.stackstates[-1] #El primer state es el del tope de la stack
            entrada = self.inputstring[0] #El primer valor dentro del Input String se va a revisar
            action = self.table[entrada][state]
            if action == '': #Si nos encontramos con un action vacio, esta mal algo (tiene que haber o shift o reduce)
                self.errorHandler() #mandas el error como tal
            elif action == 'acc': #Si alcanzamos el estado de aceptacion, todo bien.
                print("accepted") #Mandar el accepted
                sys.exit() #Matar programa.
            if action[0] == 's': #Todos los Shifts empiezan con S, entonces solo necesitamos saber que es S para que sepamos que es un shift.
                action = action.replace('s', '') #Borras la S para que solo quede el numero del state a revisar (nada de string pues)
                action = int(action) #Convertir los valores numericos a numeros como tal (ints)
                self.stackstates.append(action) #Appendear el numero del state a la stack de states.
                self.stack.append(entrada) #Appendear el valor del input sting
                self.inputstring.pop(0) #Sacar el valor del input string
            elif action[0] == 'r': #Todos los Reduce empiezan con R, entonces solo neceistamos aber que es una R para saber que es un reduce.
                action = action.replace('r', '') #Borras la R para que solo quede el numero del state a revisar (nada de string pues)
                action = int(action) #Convertir los valores numericos a numeros como tal (ints)
                file = open('grammar.txt', 'r') #Leer la gramatica para saber que state es el que vamos a revisar para la sustitucion.
                lines = file.readlines() #Lectura por Lineas (rows)
                file.close() #Cerrar archivo
                count = 0 #Inizializar contador
                reduce = '' #Inicializar reduce
                for line in lines: #Leer cada row
                    if count == action: #Revisar que estas en la linea correcta, dada por el reduce.
                        reduce = line
                    count = count + 1 #Avanzas, linea por linea, hasta llegar a la linea de la gramtica correcta.
                reduce  = reduce.strip() #Eliminar los espacios al inicio y final del string.
                reduce = reduce.split(' ') #Separar por espacios
                if reduce [-1] == "''": #Checar si hay un Epsilon.    Epsilon es ''
                    reduce.pop()  #Como Epsilon no vale nada, solo haces el pop.
                while reduce[-1] != '->': #Buscamos en la gramatica el igual para hacer la sustitucion
                    self.stackstates.pop() #Sacas del stack de los estados el de hasta arriba.
                    if reduce.pop() != self.stack.pop(): #Si no es igual el pop del reduce y el del stack, hay un problema.
                        self.errorHandler() #mandar el error como tal. 
                reduce.pop() #Sacas el valor de hasta arriba del reduce
                self.stack.append(reduce.pop()) #de lo que sacas del reduce, lo appenead al stack.
                self.stackstates.append(int(self.table[self.stack[-1]][self.stackstates[-1]])) #A los estados tambien haces append del valor final del stack y stack states.
        print("ERROR: SE PASA DE LA CANTIDAD PERMITIDA DE CICLOS A ANALIZAR") #Por si nos toca un grammar medio locochon

#Con que correr el programa.
if len(sys.argv) != 2: #Revisar que se obtengan, si o si, 2 argumentos para correr el programa.
    print("usage: parser.py inputfile") #Usage
else: #Si si te dan dos argumentos, vas a correr el parser.
    parser = Parser(sys.argv[1]) #Mandas a parser el segundo argumento
    parser.analyze()
