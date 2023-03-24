class Player:
    def __init__(self, gender, name, age, list_pok):
        self.gender = gender
        self.name = name
        self.age = age
        self.list_pok = list_pok
    
    def get_information(self):
        return player1.__dict__
    
    def set_name(self, new_name):
        self.name = new_name
        return new_name



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
    elif nome_confirmacao.upper() == "N":
        nome_jogador = input("What's your name:")
        player1.set_name(nome_jogador)

    else: 
        ("INVALID ANSWER!!!")
    
    print('''CHOSE YOUR PATH!!
    1 -- GO TO LABORATORY 
    2 -- TALK TO MOM
    3 -- GO TO ROOM''')

    path_jogador = input("Select 1, 2 or 3:")
    if path



    


    

       
        
