class Palindromo:
    #Definimos el constructor
    def __init__(self, frase):
        self.frase = frase
            
    #Funcion para pasar la frase a mayusculas y eliminar las tildes
    def mayusculas_tildes (self):
        self.frase.upper()
        self.frase.replace(" ", "")
        self.frase.replace("Á", "A")
        self.frase.replace("É", "E")
        self.frase.replace("Í", "I")
        self.frase.replace("Ó", "O")
        self.frase.replace("Ú", "U")
        return self.frase

    #Esta funcion devuelve un booleano que nos dice si es palindromo o no
    def es_palindromo(self):
        self.frase = list(self.frase)
        if self.frase[0] == self.frase[-1]:
            self.frase = self.frase[1:len(self.frase)]
            return self.es_palindromo()
        else:
            return False

if __name__ == '__main__':

    oracion = input("Introduzca la frae a analizar: ")
    resultado = Palindromo(oracion)
    print(resultado.es_palindromo())