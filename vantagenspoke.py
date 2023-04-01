class Pokemon:
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        self.name = name
        self.tier = tier
        self.elemento = elemento
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Speed = Speed

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

            if self.Speed >= oponente.Speed:

                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano > 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                else: 
                    dano = 5
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                if oponente.Hp <= 0:
                    Win = print(self.name,"WINS THE BATTLE. CONGRATULATIONS!!")
                    return "Win"
                
                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano > 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                else: 
                    dano = 5
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in ",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                if self.Hp <= 0:
                    Lose = print("YOU LOOSE",oponente.name,"WINS THE BATTLE!!")
                    return "Lose"
                    
            elif oponente.Speed > self.Speed:

                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano > 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in ",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                else: 
                    dano = 5
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in ",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                if self.Hp <= 0:
                    Lose = print("YOU LOOSE",oponente.name,"WINS THE BATTLE!!")
                    return "Lose"
                    
                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano > 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                else: 
                    dano = 5
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                if oponente.Hp <= 0:
                    Win = print(self.name,"WINS THE BATTLE. CONGRATULATIONS!!")
                    return "Win"
                    
    def get_name_pok(self):
        return f"{self.name} -- {self.elemento}" 
    
class PokeNormal(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):

        if oponente.elemento == "lutador":
            return 1.5
        else:
            return 1.0

class PokeGrama(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):
    
        if oponente.elemento == "terra":
            return 1.5
        if oponente.elemento == "pedra":
            return 1.5
        if oponente.elemento == "agua":
            return 1.5
        else:
            return 1.0
    
class PokeFogo(Pokemon):

    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):
        
        if oponente.elemento == "grama":
            return 1.5
        if oponente.elemento == "aço":
            return 1.5
        if oponente.elemento == "insecto":
            return 1.5
        if oponente.elemento == "gelo":
            return 1.5
        else:
            return 1.0

