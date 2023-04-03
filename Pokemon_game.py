import Function
import random
import vantagenspoke

class Player:
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age
        
    
    def get_information(self):
        return (f"NAME: {nome_jogador}, AGE: {idade_jogador}, GENDER: {jogador}")
    
    def set_name(self, new_name):
        self.name = new_name
        return new_name

Penny_team1 = [vantagenspoke.poke007,vantagenspoke.poke016,vantagenspoke.poke056]
Penny_fainted = []
Penny_team2 = []
Peny_fainted2 = []
Bag_Pok = []
Bag_fainted = []
Bag_Items = []
Bag_badges = []
gym_badges = []
Bag_pc = []
kripke_team = [vantagenspoke.poke013, vantagenspoke.poke014,vantagenspoke.poke010]
kripke_fainted = []
stuart_team = [vantagenspoke.poke004,vantagenspoke.poke037,vantagenspoke.poke058]
stuart_fainted = []
howard_team = [vantagenspoke.poke054,vantagenspoke.poke060,vantagenspoke.poke072]
howard_fainted = []
raj_team = [vantagenspoke.poke043,vantagenspoke.poke069,vantagenspoke.poke102]
raj_fainted = []
leonard_team = [vantagenspoke.poke052, vantagenspoke.poke084, vantagenspoke.poke039]
leonard_fainted = []
sheldon_team = [vantagenspoke.poke063,vantagenspoke.poke096]
sheldon_fainted = []

gym1_team = [vantagenspoke.poke114, vantagenspoke.poke111, vantagenspoke.poke095]
gym1_fainted = []
gym2_team = [vantagenspoke.poke093, vantagenspoke.poke083, vantagenspoke.poke077]
gym2_fainted = []
gym3_team = [vantagenspoke.poke083, vantagenspoke.poke067, vantagenspoke.poke061]
gym3_fainted = []
gym4_team = [vantagenspoke.poke061, vantagenspoke.poke070, vantagenspoke.poke075]
gym4_fainted = []

dad_team = [vantagenspoke.poke128, vantagenspoke.poke115 , vantagenspoke.poke113, vantagenspoke.poke108, vantagenspoke.poke085]
dad_fainted = []

Wallet = 5000

