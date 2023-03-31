import Van
import Function
import random
Bag_Items = []
Bag_pc = []
Bag_Pok = [Van.Abra, Van.Aerodactyl, Van.Arcanine, Van.Articuno]
Penny_team1 = [Van.Abra, Van.Aerodactyl, Van.Arcanine, Van.Articuno]

# print("PENNY: So let's battle...")
# x = input("Press enter...")
# print("-- IN BATTLE --")
# x = input("Press enter...")    
# contador_team = 0
# for i in Bag_Pok:
#     contador_team += 1
#     print(f"{contador_team} -- {i.get_name_pok()}")
# select_fighter = int(input(f"Select one in {len(Bag_Pok)} Pokemons:"))
# if select_fighter in range(1,len(Bag_Pok)+1):
#     selected_pokemon = Bag_Pok[select_fighter-1]
#     selected_pokemon.Battle(random.choice(Penny_team1)) 


print("Entering the bush...")
x = input("Press enter...")
found = (Function.found_bush())
if found == "Nothing here...":
    pass
else:
    print(f"You found {found.get_name_pok()}!") 
    capture = input(f"Try to cath {found.get_name_pok()}?(Y/N)")
    if capture.upper() == "N":
        pass
    elif capture.upper() == "Y":
        catch = True
        while catch:
            count = Bag_Items.count("Pokeball")
            if count >= 1:
                trhow = input("You want to trhow a Pokeball?(Y/N)")
                if trhow.upper() == "N":
                    print("Oskey?!")
                    catch = False
                elif trhow.upper() == "Y":
                    print(f"You have {count} Pokeballs!")
                    print("Trhowing a Pokeball...")
                    x = input("Press enter...")
                    chance_catch = random.randint(1,101)
                    if chance_catch < 45:
                        print("The Pokeball failed...")
                        Bag_Items.remove("Pokeball")
                        pass
                    elif chance_catch > 45:
                        print(f"Gotcha!! The {found} was added on your list.")
                        Bag_Pok.append(found)
                        Bag_Items.remove("Pokeball")
                        catch = False
            else:
                print("You don't have enough Pokeball...")
                catch = False


