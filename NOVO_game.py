class Player:
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age
        
    
    def get_information(self):
        return player1.__dict__
    
    def set_name(self, new_name):
        self.name = new_name
        return new_name

Bag_Pok = []
Bag_Items = []

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
        break
    age_jogador = input("What's your age?")    
    nome_jogador = input("What's the player name?")
    nome_confirmacao = input(f"Your name is {nome_jogador}?(Y/N)")
    if nome_confirmacao.upper() == "Y":
        player1 = Player(jogador,nome_jogador,age_jogador)
        x = input("You want to see your informations?(Y/N)")
        if x.upper() == "Y":
            print(player1.get_information())
        else:
            pass
    # Precisa melhorar a logica da Função set_name
    elif nome_confirmacao.upper() == "N":
        nome_jogador = input("What's your name:")
        player1.set_name(nome_jogador)

    else: 
        ("INVALID ANSWER!!!")
    
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
                x = input("Press enter to speak with Prf. Oak...")
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
                    print("YOU: I gonna take it!!")
                    Bag_Items.append("Potion")
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




    


    

       
        
