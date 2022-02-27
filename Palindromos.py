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