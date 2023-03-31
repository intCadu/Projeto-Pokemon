class Pokemon:
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        self.name = name
        self.tier = tier
        self.elemento = elemento
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Speed = Speed


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

Bulbassaur = PokeGrama("Bulbassauro",1,"grama",45,65,65,45)
Ivyssaur = PokeGrama("Ivyssaur",2,"grama",60,80,80,60)
Venussaur = PokeGrama("Venussaur",3,"grama",80,100,100,80)

Charmander = PokeFogo("Charmander",1,"fogo",39,60,50,65)
Charmeleon = PokeFogo("Charmeleon",2,"fogo",58,80,65,80)
Charizard = PokeFogo("Charizard",3,"fogo",78,109,85,100)

Squirtle = PokeAgua("Squirtle",1,"agua",44,50,65,43)
Wartortle = PokeAgua("Wartortle",2,"agua",59,65,80,58)
Blastoise = PokeAgua("Blastoise",3,"agua",79,85,105,78)

Caterpie = PokeInsecto("Caterpie",1,"insecto",45,30,35,45)
Metapod = PokeInsecto("Metapod",1,"insecto",50,25,55,30)
Butterfree = PokeInsecto("Butterfree",3,"insecto",60,90,80,70)  

Weedle = PokeInsecto("Weedle",1,"insecto",40,35,30,50)
Kakuna = PokeInsecto("Kakuna",1,"insecto",45,25,50,35)
Beedrill = PokeInsecto("Beedrill",3,"insecto",65,90,80,75)

Pidgey = PokeVoador("Pidgey",1,"voador",40,45,40,56)
Pidgeotto = PokeVoador("Pidgeotto",2,"voador",63,60,55,71)
Pidgeot = PokeVoador("Pidgeot",3,"voador",83,80,75,101)

Rattata = PokeNormal("Rattata",1,"normal",30,56,35,72)
Raticate = PokeNormal("Raticate",3,"normal",55,81,70,97)

Spearow = PokeVoador("Spearow",1,"voador",40,60,31,70)
Fearow = PokeVoador("Fearow",3,"voador",65,90,65,100)

Ekans = PokeVenenoso("Ekans",1,"venenoso",35,60,54,55)
Arbok = PokeVenenoso("Arbok",3,"venenoso",60,95,79,80)

Pikachu = PokeEletrico("Pikachu",2,"eletrico",35,55,50,90)
Raichu = PokeEletrico("Raichu",3,"eletrico",60,90,90,110)

Sandshrew = PokeTerra("Sandshrew",2,"terra",50,75,85,40)
Sandslash = PokeTerra("Sandslash",3,"terra",75,100,110,65)

Nidoran_F = PokeVenenoso("Nidoran♀",1,"venenoso",55,52,40,41)
Nidorina = PokeVenenoso("Nidorina",2,"venenoso",70,62,67,56)
Nidoqueen = PokeVenenoso("Nidoqueen",3,"venenoso",90,92,87,76)

Nidoran_M = PokeVenenoso("Nidoran♂",1,"venenoso",46,57,40,50)
Nidorino = PokeVenenoso("Nidorino",2,"venenoso",61,72,57,65)
Nidoking = PokeVenenoso("Nidoking",3,"venenoso",81,102,75,85)

Clefairy = PokeFada("Clefairy",1,"fada",70,60,65,35)
Clefable = PokeFada("Clefable",3,"fada",95,95,90,60)

Vulpix = PokeFogo("Vulpix",1,"fogo",38,50,65,65)
Ninetales = PokeFogo("Ninetales",3,"fogo",73,81,100,100)

Jigglypuff = PokeNormal("Jigglypuff",1,"normal",115,45,25,20)
Wigglytuff = PokeNormal("Wigglytuff",3,"normal",140,85,50,45)

Zubat = PokeVenenoso("Zubat",1,"venenoso",40,45,40,55)
Golbat = PokeVenenoso("Golbat",3,"venenoso",75,80,75,90)

Oddish = PokeGrama("Oddish",1,"grama",45,75,65,30)
Gloom = PokeGrama("Gloom",100,"grama",60,75,65,40)
Vileplume = PokeGrama("Vileplume",3,"grama",75,110,95,50)

Paras = PokeInsecto("Paras",1,"insecto",35,70,55,25)
Parasect = PokeInsecto("Parasect",2,"insecto",60,95,80,30)

