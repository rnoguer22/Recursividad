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