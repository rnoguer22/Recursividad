class Bandera:
    #Definimos el constructor
    def __init__(self, bandera):
        self.bandera = bandera
    
    def ordenar_(self):
        #Definimos las listas donde se almacenaran los colores de cada tipo
        r = []
        g = []
        b = []
        if self.bandera == "R":
            r.append(self.bandera)
        elif self.bandera == "G":
            g.append(self.bandera)
        elif self.bandera == "B":
            b.append(self.bandera)