Venonat = PokeInsecto("Venonat",1,"insecto",55,55,55,45)
Venomoth = PokeInsecto("Venomoth",2,"insecto",65,90,75,90)

Venomoth = PokeTerra("Venomoth",1,"terra",10,55,45,90)
Dugtrio = PokeTerra("Dugtrio",2,"terra",35,100,70,120)

Meowth = PokeNormal("Meowth",1,"normal",40,45,40,90)
Persian = PokeNormal("Persian",2,"normal",65,70,65,115)

Psyduck = PokeAgua("Psyduck",1,"agua",50,65,50,55)
Golduck = PokeAgua("Golduck",3,"agua",80,95,80,85)

Mankey = PokeLutador("Mankey",1,"lutador",40,80,45,70)
Primeape = PokeLutador("Primeape",3,"lutador",65,105,70,95)

Growlithe = PokeFogo("Growlithe",1,"fogo",55,70,50,60)
Arcanine = PokeFogo("Arcanine",3,"fogo",90,110,80,95)

Poliwag = PokeAgua("Poliwag",1,"agua",40,50,40,90)
Poliwhirl = PokeAgua("Poliwhirl",2,"agua",65,65,65,90)
Poliwrath = PokeAgua("Poliwrath",3,"agua",90,95,95,70)

Abra = PokePsiquico("Abra",1,"psiquico",25,105,55,90)
Kadabra = PokePsiquico("Kadabra",2,"psiquico",40,120,70,105)
Alakazam = PokePsiquico("Alakazam",3,"psiquico",55,135,95,120)

Machop = PokeLutador("Machop",1,"lutador",70,80,50,35)
Machoke = PokeLutador("Machoke",2,"lutador",80,100,70,45)
Machamp = PokeLutador("Machamp",3,"lutador",90,130,85,55)

Bellsprout = PokeGrama("Bellsprout",1,"grama",50,75,35,40)
Weepinbell = PokeGrama("Weepinbell",2,"grama",65,90,50,55)
Victreebel = PokeGrama("Victreebel",3,"grama",80,105,70,70)

Tentacool = PokeAgua("Tentacool",1,"agua",40,50,100,70)
Tentacruel = PokeAgua("Tentacruel",3,"agua",80,80,120,100)

Geodude = PokePedra("Geodude",1,"pedra",40,80,100,20)
Graveler = PokePedra("Graveler",2,"pedra",55,95,105,35)
Golem = PokePedra("Golem",3,"pedra",80,120,130,45)

Ponyta = PokeFogo("Ponyta",2,"fogo",50,85,65,90)
Rapidash = PokeFogo("Rapidash",3,"fogo",65,100,80,105)

Slowpoke = PokeAgua("Slowpoke",1,"agua",90,65,40,15)
Slowbro = PokeAgua("Slowbro",3,"agua",95,100,110,30)

Magnemite = PokeEletrico("Magnemite",1,"eletrico",25,95,70,45)
Magneton = PokeEletrico("Magneton",3,"eletrico",50,120,95,70)

Farfetchd = PokeNormal("Farfetch'd",2,"normal",52,90,62,60)

Doduo = PokeNormal("Doduo",1,"normal",35,85,45,75)
Dodrio = PokeNormal("Dodrio",3,"normal",60,110,70,110)

Seel = PokeAgua("Seel",1,"agua",65,45,70,45)
Dewgong = PokeAgua("Dewgong",3,"agua",90,70,95,70)

Grimer = PokeVenenoso("Grimer",1,"venenoso",80,80,50,25)
Muk = PokeVenenoso("Muk",3,"venenoso",105,105,100,50)

Shellder = PokeAgua("Shellder",1,"agua",30,65,100,40)
Cloyster = PokeAgua("Cloyster",3,"agua",50,95,180,70)

Gastly = PokeFantasma("Gastly",1,"fantasma",30,100,35,80)
Haunter = PokeFantasma("Haunter",2,"fantasma",45,115,55,95)
Gengar = PokeFantasma("Gengar",3,"fantasma",60,130,75,110)

Onix = PokePedra("Onix",2,"pedra",35,45,160,70)

Drowzee = PokePsiquico("Drowzee",1,"psiquico",60,48,90,42)
Hypno = PokePsiquico("Hypno",3,"psiquico",85,73,115,67)

Krabby = PokeAgua("Krabby",1,"agua",30,105,90,75)
Kingler = PokeAgua("Kingler",3,"agua",55,130,115,100)

