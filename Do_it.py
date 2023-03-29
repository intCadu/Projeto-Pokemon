def Pc_Pok(pokemon):
    if len(Bag_Pok) == 6:
        Bag_pc.append(pokemon)
    return Bag_pc 

def change_team(pokemon1, pokemon2):
    if pokemon1 in Bag_Pok:
        Bag_Pok.remove(pokemon1) and Bag_pc.append(pokemon1)
    if pokemon2 in Bag_pc:
        Bag_pc.remove(pokemon2) and Bag_Pok.append(pokemon2)
Bag_Items = []
quantidade = input("How many do you want?")
for i in quantidade:
    Bag_Items.append("Potion")
print(Bag_Items)