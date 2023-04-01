import teste2
import Function
import random
import vantagenspoke
Bag_Items = []
Bag_pc = []
Bag_badges = []
Bag_Pok = []
Bag_fainted = []
Penny_team1 = []
Penny_fainted = []
kripke_team = []
kripke_fainted = []
stuart_team = []
stuart_fainted = []
howard_team = []
howard_fainted = []
raj_team = []
raj_fainted = []
leonard_team = []
leonard_fainted = []
sheldon_team = []
sheldon_fainted = []
everything = True
while everything:
    if "Penny's Fight" not in Bag_badges:
        penny_battle = input("You want to battle with Penny?(Y/N)")
        if penny_battle.upper() == "N":
            print("PENNY: Oh, ok! I don't knewed you are a coward!")
            x = input("Press enter...")
            print(f"PENNY: Good luck, i think you gonna need it...")
            x = input("Press enter...")
            Bag_badges.append("Penny's Fight")
            pass
        elif penny_battle.upper() == "Y":
            print("PENNY: So let's battle...")
            x = input("Press enter...")
            print("-- IN BATTLE --")
            x = input("Press enter...")
            Penny_battle = True
            while Penny_battle:
                contador_team = 0
                for i in Bag_Pok:
                    contador_team += 1
                    print(f"{contador_team} -- {i.get_name_pok()}")
                select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                if select_fighter.isnumeric():
                    if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                        selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                        penny_selected = random.choice(Penny_team1)
                        battle = selected_pokemon.Battle(penny_selected)
                        if battle == "Lose":
                            print("You lose the battle...")
                            Bag_Pok.remove(selected_pokemon)
                            Bag_fainted.append(selected_pokemon)
                            x = input("Press enter...")
                            if len(Bag_Pok) == 0:
                                print("All your Pokemons are fainted!")
                                x = input("Press enter...")
                                print("You lose for Penny...")
                                Bag_badges.append("Penny's Fight")
                                penny_battle = False
                            else:
                                pass
                        elif battle == "Win":
                            print("You win the battle!")
                            Penny_team1.remove(penny_selected)
                            Penny_fainted.append(penny_selected)
                            x = input("Press enter...")
                            if len(Penny_team1) == 0:
                                print("All of Penny's Pokemon are fainted...")
                                x = input("Press enter...")
                                print("You Won!!")
                                Bag_badges.append("Penny's Fight")
                                penny_battle = False
                            else:
                                pass
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif int(select_fighter) not in range(1, len(Bag_Pok) + 1):
                        print("INVALID!!")
                        x = input("Press enter...")
                        pass
                elif select_fighter.isnumeric() != int:
                    print("INVALID!!")
                    x = input("Press enter...")
                    pass
                else:
                    print("INVALID!!")
                    x = input("Press enter...")
                    pass
    elif "Penny's Fight" in Bag_badges:
        if len(Bag_Pok) <= 0:
            print("Your Pokemons are fainted...")
            x = input("Press enter...")
            print("Go to upa and recover them!")
            x = input("Press enter...")
            pass
        elif len(Bag_Pok) > 0:
            if "Badge" not in Bag_badges: 
                print("-- TOURNAMENT START ANNOUNCED --")
                x = input("Press enter...")
                print("YOU: So i think, it's the time...")
                x = input("Press enter...")
                print("YOU: Let's battle...")
                x = input("Press enter...")
                Bag_badges.append("Badge")
                pass
            elif "Badge" in Bag_badges:
                tournment = True
                while tournment:
                    if "Badge1" not in Bag_badges:
                        print("-- START TOURNMENT --")
                        x = input("Press enter...")
                        print("-- Phase 1 --")
                        print("-- Competitor Kripke --")
                        x = input("Press enter...")
                        print("Kripke: I'm going to finish you off with my Insect type Pokemons!")
                        x = input("Press enter...")
                        fight1 = True
                        while fight1:
                            contador_fight = 0
                            for i in Bag_Pok:
                                contador_fight += 1
                                print(f"{contador_fight} -- {i.get_name_pok()}")
                            select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                            if select_fighter.isnumeric():
                                if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                    selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                    kripke_selected = random.choice(kripke_team)
                                    battle = selected_pokemon.Battle(kripke_selected)
                                    if battle == "Lose":
                                        print("You lose the battle...")
                                        Bag_Pok.remove(selected_pokemon)
                                        Bag_fainted.append(selected_pokemon)
                                        x = input("Press enter...")
                                        if len(Bag_Pok) == 0:
                                            print("All your Pokemons are fainted!")
                                            x = input("Press enter...")
                                            print("You lose...")
                                            fight1 = False
                                            tournment = False
                                        else:
                                            pass
                                    elif battle == "Win":
                                        print("You win the battle!")
                                        kripke_team.remove(kripke_selected)
                                        kripke_fainted.append(kripke_selected)
                                        x = input("Press enter...")
                                        if len(kripke_team) == 0:
                                            print("All of Kripke's Pokemon are fainted...")
                                            x = input("Press enter...")
                                            print("You Won!!")
                                            Bag_badges.append("Badge1")
                                            fight1 = False
                                        else:
                                            pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif int(select_fighter) not in range(1, len(Bag_Pok) + 1):
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            elif select_fighter.isnumeric() != int:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                    elif "Badge2" not in Bag_badges:
                        print("-- YOU ADVANCE IN PHASE --")
                        x = input("Press enter...")
                        print("-- Phase 2 --")
                        x = input("Press enter...")
                        print("-- Competitor Stuart --")
                        x = input("Press enter...")
                        print("Stuart: I'm going to finish you off with my Fire type pokemons")
                        x = input("Press enter...")
                        fight2 = True
                        while fight2:
                            contador_fight2 = 0
                            for i in Bag_Pok:
                                contador_fight2 += 1
                                print(f"{contador_fight2} -- {i.get_name_pok()}")
                            select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                            if select_fighter.isnumeric():
                                if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                    selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                    stuart_selected = random.choice(stuart_team)
                                    battle = selected_pokemon.Battle(stuart_selected)
                                    if battle == "Lose":
                                        print("You lose the battle...")
                                        Bag_Pok.remove(selected_pokemon)
                                        Bag_fainted.append(selected_pokemon)
                                        x = input("Press enter...")
                                        if len(Bag_Pok) <= 0:
                                            print("All your Pokemons are fainted!")
                                            x = input("Press enter...")
                                            print("You lose...")
                                            fight2 = False
                                            
                                        else:
                                            pass
                                    elif battle == "Win":
                                        print("You win the battle!")
                                        stuart_team.remove(stuart_selected)
                                        stuart_fainted.append(stuart_selected)
                                        x = input("Press enter...")
                                        if len(stuart_team) == 0:
                                            print("All of Stuart's Pokemon are fainted...")
                                            x = input("Press enter...")
                                            print("You Won!!")
                                            Bag_badges.append("Badge2")
                                            fight2 = False
                                        else:
                                            pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif int(select_fighter) not in range(1, len(Bag_Pok) + 1):
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            elif select_fighter.isnumeric() != int:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                    elif "Badge3" not in Bag_badges:
                        print("-- YOU ADVANCE IN PHASE --")
                        x = input("Press enter...")
                        print("-- Phase 3 --")
                        x = input("Press enter...")
                        print("-- Competitor Howard --")
                        x = input("Press enter...")
                        print("Howard: I'm going to finish you off with my Watter type pokemons")
                        x = input("Press enter...")
                        fight3 = True
                        while fight3:
                            contador_fight3 = 0
                            for i in Bag_Pok:
                                contador_fight3 += 1
                                print(f"{contador_fight3} -- {i.get_name_pok()}")
                            select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                            if select_fighter.isnumeric():
                                if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                    selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                    howard_selected = random.choice(howard_team)
                                    battle = selected_pokemon.Battle(howard_selected)
                                    if battle == "Lose":
                                        print("You lose the battle...")
                                        Bag_Pok.remove(selected_pokemon)
                                        Bag_fainted.append(selected_pokemon)
                                        x = input("Press enter...")
                                        if len(Bag_Pok) == 0:
                                            print("All your Pokemons are fainted!")
                                            x = input("Press enter...")
                                            print("You lose...")
                                            fight3 = False
                                            tournment = False
                                        else:
                                            pass
                                    elif battle == "Win":
                                        print("You win the battle!")
                                        howard_team.remove(howard_selected)
                                        howard_fainted.append(howard_selected)
                                        x = input("Press enter...")
                                        if len(howard_team) == 0:
                                            print("All of Howard's Pokemon are fainted...")
                                            x = input("Press enter...")
                                            print("You Won!!")
                                            Bag_badges.append("Badge3")
                                            fight3 = False
                                        else:
                                            pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif int(select_fighter) not in range(1, len(Bag_Pok) + 1):
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            elif select_fighter.isnumeric() != int:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                    elif "Badge4" not in Bag_badges:
                        print("-- YOU ADVANCE IN PHASE --")
                        x = input("Press enter...")
                        print("-- Phase 4 --")
                        x = input("Press enter...")
                        print("-- Competitor Raj --")
                        x = input("Press enter...")
                        print("Raj: I'm going to finish you off with my Grass type pokemons")
                        x = input("Press enter...")
                        fight4 = True
                        while fight4:
                            contador_fight4 = 0
                            for i in Bag_Pok:
                                contador_fight4 += 1
                                print(f"{contador_fight4} -- {i.get_name_pok()}")
                            select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                            if select_fighter.isnumeric:
                                if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                    selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                    raj_selected = random.choice(raj_team)
                                    battle = selected_pokemon.Battle(raj_selected)
                                    if battle == "Lose":
                                        print("You lose the battle...")
                                        Bag_Pok.remove(selected_pokemon)
                                        Bag_fainted.append(selected_pokemon)
                                        x = input("Press enter...")
                                        if len(Bag_Pok) == 0:
                                            print("All your Pokemons are fainted!")
                                            x = input("Press enter...")
                                            print("You lose...")
                                            fight4 = False
                                            tournment = False
                                        else:
                                            pass
                                    elif battle == "Win":
                                        print("You win the battle!")
                                        raj_team.remove(raj_selected)
                                        raj_fainted.append(raj_selected)
                                        x = input("Press enter...")
                                        if len(raj_team) == 0:
                                            print("All of Raj's Pokemon are fainted...")
                                            x = input("Press enter...")
                                            print("You Won!!")
                                            Bag_badges.append("Badge4")
                                            fight4 = False
                                        else:
                                            pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif int(select_fighter) not in range(1, len(Bag_Pok) + 1):
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            elif select_fighter.isnumeric() != int:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                    elif "Semifinal" not in Bag_badges:
                        print("-- YOU ADVANCE IN PHASE --")
                        x = input("Press enter...")
                        print("-- Semifinal --")
                        x = input("Press enter...")
                        print("-- Semifinalist Leonard --")
                        x = input("Press enter...")
                        print("Leonard: I'm going to finish you off with my Normal type pokemons")
                        x = input("Press enter...")
                        fight5 = True
                        while fight5:
                            contador_fight5 = 0
                            for i in Bag_Pok:
                                contador_fight5 += 1
                                print(f"{contador_fight5} -- {i.get_name_pok()}")
                            select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                            if select_fighter.isnumeric():
                                if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                    selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                    leonard_selected = random.choice(leonard_team)
                                    battle = selected_pokemon.Battle(leonard_selected)
                                    if battle == "Lose":
                                        print("You lose the battle...")
                                        Bag_Pok.remove(selected_pokemon)
                                        Bag_fainted.append(selected_pokemon)
                                        x = input("Press enter...")
                                        if len(Bag_Pok) == 0:
                                            print("All your Pokemons are fainted!")
                                            x = input("Press enter...")
                                            print("You lose for...")
                                            fight5 = False
                                            tournment = False
                                        else:
                                            pass
                                    elif battle == "Win":
                                        print("You win the battle!")
                                        leonard_team.remove(leonard_selected)
                                        leonard_fainted.append(leonard_selected)
                                        x = input("Press enter...")
                                        if len(leonard_team) == 0:
                                            print("All of Leonard's Pokemon are fainted...")
                                            x = input("Press enter...")
                                            print("You Won!!")
                                            Bag_badges.append("Semifinal")
                                            fight5 = False
                                        else:
                                            pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif int(select_fighter) not in range(1, len(Bag_Pok) + 1):
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            elif select_fighter.isnumeric() != int:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                    elif "Champion" not in Bag_badges:
                        print("-- YOU ADVANCE IN PHASE --")
                        x = input("Press enter...")
                        print("-- Final --")
                        x = input("Press enter...")
                        print("-- Semifinalist Sheldon --")
                        x = input("Press enter...")
                        print("Sheldon: I'm going to finish you off with my Psyquic type pokemons")
                        x = input("Press enter...")
                        fight6 = True
                        while fight6:
                            contador_fight6 = 0
                            for i in Bag_Pok:
                                contador_fight6 += 1
                                print(f"{contador_fight6} -- {i.get_name_pok()}")
                            select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                            if select_fighter.isnumeric():
                                if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                    selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                    sheldon_selected = random.choice(sheldon_team)
                                    battle = selected_pokemon.Battle(sheldon_selected)
                                    if battle == "Lose":
                                        print("You lose the battle...")
                                        Bag_Pok.remove(selected_pokemon)
                                        Bag_fainted.append(selected_pokemon)
                                        x = input("Press enter...")
                                        if len(Bag_Pok) == 0:
                                            print("All your Pokemons are fainted!")
                                            x = input("Press enter...")
                                            print("You lose for...")
                                            fight6 = False
                                        else:
                                            pass
                                    elif battle == "Win":
                                        print("You win the battle!")
                                        sheldon_team.remove(sheldon_selected)
                                        sheldon_fainted.append(sheldon_selected)
                                        x = input("Press enter...")
                                        if len(sheldon_team) == 0:
                                            print("All of Sheldon's Pokemon are fainted...")
                                            x = input("Press enter...")
                                            print("You Won!!")
                                            Bag_badges.append("Champion")
                                            fight6 = False
                                            tournment = False
                                        else:
                                            pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif int(select_fighter) not in range(1, len(Bag_Pok) + 1):
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                            elif select_fighter.isnumeric() != int:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass

                




