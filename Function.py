import random
import Van


def Pc_Pok(pokemon):
    if len(Bag_Pok) == 6:
        Bag_pc.append(pokemon)
    return Bag_pc 
Bag_Pok = []
Bag_pc = []
def change_team(pokemon1, pokemon2):

    if pokemon1 in Bag_Pok:
        Bag_Pok.remove(pokemon1) and Bag_pc.append(pokemon1)
    if pokemon2 in Bag_pc:
        Bag_pc.remove(pokemon2) and Bag_Pok.append(pokemon2)

def Battle(self, oponente):
        print("IN BATTLE",self.name," VS ",oponente.name)
        contador = 1
        self.vantagem = 1
        oponente.vantagem = 1

        self.vantagem = self.Check_Vantagem(oponente)

        oponente.vantagem = oponente.Check_Vantagem(self)
        
        while True:
            x = input("Press Enter to continue or 0 to run.")
            if x == " ":
                pass
            elif x == "0":
                break
            print("""            ROUND""",contador)
            contador += 1

            if self.Speed > oponente.Speed:

                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano > 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                else: print("Damage of",self.name,"was null.")
                if oponente.Hp <= 0:
                    print(self.name,"WINS THE BATTLE. CONGRATULATIONS!!")
                    break
                
                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano > 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in ",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                else: print("Damage of",oponente.name,"was null.")
                if self.Hp <= 0:
                    print("YOU LOOSE!",oponente.name,"WINS THE BATTLE!!")
                    break

            if oponente.Speed > self.Speed:

                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano > 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in ",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                else: print("Damage of",oponente.name,"was null.")
                if self.Hp <= 0:
                    print("YOU LOOSE!",oponente.name,"WINS THE BATTLE!!")
                    break

                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano > 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                else: print("Damage of",self.name,"was null.")
                if oponente.Hp <= 0:
                    print(self.name,"WINS THE BATTLE. CONGRATULATIONS!!")
                    break

def found_lake():
    pok_lake = [Van.PokeAgua]
    chance_found = random.randint(1, 101)
    if chance_found <= 25:
        nothing = "Nothing here..."
        return nothing
    elif chance_found > 25:
        found_lake1 = random.choice(pok_lake)
        return found_lake1
    else:
        invalid = "INVALID!!"
        return invalid


