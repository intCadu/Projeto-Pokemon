import random

class Pokemon:
    def __init__(self, name, lv, tipo, Hp, Atk, Def, Speed):
        self.name = name
        self.lv = lv
        self.tipo = tipo
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Speed = Speed

    def Battle(self, oponente):
        print(f"IN BATTLE {self.name} VS {oponente.name}")
        contador = 1
        vantagem = 1
        
        while True:
            x = input("Press Enter to continue or 0 to run.")
            if x == " ":
                pass
            elif x == "0":
                break
            print(f"ROUND {contador}")
            contador += 1
            
            match self.tipo:
                case "Fire":
                    if oponente.tipo == "Grass":
                        vantagem += 1
                case "Water":
                    if oponente.tipo == "Fire":
                        vantagem += 1
                case "Grass":
                    if oponente.tipo == "Water":
                        vantagem += 1

            match oponente.tipo:
                case "Fire":
                    if self.tipo == "Grass":
                        vantagem += 1
                case "Water":
                    if self.tipo == "Fire":
                        vantagem += 1
                case "Grass":
                    if self.tipo == "Water":
                        vantagem += 1
                             
            dano = (self.Atk - oponente.Def)
            dano_total = (dano * vantagem) 
            oponente.Hp = (oponente.Hp - (dano_total))
            print(f"{self.name} give {dano_total} of damage in {oponente.name}!")
            print(f"The {oponente.name} Hp downs to {oponente.Hp}!")


            dano = (oponente.Atk - self.Def)
            dano_total = (dano * vantagem)
            self.Hp = (self.Hp - dano_total)
            print(f"{oponente.name} give {dano_total} of damage in {self.name}!")
            print(f"The {self.name} Hp downs to {self.Hp}!")
            
           
            if self.Hp <= 0:
                print(f"{oponente.name} WINS THE BATTLE. CONGRATULATIONS!!")
                break
            if oponente.Hp <= 0:
                print(f"YOU LOOSE.{self.name} WINS THE BATTLE!!")
                break

class Charizard(Pokemon):
    def __init__(self, name, lv, tipo, Hp, Atk, Def, Speed):
        super().__init__(name, lv, tipo, Hp, Atk, Def, Speed)
class Blastoise(Pokemon):
    def __init__(self, name, lv, tipo, Hp, Atk, Def, Speed):
        super().__init__(name, lv, tipo, Hp, Atk, Def, Speed)
class Venussaur(Pokemon):
    def __init__(self, name, lv, tipo, Hp, Atk, Def, Speed):
        super().__init__(name, lv, tipo, Hp, Atk, Def, Speed)
         

pokemon1 = Charizard("Charizard",100, "fogo", 250, 150, 60)
pokemon2 = Blastoise("Blastoise",100,"agua", 300, 100, 85)
pokemon3 = Venussaur("Venussaur",100,"planta", 450, 90, 75)

lista_pokemon = [pokemon3, pokemon2 , pokemon3]

print("Escolha o pokemon que deseja iniciar!")
print('''Escolha entre: 
  1 -- Charizard
  2 -- Blastoise
  3 -- Venussaur''')

str_pokemon = input("Escolha seu pokemon inicial:")
match str_pokemon:
    case "1":
        str_pokemon = pokemon1
    case "2":
        str_pokemon = pokemon2
    case "3":
        str_pokemon = pokemon3
    case _:
        print("O Pokemon escolhido é inválido! Escolha um inicial válido.")

random.choice(lista_pokemon).Battle(str_pokemon)














        
