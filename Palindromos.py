class Palindromo:
    #Definimos el constructor
    def __init__(self, frase):
        self.frase = frase
    
    #Funcion para saber si un caracter es del alfabeto
    def es_alfabetico(self, car):
        return car.isupper() or car.islower()

    def alfanumerico(self):
        if self.frase == False:
            return self.frase