class PokeAgua(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "fogo":
            return 1.5
        if oponente.elemento == "terra":
            return 1.5
        if oponente.elemento == "pedra":
            return 1.5
        else:
            return 1.0

class PokeEletrico(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "agua":
            return 1.5
        if oponente.elemento == "voador":
            return 1.5
        else:
            return 1.0
        
class PokeVoador(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "insecto":
            return 1.5
        if oponente.elemento == "lutador":
            return 1.5
        if oponente.elemento == "grama":
            return 1.5
        else:
            return 1.0
     
class PokeGelo(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
 
        if oponente.elemento == "dragao":
            return 1.5
        if oponente.elemento == "voador":
            return 1.5
        if oponente.elemento == "grama":
            return 1.5
        if oponente.elemento == "terra":
            return 1.5  
        else:
            return 1.0      

class PokePedra(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        
        if oponente.elemento == "insecto":
            return 1.5
        if oponente.elemento == "fogo":
            return 1.5
        if oponente.elemento == "voador":
            return 1.5
        if oponente.elemento == "gelo":
            return 1.5
        else:
            return 1.0

class PokeTerra(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "eletrico":
            return 1.5
        if oponente.elemento == "fogo":
            return 1.5
        if oponente.elemento == "venenoso":
            return 1.5
        if oponente.elemento == "pedra":
            return 1.5
        if oponente.elemento == "aço":
            return 1.5
        else:
            return 1.0

class PokeAço(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
    
        if oponente.elemento == "fada":
            return 1.5
        if oponente.elemento == "gelo":
            return 1.5
        if oponente.elemento == "pedra":
            return 1.5
        else:
            return 1.0

class PokeLutador(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "sombrio":
            return 1.5
        if oponente.elemento == "gelo":
            return 1.5
        if oponente.elemento == "normal":
            return 1.5
        if oponente.elemento == "pedra":
            return 1.5
        if oponente.elemento == "aço":
            return 1.5
        else:
            return 1.0

class PokeSombrio(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        
        if oponente.elemento == "fantasma":
            return 1.5
        if oponente.elemento == "psiquico":
            return 1.5
        else:
            return 1.0

class PokePsiquico(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "lutador":
            return 1.5
        if oponente.elemento == "venenoso":
            return 1.5
        else:
            return 1.0

class PokeVenenoso(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):
        
        if oponente.elemento == "fada":
            return 1.5
        if oponente.elemento == "grama":
            return 1.5
        else:
            return 1.0

class PokeInsecto(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        
        if oponente.elemento == "sombrio":
            return 1.5
        if oponente.elemento == "grama":
            return 1.5
        if oponente.elemento == "psiquico":
            return 1.5
        else:
            return 1.0

class PokeFada(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "sombrio":
            return 1.5
        if oponente.elemento == "dragao":
            return 1.5
        if oponente.elemento == "lutador":
            return 1.5
        else:
            return 1.0

class PokeFantasma(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "fantasma":
            return 1.5
        if oponente.elemento == "psiquico":
            return 1.5
        else:
            return 1.0

class PokeDragao(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "dragao":
            return 1.5
        if oponente.elemento == "fada":
            return 1.5
        if oponente.elemento == "galo":
            return 1.5
        else:
            return 1.0

poke001 = PokeGrama("Bulbasauro",1,"grama",45,65,65,45)
poke002 = PokeGrama("Ivysaur",2,"grama",60,80,80,60)
poke003 = PokeGrama("Venusaur",3,"grama",80,100,100,80)

poke004 = PokeFogo("Charmander",1,"fogo",39,60,50,65)
poke005 = PokeFogo("Charmeleon",2,"fogo",58,80,65,80)
poke006 = PokeFogo("Charizard",3,"fogo",78,109,85,100)

poke007 = PokeAgua("Squirtle",1,"agua",44,50,65,43)
poke008 = PokeAgua("Wartortle",2,"agua",59,65,80,58)
poke009 = PokeAgua("Blastoise",3,"agua",79,85,105,78)

poke010 = PokeInsecto("Caterpie",1,"insecto",45,30,35,45)
poke011 = PokeInsecto("Metapod",1,"insecto",50,25,55,30)
poke012 = PokeInsecto("Butterfree",3,"insecto",60,90,80,70)  

poke013 = PokeInsecto("Weedle",1,"insecto",40,35,30,50)
poke014 = PokeInsecto("Kakuna",1,"insecto",45,25,50,35)
poke015 = PokeInsecto("Beedrill",3,"insecto",65,90,80,75)

poke016 = PokeVoador("Pidgey",1,"voador",40,45,40,56)
poke017 = PokeVoador("Pidgeotto",2,"voador",63,60,55,71)
poke018 = PokeVoador("Pidgeot",3,"voador",83,80,75,101)

poke019 = PokeNormal("Rattata",1,"normal",30,56,35,72)
poke020 = PokeNormal("Raticate",3,"normal",55,81,70,97)

poke021 = PokeVoador("Spearow",1,"voador",40,60,31,70)
poke022 = PokeVoador("Fearow",3,"voador",65,90,65,100)

poke023 = PokeVenenoso("Ekans",1,"venenoso",35,60,54,55)
poke024 = PokeVenenoso("Arbok",3,"venenoso",60,95,79,80)

poke025 = PokeEletrico("Pikachu",2,"eletrico",35,55,50,90)
poke026 = PokeEletrico("Raichu",3,"eletrico",60,90,90,110)

poke027 = PokeTerra("Sandshrew",2,"terra",50,75,85,40)
poke028 = PokeTerra("Sandslash",3,"terra",75,100,110,65)

poke029 = PokeVenenoso("Nidoran♀",1,"venenoso",55,52,40,41)
poke030 = PokeVenenoso("Nidorina",2,"venenoso",70,62,67,56)
poke031 = PokeVenenoso("Nidoqueen",3,"venenoso",90,92,87,76)

poke032 = PokeVenenoso("Nidoran♂",1,"venenoso",46,57,40,50)
poke033 = PokeVenenoso("Nidorino",2,"venenoso",61,72,57,65)
poke034 = PokeVenenoso("Nidoking",3,"venenoso",81,102,75,85)

poke035 = PokeFada("Clefairy",1,"fada",70,60,65,35)
poke036 = PokeFada("Clefable",3,"fada",95,95,90,60)

poke037 = PokeFogo("Vulpix",1,"fogo",38,50,65,65)
poke038 = PokeFogo("Ninetales",3,"fogo",73,81,100,100)

poke039 = PokeNormal("Jigglypuff",1,"normal",115,45,25,20)
poke040 = PokeNormal("Wigglytuff",3,"normal",140,85,50,45)

poke041 = PokeVenenoso("Zubat",1,"venenoso",40,45,40,55)
poke042 = PokeVenenoso("Golbat",3,"venenoso",75,80,75,90)

poke043 = PokeGrama("Oddish",1,"grama",45,75,65,30)
poke044 = PokeGrama("Gloom",1,"grama",60,75,65,40)
poke045 = PokeGrama("Vileplume",3,"grama",75,110,95,50)

poke046 = PokeInsecto("Paras",1,"insecto",35,70,55,25)
poke047 = PokeInsecto("Parasect",2,"insecto",60,95,80,30)

poke048 = PokeInsecto("Venonat",1,"insecto",55,55,55,45)
poke049 = PokeInsecto("Venomoth",2,"insecto",65,90,75,90)

poke050 = PokeTerra("Diglett",1,"terra",10,55,45,90)
poke051 = PokeTerra("Dugtrio",2,"terra",35,100,70,120)

poke052 = PokeNormal("Meowth",1,"normal",40,45,40,90)
poke053 = PokeNormal("Persian",2,"normal",65,70,65,115)

poke054 = PokeAgua("Psyduck",1,"agua",50,65,50,55)
poke055 = PokeAgua("Golduck",3,"agua",80,95,80,85)

poke056 = PokeLutador("Mankey",1,"lutador",40,80,45,70)
poke057 = PokeLutador("Primeape",3,"lutador",65,105,70,95)

poke058 = PokeFogo("Growlithe",1,"fogo",55,70,50,60)
poke059 = PokeFogo("Arcanine",3,"fogo",90,110,80,95)

poke060 = PokeAgua("Poliwag",1,"agua",40,50,40,90)
poke061 = PokeAgua("Poliwhirl",2,"agua",65,65,65,90)
poke062 = PokeAgua("Poliwrath",3,"agua",90,95,95,70)

poke063 = PokePsiquico("Abra",1,"psiquico",25,105,55,90)
poke064 = PokePsiquico("Kadabra",2,"psiquico",40,120,70,105)
poke065 = PokePsiquico("Alakazam",3,"psiquico",55,135,95,120)

poke066 = PokeLutador("Machop",1,"lutador",70,80,50,35)
poke067 = PokeLutador("Machoke",2,"lutador",80,100,70,45)
poke068 = PokeLutador("Machamp",3,"lutador",90,130,85,55)

poke069 = PokeGrama("Bellsprout",1,"grama",50,75,35,40)
poke070 = PokeGrama("Weepinbell",2,"grama",65,90,50,55)
poke071 = PokeGrama("Victreebel",3,"grama",80,105,70,70)

poke072 = PokeAgua("Tentacool",1,"agua",40,50,100,70)
poke073 = PokeAgua("Tentacruel",3,"agua",80,80,120,100)

poke074 = PokePedra("Geodude",1,"pedra",40,80,100,20)
poke075 = PokePedra("Graveler",2,"pedra",55,95,105,35)
poke076 = PokePedra("Golem",3,"pedra",80,120,130,45)

poke077 = PokeFogo("Ponyta",2,"fogo",50,85,65,90)
poke078 = PokeFogo("Rapidash",3,"fogo",65,100,80,105)

poke079 = PokeAgua("Slowpoke",1,"agua",90,65,40,15)
poke080 = PokeAgua("Slowbro",3,"agua",95,100,110,30)

poke081 = PokeEletrico("Magnemite",1,"eletrico",25,95,70,45)
poke082 = PokeEletrico("Magneton",3,"eletrico",50,120,95,70)

poke083 = PokeNormal("Farfetch'd",2,"normal",52,90,62,60)

poke084 = PokeNormal("Doduo",1,"normal",35,85,45,75)
poke085 = PokeNormal("Dodrio",3,"normal",60,110,70,110)

poke086 = PokeAgua("Seel",1,"agua",65,45,70,45)
poke087 = PokeAgua("Dewgong",3,"agua",90,70,95,70)

poke088 = PokeVenenoso("Grimer",1,"venenoso",80,80,50,25)
poke089 = PokeVenenoso("Muk",3,"venenoso",105,105,100,50)

poke090 = PokeAgua("Shellder",1,"agua",30,65,100,40)
poke091 = PokeAgua("Cloyster",3,"agua",50,95,180,70)

poke092 = PokeFantasma("Gastly",1,"fantasma",30,100,35,80)
poke093 = PokeFantasma("Haunter",2,"fantasma",45,115,55,95)
poke094 = PokeFantasma("Gengar",3,"fantasma",60,130,75,110)

poke095 = PokePedra("Onix",2,"pedra",35,45,160,70)

poke096 = PokePsiquico("Drowzee",1,"psiquico",60,48,90,42)
poke097 = PokePsiquico("Hypno",3,"psiquico",85,73,115,67)

poke098 = PokeAgua("Krabby",1,"agua",30,105,90,75)
poke099 = PokeAgua("Kingler",3,"agua",55,130,115,100)

poke100 = PokeEletrico("Voltorb",1,"eletrico",40,55,55,100)
poke101 = PokeEletrico("Electrode",3,"eletrico",60,80,80,150)

poke102 = PokeGrama("Exeggcute",1,"grama",60,60,80,40)
poke103 = PokeGrama("Exeggutor",3,"grama",95,125,85,55)

poke104 = PokeTerra("Cubone",1,"terra",50,50,95,35)
poke105 = PokeTerra("Marowak",3,"terra",60,80,110,45)

poke106 = PokeLutador("Hitmonlee",3,"lutador",50,120,110,86)

poke107 = PokeLutador("Hitmonchan",3,"lutador",50,105,110,76)

poke108 = PokeNormal("Lickitung",2,"normal",90,60,75,30)

poke109 = PokeVenenoso("Koffing",1,"venenoso",40,65,90,35)
poke110 = PokeVenenoso("Weezing",3,"venenoso",65,90,120,60)

poke111 = PokeTerra("Rhyhorn",2,"terra",80,85,95,25)
poke112 = PokeTerra("Rhydon",3,"terra",105,130,120,40)

poke113 = PokeNormal("Chansey",3,"normal",250,35,105,50)

poke114 = PokeGrama("Tangela",2,"grama",65,100,115,60)

poke115 = PokeNormal("Kangaskhan",3,"normal",105,125,100,100)

poke116 = PokeAgua("Horsea",1,"agua",30,70,70,60)
poke117 = PokeAgua("Seadra",3,"agua",55,95,95,85)

poke118 = PokeAgua("Goldeen",1,"agua",80,67,60,63)
poke119 = PokeAgua("Seaking",3,"agua",45,92,80,68)

poke120 = PokeAgua("Staryu",1,"agua",30,70,55,85)
poke121 = PokeAgua("Starmie",3,"agua",60,100,85,115)

poke122 = PokePsiquico("Mr. Mime",3,"psiquico",40,100,120,90)

poke123 = PokeInsecto("Scyther",3,"insecto",70,110,80,105)

poke124 = PokeGelo("Jynx",3,"gelo",65,115,95,95)

poke125 = PokeEletrico("Electabuzz",3,"eletrico",65,95,85,105)

poke126 = PokeFogo("Magmar",3,"fogo",63,100,85,93)

poke127 = PokeInsecto("Pinsir",3,"insecto",65,125,100,85)

poke128 = PokeNormal("Tauros",3,"normal",75,100,95,110)

poke129 = PokeAgua("Magikarp",1,"agua",20,15,55,80)
poke130 = PokeAgua("Gyarados",3,"agua",95,125,100,81)

poke131 = PokeGelo("Lapras",3,"gelo",130,85,95,60)

poke132 = PokeNormal("Ditto",1,"normal",48,48,48,48)

poke133 = PokeNormal("Eevee",1,"normal",55,55,65,55)
poke134 = PokeAgua("Vaporeon",3,"agua",130,110,95,65)
poke135 = PokeEletrico("Jolteon",3,"eletrico",65,110,95,130)
poke136 = PokeFogo("Flareon",3,"fogo",65,130,110,65)

poke137 = PokeNormal("Porygon",2,"normal",65,85,75,40)

poke138 = PokePedra("Omanyte",2,"pedra",35,90,100,35)
poke139 = PokePedra("Omastar",3,"pedra",70,125,115,55)

poke140 = PokePedra("Kabuto",2,"pedra",30,80,90,55)
poke141 = PokePedra("Kabutops",3,"pedra",60,115,105,80)

poke142 = PokePedra("Aerodactyl",3,"pedra",80,105,75,130)

poke143 = PokeNormal("Snorlax",3,"normal",160,110,110,30)

poke144 = PokeGelo("Articuno",4,"gelo",90,95,125,85)

poke145 = PokeEletrico("Zapdos",4,"eletrico",90,125,90,100)

poke146 = PokeFogo("Moltres",4,"fogo",90,125,90,90)

poke147 = PokeDragao("Dratini",1,"dragao",41,64,50,50)
poke148 = PokeDragao("Dragonair",2,"dragao",61,84,70,70)
poke149 = PokeDragao("Dragonite",4,"dragao",91,134,100,80)

poke150 = PokePsiquico("Mewtwo",5,"psiquico",106,154,90,130)

poke151 = PokePsiquico("Mew",4,"psiquico",100,100,100,100)
poke152 = PokePsiquico("Tariken",5,"psiquico",250,250,250,250)

lista_pokemon = []

for i in range(1,152):
    if i < 10:
        lista_pokemon.append(globals()[f"poke00{i}"])
    elif i >=10 and i <100:
        lista_pokemon.append(globals()[f"poke0{i}"])
    else:
        lista_pokemon.append(globals()[f"poke{i}"])


                