jogador = ""
nome_jogador = ""
Game = True
while Game:
    
    gender_conf = True
    while gender_conf:
        print("Press B(BOY) or G(GIRL)!")
        ask_Tipo = input("Chose your Gender:")   
        if ask_Tipo.upper() == "B":
            jogador = "Boy"
            gender_conf = False
        elif ask_Tipo.upper() == "G":
            jogador = "Girl"
            gender_conf = False
        else:
            print("INVALID ANSWER!!!")
            print("TRY AGAIN!!")
            pass
    age_conf = True
    while age_conf:    
        age_jogador = input("What's your age?")
        if age_jogador.isnumeric():
            if int(age_jogador) < 100:
                idade_jogador = age_jogador
                age_conf = False
            elif int(age_jogador) > 100:
                print("INVALID AGE!!")
                print("TRY AGAIN!!")
                pass
            else:
                pass
        else:
            print("INVALID ANSWER!!!")
            print("TRY AGAIN!!")
            pass


    nome_jogador = input("What's the player name?")
        
    while True:
        
        nome_confirmacao = input(f"Your name is {nome_jogador}?(Y/N)")

        if nome_confirmacao.upper() == "Y":
            break
        elif nome_confirmacao.upper() == "N":
            nome_jogador = input("What's your name:")
        else: 
            print("INVALID ANSWER!!!")
            


    player1 = Player(jogador,nome_jogador,idade_jogador)
    x = input("You want to see your informations?(Y/N)")
    if x.upper() == "Y":
        print(player1.get_information())
        pass
    elif x.upper() == "N":
        print("Oskey?!")
        pass
        

    partner = True
    while partner:
        Function.linha()
        print('''CHOSE YOUR PATH!!
1 -- GO TO LABORATORY 
2 -- TALK TO MOM
3 -- GO TO ROOM''')
        Function.linha()
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
                                        Bag_Pok.append(vantagenspoke.poke004)
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
                                        Bag_Pok.append(vantagenspoke.poke007)
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
                                        Bag_Pok.append(vantagenspoke.poke001)
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
            if jogador == "Boy":
                print("Hey son, where are you going?")
                x = input("Press enter...")
                print("I know, we just moved and you want to explore the city, ain't it?")
                x = input("Press enter...")
                print("So take care, are many wild Pokemons out there!!")
                x = input("Press enter...")
                print("Bye baby, hurry up!!")
                pass
            elif jogador == "Girl":
                print("Hey daughter, where are you going?")
                x = input("Press enter...")
                print("I know, we just moved and you want to explore the city, ain't it?")
                x = input("Press enter...")
                print("So take care, are many wild Pokemons out there!!")
                x = input("Press enter...")
                print("Bye baby, hurry up!!")
                pass
            else:
                print("ERROR!")
                x = input("Press enter...")
                pass    

        elif path_jogador == "3":
            print("YOU: It's just my room, nothing important...")
            x = input("Press enter...")
            print("YOU: Oh my PC, maybe there have some important thing...")
            computer = input("Look your PC?(Y/N)")
            if computer.upper() == "Y":
                if "Potion" not in Bag_Items:
                    print("YOU: Let's see... Oh look i have one potion!!")
                    take_potion = input("Take the potion?(Y/N)")
                    if take_potion.upper() == "Y":
                        if "Potion" not in Bag_Items:
                            print("YOU: I gonna take it!!")
                            Bag_Items.append("Potion")
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
                elif "Potion" in Bag_Items:
                    print("YOU: Let's see... Nothing here!")
                    x = input("Press enter...")
                    pass
                else:
                    print("ERROR!")
                    x = input("Press enter...")
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
    print("MOM: Hey i almost forgot, take it... ")
    x = input("Press enter...")
    print("MOM: You will need this on your journey...")
    Bag_Items.append("Wallet")
    x = input("Press enter...")
    print("-- YOU RECIEVED 5000 CAU COINS --")
    x = input("Press enter...")
    print("MOM: Your journey start now, go ahead!")
    x = input("Press enter...")
    print("-- GOING OUT SIDE --")
    
    
    start_journey = True
    while start_journey:

        Function.linha()    
        print('''CHOSE YOUR PATH!!
1 -- GO TO HOUSE 085
2 -- TALK WITH MAYOR
3 -- GO TO ROUTE 222''')
        Function.linha()
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
                    if "Pokeball" not in Bag_Pok:
                        print("Traveler: Greatful, take these Pokeball you will not regret it!")
                        for i in range(1, 11):
                            Bag_Items.append("Pokeball")
                        print("-- YOU ADDED POKEBALLS ON YOUR BAG --")
                        print("YOU: This Pokeballs will help me a lot!!")
                        pass
                    else:
                        print("You already take it...")
                        x = input("Press enter...")
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
                            Function.linha()
                            print('''-- SELECT THE ACTION --
1 -- BUSH 1
2 -- BUSH 2
3 -- BUSH 3
4 -- BUSH 4
9 -- TO EXIT THE BUSHES''')
                            Function.linha()
                            action_bushes = input("Selec your action:")
                            if action_bushes == "1":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                found = (Function.found_bush())
                                if found == "Nothing here...":
                                    print(f"{found}")
                                    pass
                                elif found!= "Nothing here...": 
                                    print(f"You found {found.name}!")
                                    capture = input(f"Try to cath {found.name}?(Y/N)")
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
                                                        print(f"Gotcha!! The {found.name} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False
                                else:
                                    print("Invalid!!")
                                    input("Press enter...")
                                    pass
                            elif action_bushes == "2":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                found = (Function.found_bush())
                                if found == "Nothing here...":
                                    print(f"{found}")
                                    pass
                                elif found!= "Nothing here...": 
                                    print(f"You found {found.name}!")
                                    capture = input(f"Try to cath {found.name}?(Y/N)")
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
                                                        print(f"Gotcha!! The {found.name} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False
                                else:
                                    print("Invalid!!")
                                    input("Press enter...")
                                    pass                            
                            elif action_bushes == "3":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                found = (Function.found_bush())
                                if found == "Nothing here...":
                                    print(f"{found}")
                                    pass
                                elif found!= "Nothing here...": 
                                    print(f"You found {found.name}!")
                                    capture = input(f"Try to cath {found.name}?(Y/N)")
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
                                                        print(f"Gotcha!! The {found.name} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False
                                else:
                                    print("Invalid!!")
                                    input("Press enter...")
                                    pass
                            elif action_bushes == "4":
                                print("Entering the bush...")
                                x = input("Press enter...")
                                found = (Function.found_bush())
                                if found == "Nothing here...":
                                    print(f"{found}")
                                    pass
                                elif found!= "Nothing here...": 
                                    print(f"You found {found.name}!")
                                    capture = input(f"Try to cath {found.name}?(Y/N)")
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
                                                        print(f"Gotcha!! The {found.name} was added on your list.")
                                                        Bag_Pok.append(found)
                                                        Bag_Items.remove("Pokeball")
                                                        catch = False
                                            else:
                                                print("You don't have enough Pokeball...")
                                                catch = False
                                else:
                                    print("Invalid!!")
                                    input("Press enter...")
                                    pass
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
            print("INVALID!!")
            x = input("Press enter...")
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
        Function.linha()
        print('''-- CHOOSE YOUR PATH!! --
1 -- UPA
2 -- GO TO HARBOR
3 -- NORTH SHOPPING STORE
4 -- BATTLE ARENA 
5 -- BLACK GATE''')
        Function.linha()
        lake_path = input("Select your path 1, 2, 3, 4 or 5:")
        if lake_path == "1":
            print("-- ENTERING UPA --")
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
                    Function.linha()
                    print('''-- SELECT AN ACTION --
1 -- SEE YOUR POKEMONS
2 -- CHANGE YOUR TEAM
3 -- HEAL YOUR POKEMON
4 -- EXIT PC''')
                    Function.linha()
                    PC_action = input("Select 1, 2, 3 or 4:")
                    if PC_action == "1":
                        see_team = True
                        while see_team:
                            Function.linha()
                            print('''-- SELECT --
1 -- SEE YOUR TEAM
2 -- SEE YOUR STORED POKEMONS
3 -- RETURN''')
                            Function.linha()
                            PC_action2 = input("Select 1, 2 or 3:")
                            if PC_action2 == "1":
                                contador = 0
                                for i in Bag_Pok:
                                    contador += 1
                                    print(i.name)
                                x = input("Press enter...")
                                pass
                            elif PC_action2 == "2":
                                contador = 0
                                for i in Bag_Pok:
                                    contador += 1
                                    print(i.name)
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
                                    Function.change_team(trade1, trade2)
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
                    elif PC_action == "3":
                        heal = input("You want to heal all your Pokemons?(Y/N)")
                        if heal.upper() == "N":
                            print("Oskey?!")
                            x = input("Press enter...")
                            pass
                        elif heal.upper() == "Y":
                            print("NURSE JOY: Wait a second.")
                            x = input("Press enter...")
                            print("Healing...")
                            contador_team = 0
                            for i in Bag_fainted:
                                Bag_Pok.append(i)
                                contador_team += 1
                                print(f"{contador_team} -- {i.name} Is Healed!")
                            x = input("Press enter...")
                            pass
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif PC_action =="4":
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
        
        elif lake_path == "2":
            if "Super Rod" in Bag_Items:
                print("-- IN HARBOR --")
                print("YOU: So this is the Tabapua Harbor!")
                x = input("Press enter...")
                print("-- Sailor Approaches --")
                x = input("Press enter...")
                ask_sailor = input("Sailor: Hey you, are you a trainer Pokemon?(Y/N)")
                if ask_sailor.upper() == "N":
                    print("Sailor: Ok, so it's not you the captain is looking for...")
                    x = input("Press enter...")
                    print("Sailor: Go away, your place is not here!")
                    x = input("Press enter...")
                    pass
                elif ask_sailor.upper() == "Y":
                    print("Sailor: So are you who the captain is looking for...")
                    x = input("Press enter...")
                    print("Sailor: The captain, was waiting for the trainer sent by Prf. Tarik...")
                    x = input("Press enter...")
                    print("Sailor: I think is you, come with me...")
                    x = input("Press enter...")
                    print("-- IN CAPTAIN'S OFFICE --")
                    x = input("Press enter...")
                    ask_captain = input(f"CAPTAIN: Hey, your name is {player1.name}?(Y/N)")
                    if ask_captain.upper() == "N":
                        print("CAPTAIN: So you are not who i'm looking for!")
                        x = input("Press enter...")
                        print("CAPTAIN: I'll keeping waiting...")
                        x = input("Press enter...")
                        pass
                    elif ask_captain.upper() == "Y":
                        print("CAPTAIN: I see, Prf. Tarik said you would come...")
                        x = input("Press enter...")
                        print("CAPTAIN: Prf. Tarik ask me for help on your research...")
                        x = input("Press enter...")
                        print("CAPTAIN: Here on Tabapua Lake...")
                        x = input("Press enter...")
                        print("CAPTAIN: And told me that you would come...")
                        x = input("Press enter...")
                        ask_research = input("Will you come with me by boat across the lake?(Y/N)")
                        if ask_research.upper() == "N":
                            print("CAPTAIN: Oh, maybe other time, i'll waiting for you...")
                            x = input("Press enter...")
                            pass
                        elif ask_research.upper() == "Y":
                            print("CAPTAIN: Wonderful, let's start our adventure across the lake!")
                            x = input("Press enter...")
                            print("CAPTAIN: Take you Super Rod and follow me...")
                            x = input("Press enter...")
                            print("CAPTAIN: Try to catch as many Pokemons as you can!")
                            x = input("Press enter...")
                            print("-- ENTERING IN THE BOAT --")
                            x = input("Press enter...")
                            on_boat = True
                            while on_boat:
                                print("-- IN THE TABAPUA LAKE --")
                                Function.linha()
                                print('''-- CHOOSE --
1 -- USE THE SUPER ROD IN LEFT SIDE
2 -- USE THE SUPER ROD IN RIGHT SIDE
3 -- USE THE SUPER ROD ON THE BOAT'S PROW
4 -- CAME BAKE TO HARBOR''')
                                Function.linha()
                                do_boat = input("Select 1, 2, 3 or 4:")
                                if do_boat in ("1", "2", "3"):
                                    print("Using Super Rod...")
                                    x = input("Press enter...")
                                    find = (Function.found_lake())
                                    if find != "Nothing here...":
                                        ask_catch = input(f"Try catch {find.name}?(Y/N)")
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
                                                                print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                                Bag_pc.append(find)
                                                                trhow_ball = False
                                                            elif len(Bag_Pok) <= 6:
                                                                print(f"Gotcha! {find.name} was captured and added on your team!")
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
                                                                print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                                Bag_pc.append(find)
                                                                trhow_ball = False
                                                            elif len(Bag_Pok) <= 6:
                                                                print(f"Gotcha! {find.name} was captured and added on your team!")
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
                                                            print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                            Bag_pc.append(find)
                                                            trhow_ball = False
                                                        elif len(Bag_Pok) <= 6:
                                                            print(f"Gotcha! {find.name} was captured and added on your team!")
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
                                                elif wich_ball == "0":
                                                    run = input("You want to run?(Y/N)")
                                                    if run.upper() == "N":
                                                        print("Oskey?!")
                                                        x = input("Press enter...")
                                                        pass
                                                    elif run.upper() == "Y":
                                                        print("Runing away...")
                                                        x = input("Press enter...")
                                                        trhow_ball = False
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
                                        print("-- IN HARBOR --")
                                        x = input("Press enter...")
                                        if "Battle Ticket" not in Bag_Items:
                                            print("CAPTAIN: I'ts the end of our adventure in Tabapua lake...")
                                            x = input("Press enter...")
                                            print("CAPTAIN: You need to go ahead with your journey...")
                                            x = input("Press enter...")
                                            print("CAPTAIN: Best of luck with it...")
                                            x = input("Press enter...")
                                            print("CAPTAIN: Oh wait. i almost forgot...")
                                            x = input("Press enter...")
                                            print("CAPTAIN: Take this, a Battle Ticket!")
                                            x = input("Press enter...")
                                            print("CAPTAIN: You need this to enter in Battle Arena!")
                                            x = input("Press enter...")
                                            print("CAPTAIN: I think you could win this challenge...")
                                            Bag_Items.append("Battle Ticket")
                                            x = input("Press enter...")
                                            on_boat = False
                                        else:
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
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass
                else:
                    print("INVALID!!")
                    x = input("Press enter...")
                    pass        
            elif "Super Rod" not in Bag_Items:
                print("You will need a Super Rod to enter in Harbor!")
                x = input("Press enter...")
                pass
            else:
                print("INVALID!!")
                x = input("Press enter...")
                pass
        
        elif lake_path == "3":
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
                        Function.linha()
                        print('''1 -- BUY POKEBALLS
2 -- BUY SPECIAL ITEMS
3 -- SELL ITEMS
9 -- EXIT''')
                        Function.linha()
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
                                    Function.linha()                                   
                                    print('''-- SELECT --
1 -- POKEBALL......... R$200 
2 -- GREATBALL........ R$400
3 -- ULTRABALL........ R$600
4 -- EXIT''')
                                    Function.linha()
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
                                                    pass
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
                                            print(f"The price for {quantidade} Greatball is {valor}!")
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
                                                    print(f"{quantidade} Greatball was added!")
                                                    for i in range(1, int(quantidade) + 1):
                                                        Bag_Items.append("Greatball")
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
                                    elif product == "3":
                                        quantidade = input("How many do you want?")
                                        if quantidade.isnumeric() > 0:
                                            valor = (int(quantidade) * 600)
                                            print(f"The price for {quantidade} Ultraball is {valor}!")
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
                                                    print(f"{quantidade} Ultraball was added!")
                                                    for i in range(1, int(quantidade) + 1):
                                                        Bag_Items.append("Ultraball")
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
                                    elif product == "4":
                                        run = input("You really want to leave?(Y/N)")
                                        if run.upper() == "Y":
                                            print("LEAVING!!")
                                            x = input("Press enter...")
                                            buy_pokeball = False   
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
                                Function.linha()
                                print('''-- SELECT --
1 -- SUPER ROD........ R$200 
2 -- POTION........... R$100
3 -- EXIT''')
                                Function.linha()
                                product = input("Select 1, 2 or 3:")
                                print(f"You have {Wallet} Cau coins!")
                                if product == "1":
                                    if "Super Rod" not in Bag_Items:
                                        buy_rod = input("Want to buy Super Rod?(Y/N)")
                                        if buy_rod.upper() == "Y":
                                            print(f"The price for Super Rod is R$200!")
                                            total = (Wallet - 200)
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
                                    Function.linha()
                                    print('''-- SELLING --
1 -- POTION........... R$50
2 -- POKEBALL......... R$100 
3 -- GREATBALL........ R$200
4 -- ULTRABALL........ R$300
9 -- EXIT ''')
                                    Function.linha()
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
                
        elif lake_path == "4":
            print("-- IN BATTLE ARENA --")
            x = input("Press enter...")
            if "Battle Ticket" in Bag_Items:
                if "Penny's Fight" not in Bag_badges:   
                    print("YOU: So, this is the Battle Arena?!")
                    x = input("Press enter...")
                    print("YOU: I think this can be a interesting thing...")
                    x = input("Press enter...")
                    print("-- SOMEONE CALLS --")
                    x = input("Press enter...")
                    print(f"PENNY: Hey you, you are the {player1.name}?")
                    x = input("Press enter...")
                    print("PENNY: So thats you, what are you doing here...")
                    x = input("Press enter...")
                    print("PENNY: This tournmet is only to great Pokemon Trainers...")
                    x = input("Press enter...")
                    print("PENNY: Whatever i don't think you will won this...")
                    x = input("Press enter...")
                    print("PENNY: What do you think, let's battle?")
                    x = input("Press enter...")
                    print("PENNY: I want to train little bit before the tournment...")
                    x = input("Press enter...")
                    print("PENNY: Although I think you won't do much good...")
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
                                    print(f"{contador_team} -- {i.name} -- {i.elemento}")
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
                                                Penny_battle = False
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
                                                Penny_battle = False
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
                                            print(f"{contador_fight} -- {i.name} -- {i.elemento}")
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
                                            print(f"{contador_fight2} -- {i.name} -- {i.elemento}")
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
                                            print(f"{contador_fight3} -- {i.name} -- {i.elemento}")
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
                                            print(f"{contador_fight4} -- {i.name} -- {i.elemento}")
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
                                            print(f"{contador_fight5} -- {i.name} -- {i.elemento}")
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
                                            print(f"{contador_fight6} -- {i.name} -- {i.elemento}")
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
                                                        print("You know are a Champion!")
                                                        x = input("Press enter...")
                                                        print("You recieved a Black key!")
                                                        x = input("Press enter...")
                                                        print("YOU: What door this key can open?")
                                                        x = input("Press enter...")                                                            
                                                        print("You Won!!")
                                                        Bag_Items.append("Black Key")
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
            elif "Battle Ticket" not in Bag_Items:
                print("-- YOU CAN'T ENTER HERE --")
                x = input("Press enter...")
                print("To enter here you need a Battle Ticket!")
                x = input("Press enter...")
                pass  
            
        elif lake_path == "5":
            if "Black Key" not in Bag_Items:
                print("YOU: What a giant gate...")
                x = input("Press enter...")
                print("YOU: I think i gonna need a key to enter...")
                x = input("Press enter...")
                print("YOU: Where can i find it?")
                x = input("Press enter...")
                pass
            elif "Black Key" in Bag_Items:
                print("YOU: With this key, i think i can use it...")
                x = input("Press enter...")
                print("-- THE GATE OPENS --")
                x = input("Press enter...")
                print(f"MAYOR VALIM: Hey {player1.name} i knew i would see you again!")
                x = input("Press enter...")
                print("MAYOR VALIM: But of corse i would see, you are the winner...")
                x = input("Press enter...")
                print("MAYOR VALIM: I came here to give you all awards of Battle Arena!")
                x = input("Press enter...")
                print("MAYOR VALIM: The first of all, the cash award!")
                x = input("Press enter...")
                print("MAYOR VALIM: You just got 10000 Cau coins on your wallet!")
                Wallet + 10000
                x = input("Press enter...")
                print("MAYOR VALIM: The second award is a Masterball!")
                x = input("Press enter...")
                print("MAYOR VALIM: It can capture any pokemon at first!")
                Bag_Items.append("Masterball")
                x = input("Press enter...")
                print("MAYOR VALIM: In third, you jus won 10 of all the three types of Pokeball!")
                for i in range(1,11):
                    Bag_Items.append("Pokeball")
                for i in range(1,11):
                    Bag_Items.append("Greatball")
                for i in range(1,11):
                    Bag_Items.append("Ultraball")
                x = input("Press enter...")
                print("MAYOR VALIM: And at last but not least, here a Ticket for your journey...")
                x = input("Press enter...")
                print("MAYOR VALIM: This ticket is for the Vitoria's Bus, to help you to arrive in Fortal City!")
                x = input("Press enter...")
                print("MAYOR VALIM: And that's all, best of look on your journey!")
                x = input("Press enter...")
                lake_journey = False

    print("-- ARRIVING IN FORTAL CITY --")
    print("YOU: So this is Fortal City?!")
    x = input("Press enter...")
    print("YOU: What a big city...")
    x = input("Press enter...")
    print("YOU: Well, can i found my dad in this madness?")
    x = input("Press enter...")
    print("YOU: I'll only know if i try...")
    x = input("Press enter...")
    print("YOU: Let's do it!")
    
    fortal_journey = True
    while fortal_journey:
        print("-- IN FORTAL CITY --")
        Function.linha()
        print('''-- CHOOSE YOUR PATH --
1 -- BUSHES OF COCÓ
2 -- RIO MAR SHOPPING
3 -- UPA
4 -- FORTAL GYM
5 -- CRUSH'S BEACH ''')
        Function.linha()
        fortal_path = input("Select path 1, 2, 3, 4 or 5:")
        if fortal_path == "1":
            on_beach = True
            while on_beach:
                print("-- IN THE TABAPUA LAKE --")
                Function.linha()
                print('''-- CHOOSE --
1 -- COCÓ'S BUSH
2 -- COCÓ'S BUSH
3 -- COCÓ'S BUSH
4 -- COCÓ'S BUSH
9 -- EXIT''')
                Function.linha()
                do_bush = input("Select 1, 2, 3, 4 or 9:")
                if do_bush in ("1", "2", "3", "4"):
                    print("Using Super Rod...")
                    x = input("Press enter...")
                    find = (Function.coco1_bush())
                    if find != "Nothing here...":
                        ask_catch = input(f"Try catch {find.name}?(Y/N)")
                        if ask_catch.upper() == "N":
                            print("Oskey?!")
                            x = input("Press enter...")
                            pass
                        elif ask_catch.upper() == "Y":
                            trhow_ball2 = True
                            while trhow_ball2:
                                contador2 = 0
                                contador3 = 0
                                contador4 = 0
                                contador5 = 0        
                                for i in Bag_Items:
                                    if i == "Pokeball":
                                        contador2 += 1
                                    elif i == "Greatball":
                                        contador3 += 1
                                    elif i == "Ultraball":
                                        contador4 += 1
                                    elif i == "Masterball":
                                        contador5 += 1
                                print(f"You have {contador2} Pokeball")
                                print(f"You have {contador3} Greatball")
                                print(f"You have {contador4} Ultraball")
                                print(f"You have {contador5} Masterball")
                                wich_ball = input("Wich ball you want to use?(Press 0 to run)")
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
                                                print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                Bag_pc.append(find)
                                                trhow_ball2 = False
                                            elif len(Bag_Pok) <= 6:
                                                print(f"Gotcha! {find.name} was captured and added on your team!")
                                                Bag_Pok.append(find)
                                                trhow_ball2 = False
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
                                                print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                Bag_pc.append(find)
                                                trhow_ball2 = False
                                            elif len(Bag_Pok) <= 6:
                                                print(f"Gotcha! {find.name} was captured and added on your team!")
                                                Bag_Pok.append(find)
                                                trhow_ball2 = False
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
                                            print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                            Bag_pc.append(find)
                                            trhow_ball2 = False
                                        elif len(Bag_Pok) <= 6:
                                            print(f"Gotcha! {find.name} was captured and added on your team!")
                                            Bag_Pok.append(find)
                                            trhow_ball2 = False
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass   
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif wich_ball.upper() == "MASTERBALL":
                                    if len(Bag_Pok) >= 6:
                                            print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                            Bag_pc.append(find)
                                            trhow_ball2 = False
                                    elif len(Bag_Pok) <= 6:
                                        print(f"Gotcha! {find.name} was captured and added on your team!")
                                        Bag_Pok.append(find)
                                        trhow_ball2 = False
                                    else:
                                        print("INVALID!!")
                                        x = input("Press enter...")
                                        pass
                                elif wich_ball == "0":
                                    run = input("You want to run?(Y/N)")
                                    if run.upper() == "N":
                                        print("Oskey?!")
                                        x = input("Press enter...")
                                        pass
                                    elif run.upper() == "Y":
                                        print("Runing away...")
                                        x = input("Press enter...")
                                        trhow_ball2 = False
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
                    elif find == "Nothing here...":
                        print("You find nothing...")
                        x = input("Press enter...")
                        pass
                    else:
                        print("INVALID!!")
                        x = input("Press enter...")
                        pass
                elif do_bush == "9":
                    do_exit = input("Want to leave the bush?(Y/N)")
                    if do_exit.upper() == "N":
                        print("Oskey?!")
                        x = input("Press enter...")
                        pass
                    elif do_exit.upper() == "Y":
                        print("Leaving...")
                        x = input("Press enter...")
                        on_beach = False
        
        elif fortal_path == "2":
            store1 = input("Do you really want to go into the store?(Y/N)")
            if store1.upper() == "N":
                print("Oskey?!")
                x = input("Press enter...")
                pass
            elif store1.upper() == "Y":
                print("-- IN STORE --")
                x = input("Press enter...")
                print("Seller: Welcome to the Rio Mar store!")
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
                        Function.linha()
                        print('''1 -- BUY POKEBALLS
2 -- BUY SPECIAL ITEMS
3 -- SELL ITEMS
9 -- EXIT''')
                        Function.linha()
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
                                    Function.linha()                                   
                                    print('''-- SELECT --
1 -- POKEBALL......... R$200 
2 -- GREATBALL........ R$400
3 -- ULTRABALL........ R$600
4 -- EXIT''')
                                    Function.linha()
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
                                            print(f"The price for {quantidade} Greatball is {valor}!")
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
                                                    print(f"{quantidade} Greatball was added!")
                                                    for i in range(1, int(quantidade) + 1):
                                                        Bag_Items.append("Greatball")
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
                                            print(f"The price for {quantidade} Ultraball is {valor}!")
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
                                                    print(f"{quantidade} Ultraball was added!")
                                                    for i in range(1, int(quantidade) + 1):
                                                        Bag_Items.append("Ultraball")
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
                                Function.linha()                                    
                                print('''-- SELECT --
1 -- SUPER ROD........ R$200 
2 -- POTION........... R$100
3 -- EXIT''')
                                Function.linha()
                                product = input("Select 1, 2 or 3:")
                                print(f"You have {Wallet} Cau coins!")
                                if product == "1":
                                    if "Super Rod" not in Bag_Items:
                                        buy_rod = input("Want to buy Super Rod?(Y/N)")
                                        if buy_rod.upper() == "Y":
                                            print(f"The price for Super Rod is R$200!")
                                            total = (Wallet - 200)
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
                                    Function.linha()
                                    print('''-- SELLING --
1 -- POTION........... R$50
2 -- POKEBALL......... R$100 
3 -- GREATBALL........ R$200
4 -- ULTRABALL........ R$300
9 -- EXIT ''')
                                    Function.linha()
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
        
        elif fortal_path == "3":
            print("-- ENTERING UPA --")
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
                    Function.linha()
                    print('''-- SELECT AN ACTION --
1 -- SEE YOUR POKEMONS
2 -- CHANGE YOUR TEAM
3 -- HEAL YOUR POKEMON
4 -- EXIT PC''')
                    Function.linha()
                    PC_action = input("Select 1, 2 or 3:")
                    if PC_action == "1":
                        see_team = True
                        while see_team:
                            Function.linha()
                            print('''-- SELECT --
1 -- SEE YOUR TEAM
2 -- SEE YOUR STORED POKEMONS
3 -- RETURN''')
                            Function.linha()
                            PC_action2 = input("Select 1, 2 or 3:")
                            if PC_action2 == "1":
                                contador = 0
                                for i in Bag_Pok:
                                    contador += 1
                                    print(f"{contador}--{i.name}")
                                x = input("Press enter...")
                                pass
                            elif PC_action2 == "2":
                                contador = 0
                                for i in Bag_pc:
                                    contador += 1
                                    print(f"{contador}--{i.name}")
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
                                    Function.change_team(trade1, trade2)
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
                    elif PC_action == "3":
                        heal = input("You want to heal all your Pokemons?(Y/N)")
                        if heal.upper() == "N":
                            print("Oskey?!")
                            x = input("Press enter...")
                            pass
                        elif heal.upper() == "Y":
                            print("NURSE JOY: Wait a second.")
                            x = input("Press enter...")
                            print("Healing...")
                            contador_team = 0
                            for i in Bag_fainted:
                                Bag_Pok.append(i)
                                contador_team += 1
                                print(f"{contador_team} -- {i.name} Is Healed!")
                            x = input("Press enter...")
                            pass
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif PC_action =="4":
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
        
        elif fortal_path == "4":
            gym = True
            while gym:
                if len(Bag_Pok) <= 0:
                    print("Your Pokemons are fainted...")
                    x = input("Press enter...")
                    print("Go to upa and recover them!")
                    x = input("Press enter...")
                    pass
                elif len(Bag_Pok) > 0:
                    print("-- IN FORTAL GYM --")
                    x = input("Press enter...")
                    Function.linha()
                    gym_select = input('''-- CHOOSE GYM PATH --
1 -- CAPTAIN WAGNER
2 -- JOSEPH SARTO
3 -- EMANUEL DE FRENTES
4 -- EMANUEL DE COSTAS
5 -- BLACK ROOM''')
                    Function.linha()
                    do_gym = input("Select 1, 2, 3, 4 or 5:(Press 0 to leave)")
                    if do_gym == "1":
                        if "First battle" not in Bag_badges:
                            gym1_battle = True
                            while gym1_battle:
                                contador_team = 0
                                for i in Bag_Pok:
                                    contador_team += 1
                                    print(f"{contador_team} -- {i.name} -- {i.elemento}")
                                select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                                if select_fighter.isnumeric():
                                    if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                        selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                        gym1_selected = random.choice(gym1_team)
                                        battle = selected_pokemon.Battle(gym1_selected)
                                        if battle == "Lose":
                                            print("You lose the battle...")
                                            Bag_Pok.remove(selected_pokemon)
                                            Bag_fainted.append(selected_pokemon)
                                            x = input("Press enter...")
                                            if len(Bag_Pok) == 0:
                                                print("All your Pokemons are fainted!")
                                                x = input("Press enter...")
                                                print("You lose...")
                                                gym1_battle = False
                                            else:
                                                pass
                                        elif battle == "Win":
                                            print("You win the battle!")
                                            gym1_team.remove(gym1_selected)
                                            gym1_fainted.append(gym1_selected)
                                            x = input("Press enter...")
                                            if len(gym1_team) == 0:
                                                print("All of Captain's Pokemon are fainted...")
                                                x = input("Press enter...")
                                                print("You Won!!")
                                                gym_badges.append("First battle")
                                                gym1_battle = False
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
                        elif "First battle" in Bag_badges:
                            print("You all ready defeat him...")
                            x = input("Press enter...")
                            pass
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif do_gym == "2":
                        if "Second battle" not in Bag_badges:
                            gym2_battle = True
                            while gym2_battle:
                                contador_team = 0
                                for i in Bag_Pok:
                                    contador_team += 1
                                    print(f"{contador_team} -- {i.name} -- {i.elemento}")
                                select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                                if select_fighter.isnumeric():
                                    if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                        selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                        gym2_selected = random.choice(gym2_team)
                                        battle = selected_pokemon.Battle(gym2_selected)
                                        if battle == "Lose":
                                            print("You lose the battle...")
                                            Bag_Pok.remove(selected_pokemon)
                                            Bag_fainted.append(selected_pokemon)
                                            x = input("Press enter...")
                                            if len(Bag_Pok) == 0:
                                                print("All your Pokemons are fainted!")
                                                x = input("Press enter...")
                                                print("You lose...")
                                                gym2_battle = False
                                            else:
                                                pass
                                        elif battle == "Win":
                                            print("You win the battle!")
                                            gym2_team.remove(gym2_selected)
                                            gym2_fainted.append(gym2_selected)
                                            x = input("Press enter...")
                                            if len(gym2_team) == 0:
                                                print("All of Sarto's Pokemon are fainted...")
                                                x = input("Press enter...")
                                                print("You Won!!")
                                                gym_badges.append("Second battle")
                                                gym2_battle = False
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
                        elif "Second battle" in Bag_badges: 
                            print("You all ready defeat him...")
                            x = input("Press enter...")
                            pass 
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif do_gym == "3":
                        if "Third battle" not in Bag_badges:
                            gym3_battle = True
                            while gym3_battle:
                                contador_team = 0
                                for i in Bag_Pok:
                                    contador_team += 1
                                    print(f"{contador_team} -- {i.name} -- {i.elemento}")
                                select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                                if select_fighter.isnumeric():
                                    if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                        selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                        gym3_selected = random.choice(gym3_team)
                                        battle = selected_pokemon.Battle(gym3_selected)
                                        if battle == "Lose":
                                            print("You lose the battle...")
                                            Bag_Pok.remove(selected_pokemon)
                                            Bag_fainted.append(selected_pokemon)
                                            x = input("Press enter...")
                                            if len(Bag_Pok) == 0:
                                                print("All your Pokemons are fainted!")
                                                x = input("Press enter...")
                                                print("You lose...")
                                                gym3_battle = False
                                            else:
                                                pass
                                        elif battle == "Win":
                                            print("You win the battle!")
                                            gym3_team.remove(gym3_selected)
                                            gym3_fainted.append(gym3_selected)
                                            x = input("Press enter...")
                                            if len(gym3_team) == 0:
                                                print("All of Emanuel de Frente's Pokemon are fainted...")
                                                x = input("Press enter...")
                                                print("You Won!!")
                                                gym_badges.append("Third battle")
                                                gym3_battle = False
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
                        elif "Third battle" in Bag_badges:
                            print("You all ready defeat him...")
                            x = input("Press enter...")
                            pass 
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif do_gym == "4":
                        if "Fourth battle" not in Bag_badges:
                            gym4_battle = True
                            while gym4_battle:
                                contador_team = 0
                                for i in Bag_Pok:
                                    contador_team += 1
                                    print(f"{contador_team} -- {i.name} -- {i.elemento}")
                                select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                                if select_fighter.isnumeric():
                                    if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                        selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                        gym4_selected = random.choice(gym4_team)
                                        battle = selected_pokemon.Battle(gym4_selected)
                                        if battle == "Lose":
                                            print("You lose the battle...")
                                            Bag_Pok.remove(selected_pokemon)
                                            Bag_fainted.append(selected_pokemon)
                                            x = input("Press enter...")
                                            if len(Bag_Pok) == 0:
                                                print("All your Pokemons are fainted!")
                                                x = input("Press enter...")
                                                print("You lose...")
                                                gym4_battle = False
                                            else:
                                                pass
                                        elif battle == "Win":
                                            print("You win the battle!")
                                            gym4_team.remove(gym4_selected)
                                            gym4_fainted.append(gym4_selected)
                                            x = input("Press enter...")
                                            if len(gym4_team) == 0:
                                                print("All of Emanuel de Costa's Pokemon are fainted...")
                                                x = input("Press enter...")
                                                print("You Won!!")
                                                gym_badges.append("Fourth battle")
                                                gym4_battle = False
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
                        elif "Fourth battle" in Bag_badges:
                            print("You all ready defeat him...")
                            x = input("Press enter...")
                            pass 
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass            
                    elif do_gym == "5":
                        if len(gym_badges) >= 4:
                            print("-- IN THE GYM LEADER ROOM --")
                            if jogador == "Boy":
                                print("GYM LEADER(DAD): Hey son, your mom told me you are in a journey...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): But i never tought see you here...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): You know i'm the Gym leader here in Fortal City...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): And i have an obligation...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): If you want to go trough me...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): I couldn't allow this...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): Let's battle son...")
                                dad_battle = True
                                while dad_battle:
                                    contador_team = 0
                                    for i in Bag_Pok:
                                        contador_team += 1
                                        print(f"{contador_team} -- {i.name} -- {i.elemento}")
                                    select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                                    if select_fighter.isnumeric():
                                        if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                            selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                            dad_selected = random.choice(dad_team)
                                            battle = selected_pokemon.Battle(dad_selected)
                                            if battle == "Lose":
                                                print("You lose the battle...")
                                                Bag_Pok.remove(selected_pokemon)
                                                Bag_fainted.append(selected_pokemon)
                                                x = input("Press enter...")
                                                if len(Bag_Pok) == 0:
                                                    print("All your Pokemons are fainted!")
                                                    x = input("Press enter...")
                                                    print("You lose...")
                                                    dad_battle = False
                                                else:
                                                    pass
                                            elif battle == "Win":
                                                print("You win the battle!")
                                                dad_team.remove(dad_selected)
                                                dad_fainted.append(dad_selected)
                                                x = input("Press enter...")
                                                if len(dad_team) == 0:
                                                    print("All of Dad's Pokemon are fainted...")
                                                    x = input("Press enter...")
                                                    print("You Won!!")
                                                    Bag_badges.append("Fourth battle")
                                                    dad_battle = False
                                                    gym =  False
                                                    fortal_journey = False
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
                            elif jogador == "Girl":
                                print("GYM LEADER(DAD): Hey daughter, your mom told me you are in a journey...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): But i never tought see you here...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): You know i'm the Gym leader here in Fortal City...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): And i have an obligation...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): If you want to go trough me...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): I couldn't allow this...")
                                x = input("Press enter...")
                                print("GYM LEADER(DAD): Let's battle daughter...")
                                dad_battle = True
                                while dad_battle:
                                    contador_team = 0
                                    for i in Bag_Pok:
                                        contador_team += 1
                                        print(f"{contador_team} -- {i.get_name_pok()}")
                                    select_fighter = input(f"Select one in {len(Bag_Pok)} Pokemons:")
                                    if select_fighter.isnumeric():
                                        if int(select_fighter) in range(1, len(Bag_Pok) + 1):
                                            selected_pokemon = Bag_Pok[int(select_fighter) - 1]
                                            dad_selected = random.choice(dad_team)
                                            battle = selected_pokemon.Battle(dad_selected)
                                            if battle == "Lose":
                                                print("You lose the battle...")
                                                Bag_Pok.remove(selected_pokemon)
                                                Bag_fainted.append(selected_pokemon)
                                                x = input("Press enter...")
                                                if len(Bag_Pok) == 0:
                                                    print("All your Pokemons are fainted!")
                                                    x = input("Press enter...")
                                                    print("You lose...")
                                                    dad_battle = False
                                                else:
                                                    pass
                                            elif battle == "Win":
                                                print("You win the battle!")
                                                dad_team.remove(dad_selected)
                                                dad_fainted.append(dad_selected)
                                                x = input("Press enter...")
                                                if len(dad_team) == 0:
                                                    print("All of Dad's Pokemon are fainted...")
                                                    x = input("Press enter...")
                                                    print("You Won!!")
                                                    x = input("Press enter...")
                                                    print("You recieved the Normal Badge")
                                                    Bag_badges.append("Normal Badge")
                                                    dad_battle = False
                                                    fortal_jouyney = False
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
                            else:
                                print("INVALID!!")
                                x = input("Press enter...")
                                pass           
                        elif len(gym_badges) < 4:
                            print(gym_badges)
                            print("You need to defeat the other Trainers...")
                            x = input("Press enter...")
                            pass            
                        else:
                            print("INVALID!!")
                            x = input("Press enter...")
                            pass
                    elif do_gym == "0":
                        exit_gym = input("You want to leave the gym?(Y/N)")
                        if exit_gym.upper() == "N":
                            print("Oskey?!")
                            x = input("Press enter...")
                            pass
                        elif exit_gym.upper() == "Y":
                            print("Leaving...")
                            x = input("Press enter...")
                            gym = False
                    else:
                        print("INVALID!!")
                        x = input("Press enter...")
                        pass        
        
        elif fortal_path == "5":
            if "Super Rod" in Bag_Items:
                on_beach = True
                while on_beach:
                    print("-- IN THE TABAPUA LAKE --")
                    Function.linha()
                    print('''-- CHOOSE --
1 -- CRUSH'S BEACH
2 -- CRUSH'S BEACH
3 -- CRUSH'S BEACH
4 -- EXIT''')
                    Function.linha()
                    do_boat = input("Select 1, 2, 3 or 4:")
                    if do_boat in ("1", "2", "3"):
                        print("Using Super Rod...")
                        x = input("Press enter...")
                        find = (Function.crush_beach())
                        if find != "Nothing here...":
                            ask_catch = input(f"Try catch {find.name}?(Y/N)")
                            if ask_catch.upper() == "N":
                                print("Oskey?!")
                                x = input("Press enter...")
                                pass
                            elif ask_catch.upper() == "Y":
                                trhow_ball2 = True
                                while trhow_ball2:
                                    contador2 = 0
                                    contador3 = 0
                                    contador4 = 0
                                    contador5 = 0        
                                    for i in Bag_Items:
                                        if i == "Pokeball":
                                            contador2 += 1
                                        elif i == "Greatball":
                                            contador3 += 1
                                        elif i == "Ultraball":
                                            contador4 += 1
                                        elif i == "Masterball":
                                            contador5 += 1
                                    print(f"You have {contador2} Pokeball")
                                    print(f"You have {contador3} Greatball")
                                    print(f"You have {contador4} Ultraball")
                                    print(f"You have {contador5} Masterball")
                                    wich_ball = input("Wich ball you want to use?(Press 0 to run)")
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
                                                    print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                    Bag_pc.append(find)
                                                    trhow_ball2 = False
                                                elif len(Bag_Pok) <= 6:
                                                    print(f"Gotcha! {find.name} was captured and added on your team!")
                                                    Bag_Pok.append(find)
                                                    trhow_ball2 = False
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
                                                    print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                    Bag_pc.append(find)
                                                    trhow_ball2 = False
                                                elif len(Bag_Pok) <= 6:
                                                    print(f"Gotcha! {find.name} was captured and added on your team!")
                                                    Bag_Pok.append(find)
                                                    trhow_ball2 = False
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
                                                print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                Bag_pc.append(find)
                                                trhow_ball2 = False
                                            elif len(Bag_Pok) <= 6:
                                                print(f"Gotcha! {find.name} was captured and added on your team!")
                                                Bag_Pok.append(find)
                                                trhow_ball2 = False
                                            else:
                                                print("INVALID!!")
                                                x = input("Press enter...")
                                                pass   
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass
                                    elif wich_ball.upper() == "MASTERBALL":
                                        if len(Bag_Pok) >= 6:
                                                print(f"Gotcha! {find.name} was captured and added on your Pc!")
                                                Bag_pc.append(find)
                                                trhow_ball2 = False
                                        elif len(Bag_Pok) <= 6:
                                            print(f"Gotcha! {find.name} was captured and added on your team!")
                                            Bag_Pok.append(find)
                                            trhow_ball2 = False
                                        else:
                                            print("INVALID!!")
                                            x = input("Press enter...")
                                            pass
                                    elif wich_ball == "0":
                                        run = input("You want to run?(Y/N)")
                                        if run.upper() == "N":
                                            print("Oskey?!")
                                            x = input("Press enter...")
                                            pass
                                        elif run.upper() == "Y":
                                            print("Runing away...")
                                            x = input("Press enter...")
                                            trhow_ball2 = False
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
                            on_beach = False                
        
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass

    if jogador == "Boy":
        print("-- OUT OF THE GYM --")
        x = input("Press enter...")
        print("DAD: I can believe, i was defeated...")
        x = input("Press enter...")
        print("DAD: I'm so proud of you son...")
        x = input("Press enter...")
        print("DAD: I think you future gonna be brilliant...")
        x = input("Press enter...")
        print("DAD: Your mom and i are proud of you!")
        x = input("Press enter...")
        print("DAD: I think you gonna be the best trainer of the world...")
        x = input("Press enter...")
        print("DAD: Because you defeated me, take this...")
        x = input("Press enter...")
        print("DAD: This is proof of your victory...")
        x = input("Press enter...")
        print("-- YOU RECIEVED THE NORMAL BADGE --")
        Bag_Items.append("The Normal Badge")
        x = input("Press enter...")
        print("DAD: I have to return, but you need to complete your journey...")
        x = input("Press enter...")
        print("DAD: Are many Pokemons in the wolrd, and you have to see them...")
        x = input("Press enter...")
        print("DAD: By son, hope to see you again here!")
        x = input("Press enter...")
        print("YOU: This is my path, what is still waiting for me?")
        print("-- END --")
        x = input("Press enter...")
        print('''
        
                CREATED BY: EDUARDO ROCHA & RAFAEL BARBOSA 
                
    ''')
        Game = False
    elif jogador == "Girl":
        print("-- OUT OF THE GYM --")
        x = input("Press enter...")
        print("DAD: I can believe, i was defeated...")
        x = input("Press enter...")
        print("DAD: I'm so proud of you daughter...")
        x = input("Press enter...")
        print("DAD: I think you future gonna be brilliant...")
        x = input("Press enter...")
        print("DAD: Your mom and i are proud of you!")
        x = input("Press enter...")
        print("DAD: I think you gonna be the best trainer of the world...")
        x = input("Press enter...")
        print("DAD: Because you defeated me, take this...")
        x = input("Press enter...")
        print("DAD: This is proof of your victory...")
        x = input("Press enter...")
        print("-- YOU RECIEVED THE NORMAL BADGE --")
        Bag_Items.append("The Normal Badge")
        x = input("Press enter...")
        print("DAD: I have to return, but you need to complete your journey...")
        x = input("Press enter...")
        print("DAD: Are many Pokemons in the wolrd, and you have to see them...")
        x = input("Press enter...")
        print("DAD: By daughter, hope to see you again here!")
        x = input("Press enter...")
        print("YOU: This is my path, what is still waiting for me?")
        print("-- END --")
        x = input("Press enter...")
        print('''
        
                CREATED BY: EDUARDO ROCHA & RAFAEL BARBOSA 
                
    ''')
        Game = False
    else:
        print("INVALID!!")
        x = input("Press enter...")
        pass

    
    
    
    



                





                


    


    

       
        
