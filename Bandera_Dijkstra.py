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
            resultado = self.r + self.g + self.b
            return print ("La bandera ordenada quedaria asi: {}".format(resultado))
        else:
            if self.bandera[n] == "R":
                self.r.append("R")
                n += 1
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
    bandera = Bandera(bandera, r=[], g=[], b=[])
    bandera.ordenar_(n=0)