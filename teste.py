# Loja POKEBALL
import random
import Do_it
Bag_Items = ["Potion","Potion","Potion","Pokeball","Pokeball","Greatball","Greatball","Ultraball","Ultraball","Ultraball","Ultraball","Ultraball","Ultraball","Ultraball"]
Bag_Pok = []
Bag_pc = []
on_boat = True
while on_boat:
    print("-- IN THE TABAPUA LAKE --")
    print('''-- CHOOSE --
1 -- USE THE SUPER ROD IN LEFT SIDE
2 -- USE THE SUPER ROD IN RIGHT SIDE
3 -- USE THE SUPER ROD ON THE BOAT'S PROW
4 -- CAME BAKE TO HARBOR''')
    do_boat = input("Select 1, 2, 3 or 4:")
    if do_boat in ("1", "2", "3"):
        print("Using Super Rod...")
        x = input("Press enter...")
        find = (Do_it.found_lake())
        if find != "Nothing here...":
            ask_catch = input(f"Try catch {find}?(Y/N)")
            if ask_catch.upper() == "N":
                print("Oskey?!")
                x = input("Press enter...")
                pass
            elif ask_catch.upper() == "Y":
                trhow_ball = True
                while trhow_ball:
                    contador2 = 0
                    contador3 = 0
                    contador4 = 0        
                    for i in Bag_Items:
                        if i == "Pokeball":
                            contador2 += 1
                        elif i == "Greatball":
                            contador3 += 1
                        elif i == "Ultraball":
                            contador4 += 1
                    print(f"You have {contador2} Pokeball")
                    print(f"You have {contador3} Greatball")
                    print(f"You have {contador4} Ultraball")
                    wich_ball = input("Wich ball you want to use?")
                    if wich_ball.upper() == "POKEBALL":
                        if contador2 > 0:
                            print("Trhowing Pokeball...")
                            Bag_Items.remove("Pokeball")
                            x = input("Press enter...")
                            chance_catch = random.randint(1,101)
                            if chance_catch > 45:
                                print("The Pokeball failed...")
                                x = input("Press enter...")
                                pass
                            elif chance_catch <= 45:
                                if len(Bag_Pok) >= 6:
                                    print(f"Gotcha! {find} was captured and added on your Pc!")
                                    Bag_pc.append(find)
                                    trhow_ball = False
                                elif len(Bag_Pok) <= 6:
                                    print(f"Gotcha! {find} was captured and added on your team!")
                                    Bag_Pok.append(find)
                                    trhow_ball = False
                                else:
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                        elif contador2 == 0:
                            print("You don't have enough Pokeballs!")
                            x = input("Press enter...")
                            pass
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif wich_ball.upper() == "GREATBALL":
                        if contador3 > 0:
                            print("Trhowing Greatball...")
                            Bag_Items.remove("Greatball")
                            x = input("Press enter...")
                            chance_catch = random.randint(1,101)
                            if chance_catch > 60:
                                print("The Greatball failed...")
                                x = input("Press enter...")
                                pass
                            elif chance_catch <= 60:
                                if len(Bag_Pok) >= 6:
                                    print(f"Gotcha! {find} was captured and added on your Pc!")
                                    Bag_pc.append(find)
                                    trhow_ball = False
                                elif len(Bag_Pok) <= 6:
                                    print(f"Gotcha! {find} was captured and added on your team!")
                                    Bag_Pok.append(find)
                                    trhow_ball = False
                                else:
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                        elif contador3 == 0:
                            print("You don't have enough Pokeballs!")
                            x = input("Press enter...")
                            pass
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif wich_ball.upper() == "ULTRABALL":
                        print("Trhowing Ultraball...")
                        Bag_Items.remove("Ultraball")
                        x = input("Press enter...")
                        chance_catch = random.randint(1,101)
                        if chance_catch > 80:
                            print("The Ultraball failed...")
                            x = input("Press enter...")
                            pass
                        elif chance_catch <= 80:
                            if len(Bag_Pok) >= 6:
                                print(f"Gotcha! {find} was captured and added on your Pc!")
                                Bag_pc.append(find)
                                trhow_ball = False
                            elif len(Bag_Pok) <= 6:
                                print(f"Gotcha! {find} was captured and added on your team!")
                                Bag_Pok.append(find)
                                trhow_ball = False
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass            
        elif find == "Nothing here...":
            print("You find nothing...")
            x = input("Press enter...")
            pass
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
    elif do_boat == "4":
        do_exit = input("Want to leave the boat?(Y/N)")
        if do_exit.upper() == "N":
            print("Oskey?!")
            x = input("Press enter...")
            pass
        elif do_exit.upper() == "Y":
            print("Leaving...")
            x = input("Press enter...")
            on_boat = False
        else: 
            print("INVALID!!")
            x = input("Press enter...")
            pass
    else: 
            print("INVALID!!")
            x = input("Press enter...")
            pass
    
    


                                 






