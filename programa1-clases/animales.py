class Animales:
    def __int__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas

class Conejo(Animales):
    tipo="Conejo"
    def __init__(self,nombre,color,patas):
        super().__init__(nombre,color,patas)
    def sonido(self):
        return "coui"
    print(f"Mi conejo se llama {self.nombre}, es color {self.color} y tiene {self.patas}")

class Ornitorrinco(Animales):
    tipo="Ornitorrinco"
    def __init__(self,nombre,color,patas,tamaño):
        super().__init__(nombre,color,patas)
        self.tamaño=tamaño
    def sonido(self):
        return "krrrrrr"
    print(f"Mi ornitorrinco se llama {self.nombre}, es color {self.color}  tiene {self.patas} y su pico mide {self.tamaño}")


       