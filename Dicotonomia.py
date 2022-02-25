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
