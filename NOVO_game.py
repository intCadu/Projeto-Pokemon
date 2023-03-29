import Do_it
import random

class Player:
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age
        
    
    def get_information(self):
        return (f"GENDER: {jogador}, NAME: {nome_jogador}, AGE: {idade_jogador}")
    
    def set_name(self, new_name):
        self.name = new_name
        return new_name

Bag_Pok = []
Bag_Items = ["Wallet"]
Bag_pc = []
Wallet = 1000

jogador = ""
nome_jogador = ""
Game = True
while Game:
    
    
    print("Press B(BOY) or G(GIRL)!")
    ask_Tipo = input("Chose your Gender:")   
    if ask_Tipo.upper() == "B":
        jogador = "BOY"
        pass
    elif ask_Tipo.upper() == "G":
        jogador = "GIRL"
        pass
    else:
        print("INVALID ANSWER!!!")
        print("TRY AGAIN!!")
        break
    age_jogador = int(input("What's your age?"))
    if age_jogador:
        if age_jogador < 100:
            idade_jogador = age_jogador
            pass
        elif age_jogador > 100:
            print("INVALID AGE!!")
            print("TRY AGAIN!!")
            break
        else:
            break
    else:
        print("INVALID ANSWER!!!")
        print("TRY AGAIN!!")
        break

    nome_jogador = input("What's the player name?")
    nome_confirmacao = input(f"Your name is {nome_jogador}?(Y/N)")
    if nome_confirmacao.upper() == "Y":
        player1 = Player(jogador,nome_jogador,idade_jogador)
        x = input("You want to see your informations?(Y/N)")
        if x.upper() == "Y":
            print(player1.get_information())
            Game = False
        else:
            Game = False
        # Precisa melhorar a logica da Função set_name
    elif nome_confirmacao.upper() == "N":
        new_nome_jogador = input("What's your name:")
        player1.set_name(new_nome_jogador)
        x = input("You want to see your informations?(Y/N)")
        if x.upper() == "Y":
            print(player1.get_information())
            Game = False
        else:
            Game = False
    else: 
        ("INVALID ANSWER!!!")
        break
    

    partner = True
    while partner:
        print('''CHOSE YOUR PATH!!
        1 -- GO TO LABORATORY 
        2 -- TALK TO MOM
        3 -- GO TO ROOM''')

        path_jogador = input("Select 1, 2 or 3:")
        if path_jogador == "1":
            path1 = input("You want go to laboratory?(Y/N)")
            if path1.upper() == "N":
                print("Oskey?!")
                pass
            elif path1.upper() == "Y":
                print("You are in laboratory...")
                x = input("Press enter to speak with Prf. Tarik...")
                print(f"Oh! Hello {player1.name}, i was here studing Pokemons...")
                x = input("Press enter...")
                print("And i have a dicover, there are many Pokemons in the world...")
                x = input("Press enter...")
                print("So i create a Pokedex, a machine to research about every Pokemon data...")
                x = input("Press enter...")
                print("But i have one problem about it...")
                x = input("Press enter...")
                print("I can't leave the laboratory alone here in Caucaia City...")
                x = input("Press enter...")
                print("I was thinking, can you do this for me?")
                journey = input("Do you want go to this journey?(Y/N)")
                if journey.upper() =="Y":
                    print("Wonderful, i'll give some help with this...")
                    x = input("Press enter...")
                    print("Of course, you will need a partner...")
                    x = input("Press enter...")
                    chose_partner = input("Let's gonna chose your partner?(Y/N)")
                    if chose_partner.upper() == "Y":
                        print("Here, i have three diferent Pokemons...")
                        x = input("Press enter...")
                        i = True
                        while i:
                            print('''Chose your Partner:
1 -- Charmander
2 -- Squirtle
3 -- Bulbassaur''')
                            chose_inicial = input("Chose your partner 1, 2 or 3:")
                            match chose_inicial:
                                case "1":
                                    x = input("You want Charmander to be your partner?(Y/N)")
                                    if x.upper() == "Y":
                                        Bag_Pok.append("Charmander")
                                        print("Charmander was added on your team")
                                        i = False
                                        partner = False
                                    elif x.upper() == "N":
                                        pass
                                    else:
                                        pass
                                case "2":
                                    x = input("You want Squirtle to be your partner?(Y/N)")
                                    if x.upper() == "Y":
                                        Bag_Pok.append("Squirtle")
                                        print("Squirtle was added on your team")
                                        i = False
                                        partner = False
                                    elif x.upper() == "N":
                                        pass
                                    else: 
                                        pass
                                case "3":
                                    x = input("You want Bulbassaur to be your partner?(Y/N)")
                                    if x.upper() == "Y":
                                        Bag_Pok.append("Bulbassaur")
                                        print("Bulbassaur was added on your team")
                                        i = False
                                        partner = False
                                    elif x.upper() == "N":
                                        pass
                                    else:
                                        pass
                    
                    elif chose_partner.upper() == "N":
                        print("Oh! I understand, that's ok...")
                        x = input("Press enter...")
                        print(f"Maybe other time, see you later {player1.name}...")
                        x = input("Press enter...")
                        pass
                    else:
                        pass
                if journey.upper() == "N":
                    print("It's a shame, maybe someone else?!")
                    x = input("Press enter...")
                    print(f"See you later {player1.name}!!")
                    pass

                         
        elif path_jogador == "2":
            if jogador == "BOY":
                print("Hey son, where are you going?")
                x = input("Press enter...")
                print("I know, we just moved and you want to explore the city, ain't it?")
                x = input("Press enter...")
                print("So take care, are many wild Pokemons out there!!")
                x = input("Press enter...")
                print("Bye baby, hurry up!!")
                pass
            if jogador == "GIRL":
                print("Hey daughter, where are you going?")
                x = input("Press enter...")
                print("I know, we just moved and you want to explore the city, ain't it?")
                x = input("Press enter...")
                print("So take care, are many wild Pokemons out there!!")
                x = input("Press enter...")
                print("Bye baby, hurry up!!")
                pass

        elif path_jogador == "3":
            print("YOU: It's just my room, nothing important...")
            x = input("Press enter...")
            print("YOU: Oh my PC, maybe there have some important thing...")
            computer = input("Look your PC?(Y/N)")
            if computer.upper() == "Y":
                print("YOU: Let's see... Oh look i have one potion!!")
                take_potion = input("Take the potion?(Y/N)")
                if take_potion.upper() == "Y":
                    if "Potion" not in Bag_Items:
                        print("YOU: I gonna take it!!")
                        Bag_Items.append("Potion")
                        pass
                    elif "Potion" in Bag_Items:
                        print("You already take it!")
                        x = input("Press enter...")
                        pass
                    else:
                        print("ERROR!")
                        x = input("Press enter...")
                        pass
                elif take_potion.upper() == "N":
                    print("Maybe next time...")
                    x = input("Press enter...")
                    print("I need to hurry up!!")
                    pass
            elif computer.upper() == "N":
                print("Maybe next time...")
                x = input("Press enter...")
                print("I need to hurry up!!")
                pass
            else:
                print("INVALID ANSWER!")
                pass

    
    print(f'''-- BACK IN HOUSE --
{player1.name} WAS GETTING READY TO JOURNEY...''')
    print("MOM: Hey honey, i hear that you recieve your first Pokemon!!")
    x = input("Press enter...")
    print("MOM: That's great, your dad will be proud of you!!")
    x = input("Press enter...")
    print("MOM: You know, he's the gym leader of Fortal City...")
    x = input("Press enter...")
    print("MOM: But despite that, he always dreamed of seeing you become a Pokemon Trainer!")
    x = input("Press enter...")
    print("MOM: Hurry up, take your things, don't forget anything...")
    x = input("Press enter...")
    print("MOM: Your journey start now, go ahead!")
    x = input("Press enter...")
    print("-- GOING OUT SIDE --")
    
    
    start_journey = True
    while start_journey:

        print('''CHOSE YOUR PATH!!
        1 -- GO TO HOUSE 085
        2 -- TALK WITH MAYOR
        3 -- GO TO ROUTE 222
        ''')
        start_route = input("Chose your path 1, 2 or 3:")
        if start_route == "1":
            x = input("You really want go to house 085?(Y/N)")
            if x.upper() == "N":
                print("Oskey?!")
                pass
            elif x.upper() == "Y":
                print("-- INSIDE HOUSE 085 --")
                print(f"Mrs. Teller: Oh, hi {player1.name}!")
                x = input("Press enter...")
                print("Mrs. Teller: What a surprise, i was thinking when you would come see me...")
                x = input("Press enter...")
                print("Mrs. Teller: My daughter Penny are up stairs, go there!")
                x = input("Press enter...")
                print("-- GOING UP --")
                x = input("Press enter...")
                print("PENNY: I need to hurry up, i'm late to see Prf. Tarik")
                x = input("Press enter...")
                print("PENNY: Oh hi, i don't see you there...")
                x = input("Press enter...")
                print(f"PENNY: You must be the {player1.name}, i heard about you!")
                x = input("Press enter...")
                print("PENNY: Whatever, i need to go. Get out of my way!")
                x = input("Press enter...")
                pass
            else:
                pass
        elif start_route == "2":
            x = input("You really want talk with Mayor?(Y/N)")
            if x.upper() == "N":
                print("Oskey?!")
                pass
            elif x.upper() == "Y":
                print("-- INSIDE CITY HALL -- ")
                print("MAYOR VALIM: Work, work, work!")
                x = input("Press enter...")
                print(f"MAYOR VALIM: Hello {player1.name}, you know Caucaia City is the best city in Ceará?")
                x = input("Press enter...")
                print("MAYOR VALIM: Well, soon you will see more and more stuff here. Just wait...")
                x = input("Press enter...")
                print("MAYOR VALIM: Work, work, work!")
                x = input("Press enter...")
                pass
            else:
                pass
        elif start_route == "3":
            x = input("You really want go to ROUTE 222?(Y/N)")
            if x.upper() == "N":
                print("Oskey?!")
                pass
            elif x.upper() == "Y":
                print("-- IN ROUTE 222 --")
                x = input("Press enter...")
                print("YOU: I think this is the start of my journey...")
                x = input("Press enter...")
                print("YOU: What? What are these bushes for?")
                x = input("Press enter...")
                print("-- A TRAVELER SPEAKS --")
                print("Taveler: Hello young trainer!")
                x = input("Press enter...")
                print("Traveler: I was walking around and i heard you...")
                x = input("Press enter...")
                print("Traveler: In this bushes you can found some wild Pokemons... ")
                x = input("Press enter...")
                print("Traveler: But to capture one of them you will need have a Pokeball...")
                x = input("Press enter...")
                print('''Traveler: The Pokeball is a device,
that allows you to capture and store Pokemons inside it''')
                x = input("Press enter...")
                print("YOU: Oh, i understand, but i don't have any with me...")
                x = input("Press enter...")
                print("Traveler: Really? So in this case i can give some Pokeballs to you...")
                x = input("Press enter...")
                give_items = input("You want to take the Traveler's Pokeball?(Y/N)")
                if give_items.upper() == "N":
                    print("Traveler: Are you sure? Oskey?!")
                    pass
                elif give_items.upper() == "Y":
                    print("Traveler: Greatful, take these Pokeball you will not regret it!")
                    for i in range(1, 11):
                        Bag_Items.append("Pokeball")
                    print("-- YOU ADDED POKEBALLS ON YOUR BAG --")
                    print("YOU: This Pokeballs will help me a lot!!")
                    pass
                route_bushes = True
                while route_bushes:
                    enter_bushes = input("Do you want enter in bushes?(Y/N)")
                    if enter_bushes.upper() == "N":
                        print("Oskey?!")
                        route_bushes = False
                    elif enter_bushes.upper() == "Y":
                        on_bushes = True
                        while on_bushes:
                            print("-- CHOOSE THE BUSH --")
                            print('''-- SELECT THE ACTION --
1 -- BUSH 1
2 -- BUSH 2
3 -- BUSH 3
4 -- BUSH 4
9 -- TO EXIT THE BUSHES''')
                            action_bushes = input("Selec your action:")
                            if action_bushes == "1":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                pok_bush1 = ["Chamander","Bulbassaur", "Squirtle", "Caterpie", "Nothing here", "Nothing here", "Nothing here"]
                                found = random.choice(pok_bush1)
                                print(f"You found {found}!")
                                if found == "Nothing here":
                                    pass
                                else: 
                                    capture = input(f"Try to cath {found}?(Y/N)")
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
                                                    if chance_catch < 75:
                                                        print("The Pokeball failed...")
                                                        Bag_Items.remove("Pokeball")
                                                        pass
                                                    elif chance_catch > 75:
                                                        print(f"Gotcha!! The {found} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False
                            elif action_bushes == "2":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                pok_bush1 = ["Chamander","Bulbassaur", "Squirtle", "Caterpie", "Nothing here", "Nothing here", "Nothing here"]
                                found = random.choice(pok_bush1)
                                print(f"You found {found}!")
                                if found == "Nothing here":
                                    pass
                                else: 
                                    capture = input(f"Try to cath {found}?(Y/N)")
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
                                                    if chance_catch < 75:
                                                        print("The Pokeball failed...")
                                                        Bag_Items.remove("Pokeball")
                                                        pass
                                                    elif chance_catch > 75:
                                                        print(f"Gotcha!! The {found} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False                            
                            elif action_bushes == "3":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                pok_bush1 = ["Chamander","Bulbassaur", "Squirtle", "Caterpie", "Nothing here", "Nothing here", "Nothing here"]
                                found = random.choice(pok_bush1)
                                print(f"You found {found}!")
                                if found == "Nothing here":
                                    pass
                                else: 
                                    capture = input(f"Try to cath {found}?(Y/N)")
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
                                                    if chance_catch < 75:
                                                        print("The Pokeball failed...")
                                                        Bag_Items.remove("Pokeball")
                                                        pass
                                                    elif chance_catch > 75:
                                                        print(f"Gotcha!! The {found} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False
                            elif action_bushes == "4":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                pok_bush1 = ["Chamander","Bulbassaur", "Squirtle", "Caterpie", "Nothing here", "Nothing here", "Nothing here"]
                                found = random.choice(pok_bush1)
                                print(f"You found {found}!")
                                if found == "Nothing here":
                                    pass
                                else: 
                                    capture = input(f"Try to cath {found}?(Y/N)")
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
                                                    if chance_catch < 75:
                                                        print("The Pokeball failed...")
                                                        Bag_Items.remove("Pokeball")
                                                        pass
                                                    elif chance_catch > 75:
                                                        print(f"Gotcha!! The {found} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False
                            elif action_bushes == "9":
                                cont_bush = input("You really want exit the bushes?(Y/N)")
                                if cont_bush.upper() == "N":
                                    print("Oskey?!")
                                    pass
                                elif cont_bush.upper() == "Y":
                                    print("-- EXIT --")
                                    x = input("Press enter...")
                                    on_bushes = False                        
                    else:
                        print("INVALID OPTION")
                        pass                   
                    if len(Bag_Pok) <= 1:
                        print(f"The size of your team is {len(Bag_Pok)}!")
                        print("Your team isn't enough to move forward...")
                        print("Back and catch some Pokemons!")
                        pass
                    else:
                        print("YOU: I never tought it would be so much fun to be on a journey Pokemon...")
                        x = input("Press enter...")
                        print("YOU: Now i know it, maybe i can be the best trainer of all!")
                        x = input("Press enter...")
                        print("YOU: I'll keep my journey, i think i'm going to battle with my dad! ")
                        x = input("Press enter...")
                        print("YOU: Let's see where my next stop will be...")
                        x = input("Press enter...")
                        print("-- IN JOURNEY --")
                        x = input("Press enter...")
                        start_journey = False
                        route_bushes = False
        else:
            pass
    
    
    print(f"-- {(player1.name).upper()} ARRIVE AT THE TABAPUA LAKE --")
    x = input("Press enter...")
    print("YOU: Oh! A lake that's great, maybe i can catch some new Pokemons...")
    x = input("Press enter...")
    print("-- A STRANGER APPROACHES --")
    x = input("Press enter...")
    print("Fisher: Hey, are you a Pokemon trainer?")
    x = input("Press enter...")
    print("YOU: Yes sir, i came from Caucaia City...")
    x = input("Press enter...")
    print("Fisher: That's great, so you meet Prf. Tarik?")
    x = input("Press enter...")
    print("YOU: Yes, he send me on a journey to see and discover more about Pokemons...")
    x = input("Press enter...")
    print("Fisher: Here in Tabapua Lake we have a lot of water type Pokemons...")
    x = input("Press enter...")
    print("Fisher: But, if you want catch them you will need a special item...")
    x = input("Press enter...")
    print("Fisher: Try found it at North shopping store...")
    x = input("Press enter...")
    print("Fisher: You will find a lot of other things there.")
    x = input("Press enter...")
    print(f"Fisher: I have to go, best of luck on your journey!")
    x = input("Press enter...")
    print("YOU: A special item?! What it can be?")
    x = input("Press enter...")    
    
    
    lake_journey = True
    while lake_journey:
        print('''-- CHOOSE YOUR PATH!! --
1 -- UPA
2 -- GO TO HARBOR
3 -- NORTH SHOPPING STORE
4 -- BATTLE ARENA 
5 -- BLACK GATE''')
        lake_path = input("Select your path 1, 2, 3, 4 or 5:")
        if lake_path.upper() == "1":
            print("-- ENTERING POKESTOP --")
            x = input("Press enter...")
            print("NURSE JOY: Hello young trainer, here in pokestop you can access your PC...")
            x = input("Press enter...")
            print("NURSE JOY: In PC you can store all your Pokemons...")
            x = input("Press enter...")
            print("NURSE JOY: And change your team however you want")
            x = input("Press enter...")
            PC = input("You want use the Pokemon PC?(Y/N)")
            if PC.upper() == "N":
                print("Oskey?!")
                pass
            elif PC.upper() == "Y":
                pc_user = True
                while pc_user:
                    print("-- POKEMON PC --")
                    print('''-- SELECT AN ACTION --
1 -- SEE YOUR POKEMONS
2 -- CHANGE YOUR TEAM
3 -- EXIT PC''')
                    PC_action = input("Select 1, 2 or 3:")
                    if PC_action == "1":
                        see_team = True
                        while see_team:
                            print('''-- SELECT --
1 -- SEE YOUR TEAM
2 -- SEE YOUR STORED POKEMONS
3 -- RETURN''')
                            PC_action2 = input("Select 1, 2 or 3:")
                            if PC_action2 == "1":
                                print(Bag_Pok)
                                x = input("Press enter...")
                                pass
                            elif PC_action2 == "2":
                                print(Bag_pc)
                                x = input("Press enter...")
                                pass
                            elif PC_action2 == "3":
                                back = input("Return to main menu?(Y/N)")
                                if back.upper() == "Y":
                                    print("-- RETURNING --")
                                    x = input("Press enter...")
                                    see_team = False
                                elif back.upper() == "N":
                                    print("Oskey?!")
                                    pass
                                else:
                                    print("INVALID!")
                                    pass                           
                            else:
                                print("INVALID!")
                                x = input("Press enter...")
                                pass                    
                    elif PC_action == "2":
                        trade = True
                        while trade:
                            print(Bag_Pok)
                            change1 = input("Which pokemon do you want to add to the pc?")
                            print(Bag_pc)
                            change2 = input("Which pokemon do you want to add on your team?")
                            if change1 in Bag_Pok and change2 in Bag_pc:
                                trade1 = change1
                                trade2 = change2
                                confirm = input("Do you really want to change?(Y/N)")
                                if confirm.upper() == "N":
                                    print("Oskey?!")
                                    x = input("Press enter...")
                                    trade = False
                                elif confirm.upper() == "Y":
                                    Do_it.change_team(trade1, trade2)
                                    x = input("Press enter...")
                                    print("Successful exchange!!")
                                    print(f"{trade1} is in your PC!")
                                    print(f"{trade2} is in your team!")
                                    show_change = ("You want to see your team?(Y/N)")
                                    if show_change.upper() == "N":
                                        print("Oskey?!")
                                        x = input("Press enter...")
                                        trade = False
                                    elif show_change.upper() == "Y":
                                        print(Bag_Pok)
                                        x = input("Press enter...")
                                        trade = False
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        trade = False
                                else:
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    trade = False
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                trade = False            
                    elif PC_action =="3":
                        PC_exit = input("You want to leave?(Y/N)")
                        if PC_exit.upper() == "N":
                            print("Oskey?!")
                            pass
                        elif PC_exit.upper() == "Y":
                            print("-- TURNING OFF --")
                            x = input("Press enter...")
                            pc_user = False                            
                    else:
                        print("INVALID!")
                        x = input("Press enter...")
                        pass
            else:
                print("INVALID!!")
                x = input("Press enter...")
                pass
        # elif lake_path.upper() == "2":
        elif lake_path.upper() == "3":
            store = input("Do you really want to go into the store?(Y/N)")
            if store.upper() == "N":
                print("Oskey?!")
                x = input("Press enter...")
                pass
            elif store.upper() == "Y":
                print("-- IN STORE --")
                x = input("Press enter...")
                print("Seller: Welcome to the North Shopping store!")
                x = input("Press enter...")
                print("Seller: Here you can buy and sell any item you want...")
                x = input("Press enter...")
                buy_sell = input("You want buy our sell anything?(Y/N)")
                if buy_sell.upper() == "N":
                    print("Oskey?!")
                    x = input("Press enter...")
                    pass
                elif buy_sell.upper() == "Y":
                    buy_store = True
                    while buy_store:
                        print("-- CHOOSE --")
                        print('''1 -- BUY POKEBALLS
2 -- BUY SPECIAL ITEMS
3 -- SELL ITEMS
9 -- EXIT''')
                        buy = input("Select 1, 2, 3 or 9:")
                        if buy == "9":
                            leave = input("You really want to leave?(Y/N)")
                            if leave.upper() == "Y":
                                print("LEAVING!!")
                                x = input("Press enter...")
                                buy_store = False
                            elif leave.upper() == "N":
                                print("Oskey?!")
                                x = input("Press enter...")
                                pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                        elif buy == "1":
                            if "Wallet" in Bag_Items:
                                buy_pokeball = True
                                while buy_pokeball:                                   
                                    print('''-- SELECT --
1 -- POKEBALL......... R$200 
2 -- GREATBALL........ R$400
3 -- ULTRABALL........ R$600
4 -- EXIT''')
                                    product = input("Select 1, 2, 3 or 4:")
                                    print(f"You have {Wallet} Cau coins!")
                                    if product == "1":
                                        quantidade = input("How many do you want?")
                                        if quantidade.isnumeric() > 0:
                                            valor = (int(quantidade) * 200)
                                            print(f"The price for {quantidade} Pokeballs is {valor}!")
                                            compra = input("Want to buy Pokeball?(Y/N)")
                                            if compra.upper() == "N":
                                                print("Oskey?!")
                                                x = input("Press enter...")
                                                pass
                                            elif compra.upper() == "Y":
                                                total = (Wallet - valor)
                                                if total < 0:
                                                    print("You don't have Cau coins enough!")
                                                    x = input("Press enter...")
                                                    pass
                                                else:
                                                    Wallet = total
                                                    print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                                                    print(f"{quantidade} Pokeball was added!")
                                                    for i in range(1, int(quantidade) + 1):
                                                        Bag_Items.append("Pokeball")
                                                    x = input("Press enter...")
                                                    buy_pokeball = False
                                            else:
                                                print("INVALID!!")
                                                x = input("Press enter...")
                                                pass
                                        elif quantidade == " ":
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass        
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass
                                    elif product == "2":
                                        quantidade = input("How many do you want?")
                                        if quantidade.isnumeric() > 0:
                                            valor = (int(quantidade) * 400)
                                            print(f"The price for {quantidade} Pokeballs is {valor}!")
                                            compra = input("Want to buy Greatball?(Y/N)")
                                            if compra.upper() == "N":
                                                print("Oskey?!")
                                                x = input("Press enter...")
                                                pass
                                            elif compra.upper() == "Y":
                                                total = (Wallet - valor)
                                                if total < 0:
                                                    print("You don't have Cau coins enough!")
                                                    x = input("Press enter...")
                                                    pass
                                                else:
                                                    Wallet = total
                                                    print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                                                    print(f"{quantidade} Pokeball was added!")
                                                    for i in range(1, int(quantidade) + 1):
                                                        Bag_Items.append("Pokeball")
                                                    x = input("Press enter...")
                                                    buy_pokeball = False
                                            else:
                                                print("INVALID!!")
                                                x = input("Press enter...")
                                                pass        
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass    
                                    elif product == "3":
                                        quantidade = input("How many do you want?")
                                        if quantidade.isnumeric() > 0:
                                            valor = (int(quantidade) * 600)
                                            print(f"The price for {quantidade} Pokeballs is {valor}!")
                                            compra = input("Want to buy Ultraball?(Y/N)")
                                            if compra.upper() == "N":
                                                print("Oskey?!")
                                                x = input("Press enter...")
                                                pass
                                            elif compra.upper() == "Y":
                                                total = (Wallet - valor)
                                                if total < 0:
                                                    print("You don't have Cau coins enough!")
                                                    x = input("Press enter...")
                                                    pass
                                                else:
                                                    Wallet = total
                                                    print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                                                    print(f"{quantidade} Pokeball was added!")
                                                    for i in range(1, int(quantidade) + 1):
                                                        Bag_Items.append("Pokeball")
                                                    x = input("Press enter...")
                                                    buy_pokeball = False
                                            else:
                                                print("INVALID!!")
                                                x = input("Press enter...")
                                                pass        
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass
                                    elif product == "4":
                                        run = input("You really want to leave?(Y/N)")
                                        if run.upper() == "Y":
                                            print("LEAVING!!")
                                            x = input("Press enter...")
                                            buy_store = False
                                        elif run.upper() == "N":
                                            print("Oskey?!")
                                            x = input("Press enter...")
                                            pass
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass    
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                        elif buy == "2":
                            buy_SuperRod = True
                            while buy_SuperRod:                                    
                                
                                print('''-- SELECT --
1 -- SUPER ROD........ R$200 
2 -- POTION........... R$100
3 -- EXIT''')
                                product = input("Select 1, 2 or 3:")
                                print(f"You have {Wallet} Cau coins!")
                                if product == "1":
                                    if "Super Rod" not in Bag_Items:
                                        buy_rod = input("Want to buy Super Rod?(Y/N)")
                                        if buy_rod.upper() == "Y":
                                            print(f"The price for Super Rod is R$400!")
                                            total = (Wallet - 400)
                                            if total < 0:
                                                print("You don't have Cau coins enough!")
                                                x = input("Press enter...")
                                                pass
                                            elif total > 0:
                                                Wallet = total
                                                print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                                                print("Super Rod was added!")
                                                Bag_Items.append("Super Rod")
                                                x = input("Press enter...")
                                                pass
                                            else:
                                                print("INVALID!!")
                                                x = input("Press enter...")
                                                pass
                                        elif buy_rod.upper() == "N":
                                            print("Oskey?!")
                                            x = input("Press enter...")
                                            pass        
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass
                                    elif "Super Rod" in Bag_Items:
                                        print("You already have a Super Rod!")
                                        x = input("Press enter...")
                                        pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif product == "2":
                                    quantidade = input("How many do you want?")
                                    if quantidade.isnumeric() > 0:
                                        valor = (int(quantidade) * 100)
                                        print(f"The price for {quantidade} Potions is {valor}!")
                                        compra = input("Want to buy Potion?(Y/N)")
                                        if compra.upper() == "N":
                                            print("Oskey?!")
                                            x = input("Press enter...")
                                            pass
                                        elif compra.upper() == "Y":
                                            total = (Wallet - valor)
                                            if total < 0:
                                                print("You don't have Cau coins enough!")
                                                x = input("Press enter...")
                                                pass
                                            else:
                                                Wallet = total
                                                print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                                                print(f"{quantidade} Potion was added!")
                                                for i in range(1, int(quantidade) + 1):
                                                    Bag_Items.append("Potion")
                                                x = input("Press enter...")
                                                buy_SuperRod = False
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass        
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass    
                                elif product == "3":
                                    run = input("You really want to leave?(Y/N)")
                                    if run.upper() == "Y":
                                        print("LEAVING!!")
                                        x = input("Press enter...")
                                        buy_SuperRod = False
                                    elif run.upper() == "N":
                                        print("Oskey?!")
                                        x = input("Press enter...")
                                        pass
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass    
                                else:
                                    print("INVALID!!")
                                    x = input("Press enter...")
                                    pass
                        elif buy == "3":
                            sell = input("Do you really want to sell items?(Y/N)")
                            if sell.upper() == "N":
                                print("Oskey?!")
                                x = input("Press enter...")
                                pass
                            elif sell.upper() == "Y":
                                sell_items = True
                                while sell_items:
                                    print('''-- SELLING --
1 -- POTION........... R$50
2 -- POKEBALL......... R$100 
3 -- GREATBALL........ R$200
4 -- ULTRABALL........ R$300
9 -- EXIT ''')
                                    see_items = input("Want to see your items?(Y/N)")
                                    if see_items.upper() == "N":
                                        print("Oskey?!")
                                        x = input("Press enter...")
                                        pass
                                    elif see_items.upper() == "Y":
                                        contador1 = 0
                                        contador2= 0
                                        contador3 = 0
                                        contador4 = 0        
                                        for i in Bag_Items:
                                            if i == "Potion":
                                                contador1 += 1
                                            elif i == "Pokeball":
                                                contador2 += 1
                                            elif i == "Greatball":
                                                contador3 += 1
                                            elif i == "Ultraball":
                                                contador4 += 1
                                        print(f"You have {contador1} Potion")
                                        print(f"You have {contador2} Pokeball")
                                        print(f"You have {contador3} Greatball")
                                        print(f"You have {contador4} Ultraball")
                                    else:
                                        print("INVALID!")
                                        x = input("Press enter...")
                                        pass
                                    start_sell = input("Select 1, 2, 3, 4, or 9:")
                                    sell_quant = input("How many do you want to sell:")
                                    if start_sell == "1":
                                        contador_Potion = 0
                                        if sell_quant.isnumeric() > 0:
                                            for i in Bag_Items:
                                                if i == "Potion":
                                                    contador_Potion += 1
                                            sell_conf = input("Do you really want to sell?(Y/N)")
                                            if sell_conf.upper() == "Y":
                                                if int(sell_quant) <= contador_Potion:
                                                    for i in range(1, int(sell_quant) + 1):
                                                        Bag_Items.remove("Potion")
                                                        Wallet + 50
                                                    total_potion = (int(sell_quant) * 50)
                                                    print(f"Item sold! You received {total_potion} Cau coins on your wallet!")
                                                    pass
                                                elif int(sell_quant) > contador_Potion:
                                                    print("You don't have enough Potions to sell!")
                                                    x = input("Press enter...")
                                                    pass
                                                else:
                                                    print("ERROR!")
                                                    x = input("Press enter...")
                                                    pass
                                            elif sell_conf.upper() == "N":
                                                print("Oskey?!")
                                                x = input("Press enter...")
                                                pass
                                            else:
                                                print("ERROR!")
                                                x = input("Press enter...")
                                                pass
                                        else:
                                            print("ERROR!")
                                            x = input("Press enter...")
                                            pass
                                    elif start_sell == "2":
                                        contador_Pokeball = 0
                                        if sell_quant.isnumeric() > 0:
                                            for i in Bag_Items:
                                                if i == "Pokeball":
                                                    contador_Pokeball += 1
                                            sell_conf = input("Do you really want to sell?(Y/N)")
                                            if sell_conf.upper() == "Y":
                                                if int(sell_quant) <= contador_Pokeball:
                                                    for i in range(1, int(sell_quant) + 1):
                                                        Bag_Items.remove("Pokeball")
                                                        Wallet + 100
                                                    total_potion = (int(sell_quant) * 100)
                                                    print(f"Item sold! You received {total_potion} Cau coins on your wallet!")
                                                    pass
                                                elif int(sell_quant) > contador_Pokeball:
                                                    print("You don't have enough Pokeball to sell!")
                                                    x = input("Press enter...")
                                                    pass
                                                else:
                                                    print("ERROR!")
                                                    x = input("Press enter...")
                                                    pass
                                            elif sell_conf.upper() == "N":
                                                print("Oskey?!")
                                                x = input("Press enter...")
                                                pass
                                            else:
                                                print("ERROR!")
                                                x = input("Press enter...")
                                                pass
                                        else:
                                            print("ERROR!")
                                            x = input("Press enter...")
                                            pass
                                    elif start_sell == "3":
                                        contador_Greatball = 0
                                        if sell_quant.isnumeric() > 0:
                                            for i in Bag_Items:
                                                if i == "Greatball":
                                                    contador_Greatball += 1
                                            sell_conf = input("Do you really want to sell?(Y/N)")
                                            if sell_conf.upper() == "Y":
                                                if int(sell_quant) <= contador_Greatball:
                                                    for i in range(1, int(sell_quant) + 1):
                                                        Bag_Items.remove("Greatball")
                                                        Wallet + 200
                                                    total_potion = (int(sell_quant) * 200)
                                                    print(f"Item sold! You received {total_potion} Cau coins on your wallet!")
                                                    pass
                                                elif int(sell_quant) > contador_Greatball:
                                                    print("You don't have enough Greatball to sell!")
                                                    x = input("Press enter...")
                                                    pass
                                                else:
                                                    print("ERROR!")
                                                    x = input("Press enter...")
                                                    pass
                                            elif sell_conf.upper() == "N":
                                                print("Oskey?!")
                                                x = input("Press enter...")
                                                pass
                                            else:
                                                print("ERROR!")
                                                x = input("Press enter...")
                                                pass
                                        else:
                                            print("ERROR!")
                                            x = input("Press enter...")
                                            pass
                                    elif start_sell == "4":
                                        contador_Ultraball = 0
                                        if sell_quant.isnumeric() > 0:
                                            for i in Bag_Items:
                                                if i == "Ultraball":
                                                    contador_Ultraball += 1
                                            sell_conf = input("Do you really want to sell?(Y/N)")
                                            if sell_conf.upper() == "Y":
                                                if int(sell_quant) <= contador_Ultraball:
                                                    for i in range(1, int(sell_quant) + 1):
                                                        Bag_Items.remove("Ultraball")
                                                        Wallet + 300
                                                    total_potion = (int(sell_quant) * 300)
                                                    print(f"Item sold! You received {total_potion} Cau coins on your wallet!")
                                                    pass
                                                elif int(sell_quant) > contador_Ultraball:
                                                    print("You don't have enough Ultraball to sell!")
                                                    x = input("Press enter...")
                                                    pass
                                                else:
                                                    print("ERROR!")
                                                    x = input("Press enter...")
                                                    pass
                                            elif sell_conf.upper() == "N":
                                                print("Oskey?!")
                                                x = input("Press enter...")
                                                pass
                                            else:
                                                print("ERROR!")
                                                x = input("Press enter...")
                                                pass
                                        else:
                                            print("ERROR!")
                                            x = input("Press enter...")
                                            pass
                                    elif start_sell == "9":
                                        sell_exit = input("Do you really want to leave?(Y/N)")
                                        if sell_exit.upper() == "N":
                                            print("Oskey?!")
                                            x = input("Press enter...")
                                            pass
                                        elif sell_exit.upper() == "Y":
                                            print("-- RETURNING --")
                                            x = input("Press enter...")
                                            sell_items = False
                                        else:
                                            print("ERROR!")
                                            x = input("Press enter...")
                                            pass
                                    else:
                                        print("ERROR!")
                                        x = input("Press enter...")
                                        pass
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass                    
                else:
                    print("INVALID!!")
                    x = input("Press enter...")
                    pass
            else:
                print("INVALID!!")
                x = input("Press enter...")
                pass
                


        # elif lake_path.upper() == "4":
        # elif lake_path.upper() == "5":




                


    


    

       
        
