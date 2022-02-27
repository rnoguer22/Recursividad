# Recursividad
Pincha [aquí] para acceder al link del repositorio de Github

## Dicotonomia
```Python3
def dicotonomia_recursiva (tabla, t):
    i = 0
    j = len(tabla)
    if i > j:
        return "Ausente"
    else:
        m = int((i+j)/2)
        if tabla[m] == t:
            return m
        else:
            if tabla[m] < int(t):
            #Esto implica que tabla[m+1] ≤ t ≤ tabla[j] 
            #Recursividad
                print (dicotonomia_recursiva(tabla, t))
                return dicotonomia_recursiva (tabla[m+1:j], t)
            else:
            #Esto implica que tabla[i] ≤ t ≤ tabla[m–1] 
            #Recursividad
                print (dicotonomia_recursiva(tabla, t))
                return dicotonomia_recursiva (tabla[i:m-1], t)

def dicotonomia (tabla, t):
    return dicotonomia_recursiva (tabla, t)

if __name__ == "__main__":
    #Entrada
    tabla = [4,2,6,3,8,7,5,9,1,0]
    t = input("Introduzca el dato a buscar: ")
    
    #Ordenamos tabla
    tabla.sort()

    print ("{} se encuentra en la celda {}".format(t, dicotonomia(tabla,t)))
```

## Palindromos
```Python3
#Funcion para pasar la frase a mayusculas y eliminar las tildes
def mayusculas_tildes(frase):
    #Hace la conversion si la frase es de tipo string
    if str(frase):
        frase = frase.upper()
        frase = frase.replace(" ", "")
        frase = frase.replace("Á", "A")
        frase = frase.replace("É", "E")
        frase = frase.replace("Í", "I")
        frase = frase.replace("Ó", "O")
        frase = frase.replace("Ú", "U")
    #Si no, no se puede hacer la conversion
    else:
        pass
    return frase

#Esta funcion devuelve un booleano que nos dice si es palindromo o no
def es_palindromo(frase):
    frase = mayusculas_tildes(frase)
    #Llegamos a que no nos quedan mas elementos, por lo tanto sera un palindromo
    if len(frase) == 0:
        return "Palindromo!"
    else:
        #Si el primer caracter coincide con el ultimo
        if frase[0] == frase[-1]:
            #Utilizamos recursividad
            return es_palindromo(frase[1:-1])
        else:
            #Si en algun momento no coincide el primero con el ultimo, no es palindromo :(
            return "No es palindromo :("

if __name__ == '__main__':

    oracion = input("Introduzca una frase molona o un numero: ")
    print (es_palindromo(oracion))
```

## Bandera Dijkstra
```Python3
class Bandera:
    #Definimos el constructor
    def __init__(self, bandera, r, g, b):
        self.bandera = bandera
        self.r = r
        self.g = g
        self.b = b
    
    def ordenar_(self, n):
        #Añadimos un contador que nos ayudara a recorrer "bandera"
        if len(self.bandera) == n:
            #Concatenamos las diferentes listas en una sola lista
            resultado = self.r + self.g + self.b
            #Mostramos por pantalla el numero de fichas de cada color
            print("Hay {} elementos rojos".format(len(self.r)))
            print("Hay {} elementos verdes".format(len(self.g)))
            print("Hay {} elementos azules".format(len(self.b)))
            return print ("La bandera ordenada quedaria asi: {}".format(resultado))
        else:
            if self.bandera[n] == "R":
                self.r.append("R")
                #Aumentamos el contador en 1 para aplicar recursividad y recorrer todas las fichas una sola vez
                n += 1
                #Aplicamos recursividad para ver los demas elementos de "bandera"
                self.ordenar_(n)
            elif self.bandera[n] == "G":
                self.g.append(self.bandera[n])
                n += 1
                self.ordenar_(n)
            elif self.bandera[n] == "B":
                self.b.append(self.bandera[n])
                n += 1
                self.ordenar_(n)

if __name__ == "__main__":

    bandera = ["B","G","G","R","G","R","B","B"]
    print("Bandera sin ordenar: {}".format(bandera))
    bandera = Bandera(bandera, r=[], g=[], b=[])
    bandera.ordenar_(n=0)
```
