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
        if len(self.bandera) == n:
            return [r, g, b]
        else:
            if self.bandera[n] == "R":
                r.append(self.bandera[n])
                n += 1
                self.ordenar_(n)
            elif self.bandera[n] == "G":
                g.append(self.bandera[n])
                n += 1
                self.ordenar_(n)
            elif self.bandera[n] == "B":
                b.append(self.bandera[n])
                n += 1
                self.ordenar_(n)

if __name__ == "__main__":

    bandera = ["B","G","G","R","G","R","B","B"]
    bandera = Bandera(bandera)
    print (bandera.ordenar_(n=0))