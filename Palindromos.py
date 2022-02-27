class Palindromo:
    #Definimos el constructor
    def __init__(self, frase):
        self.frase = frase
    
    #Funcion para saber si un caracter es del alfabeto
    def es_alfabetico(self, car):
        
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


    def alfanumerico(self):
        if self.frase == False:
            return self.frase