class Bandera:
    #Definimos el constructor
    def __init__(self, bandera):
        self.bandera = bandera
    
    def ordenar_(self, n):
        #Definimos las listas donde se almacenaran los colores de cada tipo
        r = []
        g = []
        b = []
        #Añadimos un contador que nos ayudara a recorrer "bandera"
        n = 0
        if self.bandera[n] == "R":
            r.append(self.bandera[n])
            n += 1
            self.ordenar_(self, n)
        elif self.bandera[n] == "G":
            g.append(self.bandera[n])
            n += 1
            self.ordenar_(self, n)
        elif self.bandera[n] == "B":
            b.append(self.bandera[n])
            n += 1
            self.ordenar_(self, n)
        else:
            return [r, g, b]