Voltorb = PokeEletrico("Voltorb",1,"eletrico",40,55,55,100)
Electrode = PokeEletrico("Electrode",3,"eletrico",60,80,80,150)

Exeggcute = PokeGrama("Exeggcute",1,"grama",60,60,80,40)
Exeggutor = PokeGrama("Exeggutor",3,"grama",95,125,85,55)

Cubone = PokeTerra("Cubone",1,"terra",50,50,95,35)
Marowak = PokeTerra("Marowak",3,"terra",60,80,110,45)

Hitmonlee = PokeLutador("Hitmonlee",3,"lutador",50,120,110,86)

Hitmonchan = PokeLutador("Hitmonchan",3,"lutador",50,105,110,76)

Lickitung = PokeNormal("Lickitung",2,"normal",90,60,75,30)

Koffing = PokeVenenoso("Koffing",1,"venenoso",40,65,90,35)
Weezing = PokeVenenoso("Weezing",3,"venenoso",65,90,120,60)

Rhyhorn = PokeTerra("Rhyhorn",2,"terra",80,85,95,25)
Rhydon = PokeTerra("Rhydon",3,"terra",105,130,120,40)

Chansey = PokeNormal("Chansey",3,"normal",250,35,105,50)

Tangela = PokeGrama("Tangela",2,"grama",65,100,115,60)

Kangaskhan = PokeNormal("Kangaskhan",3,"normal",105,125,100,100)

Horsea = PokeAgua("Horsea",1,"agua",30,70,70,60)
Seadra = PokeAgua("Seadra",3,"agua",55,95,95,85)

Goldeen = PokeAgua("Goldeen",1,"agua",80,67,60,63)
Seaking = PokeAgua("Seaking",3,"agua",45,92,80,68)

Staryu = PokeAgua("Staryu",1,"agua",30,70,55,85)
Starmie = PokeAgua("Starmie",3,"agua",60,100,85,115)

MrMime = PokePsiquico("Mr. Mime",3,"psiquico",40,100,120,90)

Scyther = PokeInsecto("Scyther",3,"insecto",70,110,80,105)

Jynx = PokeGelo("Jynx",3,"gelo",65,115,95,95)

Electabuzz = PokeEletrico("Electabuzz",3,"eletrico",65,95,85,105)

Magmar = PokeFogo("Magmar",3,"fogo",63,100,85,93)

Pinsir = PokeInsecto("Pinsir",3,"insecto",65,125,100,85)

Tauros = PokeNormal("Tauros",3,"normal",75,100,95,110)

Magikarp = PokeAgua("Magikarp",1,"agua",20,15,55,80)
Gyarados = PokeAgua("Gyarados",3,"agua",95,125,100,81)

Lapras = PokeGelo("Lapras",3,"gelo",130,85,95,60)

Ditto = PokeNormal("Ditto",1,"normal",48,48,48,48)

Eevee = PokeNormal("Eevee",1,"normal",55,55,65,55)
Vaporeon = PokeAgua("Vaporeon",3,"agua",130,110,95,65)
Jolteon = PokeEletrico("Jolteon",3,"eletrico",65,110,95,130)
Flareon = PokeFogo("Flareon",3,"fogo",65,130,110,65)

Porygon = PokeNormal("Porygon",2,"normal",65,85,75,40)

Omanyte = PokePedra("Omanyte",2,"pedra",35,90,100,35)
Omastar = PokePedra("Omastar",3,"pedra",70,125,115,55)

Kabuto = PokePedra("Kabuto",2,"pedra",30,80,90,55)
Kabutops = PokePedra("Kabutops",3,"pedra",60,115,105,80)

Aerodactyl = PokePedra("Aerodactyl",3,"pedra",80,105,75,130)

Snorlax = PokeNormal("Snorlax",3,"normal",160,110,110,30)

Articuno = PokeGelo("Articuno",4,"gelo",90,95,125,85)

Zapdos = PokeEletrico("Zapdos",4,"eletrico",90,125,90,100)

Moltres = PokeFogo("Moltres",4,"fogo",90,125,90,90)

Dratini = PokeDragao("Dratini",1,"dragao",41,64,50,50)
Dragonair = PokeDragao("Dragonair",2,"dragao",61,84,70,70)
Dragonite = PokeDragao("Dragonite",4,"dragao",91,134,100,80)

Mewtwo = PokePsiquico("Mewtwo",5,"psiquico",106,154,90,130)

Mew = PokePsiquico("Mew",4,"psiquico",100,100,100,100)