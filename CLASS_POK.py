
# Pokemon - classe
class Pokemon:
    def __init__(self, Name, lv, tipo, Hp, Atk, Def,):
        self.name = Name
        self.lv = lv
        self.tipo = tipo
        self.Hp = Hp
        self.Atk = Atk
        self.DEF = Def


class Fire(Pokemon):
    def __init__(self, Name, lv, tipo, Hp, Atk, Def):
        super().__init__(Name, lv, tipo, Hp, Atk, Def)
  
class Grass(Pokemon):
    def __init__(self, Name, lv, tipo, Hp, Atk, Def):
        super().__init__(Name, lv, tipo, Hp, Atk, Def)

class Water(Pokemon):
    def __init__(self, Name, lv, tipo, Hp, Atk, Def):
        super().__init__(Name, lv, tipo, Hp, Atk, Def)


# Treinador - classe
class Treinador:
    def __init__(self,lista_pok):
        self.lista_pok = lista_pok
    
    def lista_pokemon(self):
        self.lista_pok = []
        self.lista_pok.append(Pokemon)

class Oponente(Treinador):
    def __init__(self, lista_pok):
        super().__init__(lista_pok)

class Jogador(Treinador):
    def __init__(self, lista_pok):
        super().__init__(lista_pok)


