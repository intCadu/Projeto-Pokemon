import random
import Game_Main_Poke
import vantagenspoke

Bag_Pok = []
Bag_pc = []


lista_tier1 = Game_Main_Poke.lista_pokemon_t1
lista_tier2 =  Game_Main_Poke.lista_pokemon_t2
lista_tier3 =  Game_Main_Poke.lista_pokemon_t3


poke_tier1_grama = []
poke_tier1_agua = []
poke_tier1_fogo = []
poke_tier1_voador = []
poke_tier1_lutador = []
poke_tier1_psiquico = []
poke_tier1_dragao = []
poke_tier1_normal = []
poke_tier1_eletrico = []
poke_tier1_fantasma = []
poke_tier1_fada = []
poke_tier1_venenoso = []
poke_tier1_terra = []
poke_tier1_pedra = []
poke_tier1_inseto = []
poke_tier1_gelo = []

poke_tier2_grama = []
poke_tier2_agua = []
poke_tier2_fogo = []
poke_tier2_voador = []
poke_tier2_lutador = []
poke_tier2_psiquico = []
poke_tier2_dragao = []
poke_tier2_normal = []
poke_tier2_eletrico = []
poke_tier2_fantasma = []
poke_tier2_fada = []
poke_tier2_venenoso = []
poke_tier2_terra = []
poke_tier2_pedra = []
poke_tier2_inseto = []
poke_tier2_gelo = []

poke_tier3_grama = []
poke_tier3_agua = []
poke_tier3_fogo = []
poke_tier3_voador = []
poke_tier3_lutador = []
poke_tier3_psiquico = []
poke_tier3_dragao = []
poke_tier3_normal = []
poke_tier3_eletrico = []
poke_tier3_fantasma = []
poke_tier3_fada = []
poke_tier3_venenoso = []
poke_tier3_terra = []
poke_tier3_pedra = []
poke_tier3_inseto = []
poke_tier3_gelo = []

for Pokemon in lista_tier1:
    if Pokemon.elemento == "grama":
        poke_tier1_grama.append(Pokemon)
    if Pokemon.elemento == "agua":
        poke_tier1_agua.append(Pokemon)
    if Pokemon.elemento == "fogo":
        poke_tier1_fogo.append(Pokemon)
    if Pokemon.elemento == "voador":
        poke_tier1_voador.append(Pokemon)
    if Pokemon.elemento == "lutador":
        poke_tier1_lutador.append(Pokemon)
    if Pokemon.elemento == "psiquico":
        poke_tier1_psiquico.append(Pokemon)
    if Pokemon.elemento == "dragao":
        poke_tier1_dragao.append(Pokemon)
    if Pokemon.elemento == "normal":
        poke_tier1_normal.append(Pokemon)
    if Pokemon.elemento == "eletrico":
        poke_tier1_eletrico.append(Pokemon)
    if Pokemon.elemento == "fantasma":
        poke_tier1_fantasma.append(Pokemon)
    if Pokemon.elemento == "fada":
        poke_tier1_fada.append(Pokemon)
    if Pokemon.elemento == "venenoso":
        poke_tier1_venenoso.append(Pokemon)
    if Pokemon.elemento == "terra":
        poke_tier1_terra.append(Pokemon)
    if Pokemon.elemento == "pedra":
        poke_tier1_pedra.append(Pokemon)
    if Pokemon.elemento == "insecto":
        poke_tier1_inseto.append(Pokemon)
    if Pokemon.elemento == "gelo":
        poke_tier1_gelo.append(Pokemon)

for Pokemon in lista_tier2: 
    if Pokemon.elemento == "grama":
        poke_tier2_grama.append(Pokemon)
    if Pokemon.elemento == "agua":
        poke_tier2_agua.append(Pokemon)
    if Pokemon.elemento == "fogo":
        poke_tier2_fogo.append(Pokemon)
    if Pokemon.elemento == "voador":
        poke_tier2_voador.append(Pokemon)
    if Pokemon.elemento == "lutador":
        poke_tier2_lutador.append(Pokemon)
    if Pokemon.elemento == "psiquico":
        poke_tier2_psiquico.append(Pokemon)
    if Pokemon.elemento == "dragao":
        poke_tier2_dragao.append(Pokemon)
    if Pokemon.elemento == "normal":
        poke_tier2_normal.append(Pokemon)
    if Pokemon.elemento == "eletrico":
        poke_tier2_eletrico.append(Pokemon)
    if Pokemon.elemento == "fantasma":
        poke_tier2_fantasma.append(Pokemon)
    if Pokemon.elemento == "fada":
        poke_tier2_fada.append(Pokemon)
    if Pokemon.elemento == "venenoso":
        poke_tier2_venenoso.append(Pokemon)
    if Pokemon.elemento == "terra":
        poke_tier2_terra.append(Pokemon)
    if Pokemon.elemento == "pedra":
        poke_tier2_pedra.append(Pokemon)
    if Pokemon.elemento == "insecto":
        poke_tier2_inseto.append(Pokemon)
    if Pokemon.elemento == "gelo":
        poke_tier2_gelo.append(Pokemon)

for Pokemon in lista_tier3:
    if Pokemon.elemento == "grama":
        poke_tier3_grama.append(Pokemon)
    if Pokemon.elemento == "agua":
        poke_tier3_agua.append(Pokemon)
    if Pokemon.elemento == "fogo":
        poke_tier3_fogo.append(Pokemon)
    if Pokemon.elemento == "voador":
        poke_tier3_voador.append(Pokemon)
    if Pokemon.elemento == "lutador":
        poke_tier3_lutador.append(Pokemon)
    if Pokemon.elemento == "psiquico":
        poke_tier3_psiquico.append(Pokemon)
    if Pokemon.elemento == "dragao":
        poke_tier3_dragao.append(Pokemon)
    if Pokemon.elemento == "normal":
        poke_tier3_normal.append(Pokemon)
    if Pokemon.elemento == "eletrico":
        poke_tier3_eletrico.append(Pokemon)
    if Pokemon.elemento == "fantasma":
        poke_tier3_fantasma.append(Pokemon)
    if Pokemon.elemento == "fada":
        poke_tier3_fada.append(Pokemon)
    if Pokemon.elemento == "venenoso":
        poke_tier3_venenoso.append(Pokemon)
    if Pokemon.elemento == "terra":
        poke_tier3_terra.append(Pokemon)
    if Pokemon.elemento == "pedra":
        poke_tier3_pedra.append(Pokemon)
    if Pokemon.elemento == "insecto":
        poke_tier3_inseto.append(Pokemon)
    if Pokemon.elemento == "gelo":
        poke_tier3_gelo.append(Pokemon)


def Pc_Pok(pokemon):
    if len(Bag_Pok) == 6:
        Bag_pc.append(pokemon)
    return Bag_pc 

def change_team(pokemon1, pokemon2):

    if pokemon1 in Bag_Pok:
        Bag_Pok.remove(pokemon1) and Bag_pc.append(pokemon1)
    if pokemon2 in Bag_pc:
        Bag_pc.remove(pokemon2) and Bag_Pok.append(pokemon2)

def found_lake():
    pok_lake = random.choice([poke_tier1_agua, poke_tier1_voador])
    chance_found = random.randint(1, 101)
    if chance_found <= 25:
        nothing = "Nothing here..."
        return nothing
    elif chance_found > 25:
        found_lake1 = random.choice(pok_lake)
        return found_lake1
    else:
        invalid = "INVALID!!"
        return invalid

def found_bush():

    pok_bush = random.choice([poke_tier1_eletrico,poke_tier1_fogo,poke_tier1_grama,poke_tier1_fantasma,poke_tier1_fada,poke_tier1_lutador,poke_tier1_normal,poke_tier1_pedra,poke_tier1_venenoso,poke_tier1_psiquico,poke_tier1_voador])
    chance_found = random.randint(1, 101)
    if chance_found <= 25:
        nothing = "Nothing here..."
        return nothing
    elif chance_found > 25:
        found_bush1 = random.choice(pok_bush)
        return found_bush1
    else:
        invalid = "INVALID!!"
        return invalid

def coco1_bush():

    pok_bush = random.choice([poke_tier3_eletrico,poke_tier3_fogo,poke_tier3_grama,poke_tier3_fantasma,poke_tier3_fada,poke_tier3_lutador,poke_tier3_normal,poke_tier3_pedra,poke_tier3_venenoso,poke_tier3_psiquico,poke_tier3_voador])
    chance_found = random.randint(1, 1001)
    if chance_found < 250:
        nothing = "Nothing here..."
        return nothing
    elif chance_found == 251:
        coco_bush1 = random.choice(vantagenspoke.poke150, vantagenspoke.poke151,vantagenspoke.poke149)
        return coco_bush1
    elif chance_found > 252:
        coco_bush1 = random.choice(pok_bush)
        return coco_bush1
    else:
        invalid = "INVALID!!"
        return invalid

def coco2_bush():

    pok_bush = random.choice([poke_tier3_eletrico,poke_tier3_fogo,poke_tier3_grama,poke_tier3_fantasma,poke_tier3_fada,poke_tier3_lutador,poke_tier3_normal,poke_tier3_pedra,poke_tier3_venenoso,poke_tier3_psiquico,poke_tier3_voador])
    chance_found = random.randint(1, 1001)
    if chance_found < 250:
        nothing = "Nothing here..."
        return nothing
    elif chance_found == 251:
        coco_bush2 = random.choice(vantagenspoke.poke146, vantagenspoke.poke059,vantagenspoke.poke065)
        return coco_bush2
    elif chance_found > 252:
        coco_bush2 = random.choice(pok_bush)
        return coco_bush2
    else:
        invalid = "INVALID!!"
        return invalid

def coco3_bush():

    pok_bush = random.choice([poke_tier3_eletrico,poke_tier3_fogo,poke_tier3_grama,poke_tier3_fantasma,poke_tier3_fada,poke_tier3_lutador,poke_tier3_normal,poke_tier3_pedra,poke_tier3_venenoso,poke_tier3_psiquico,poke_tier3_voador])
    chance_found = random.randint(1, 1001)
    if chance_found < 250:
        nothing = "Nothing here..."
        return nothing
    elif chance_found == 251:
        coco_bush3 = random.choice(vantagenspoke.poke135, vantagenspoke.poke136,vantagenspoke.poke143)
        return coco_bush3
    elif chance_found > 252:
        coco_bush3 = random.choice(pok_bush)
        return coco_bush3
    else:
        invalid = "INVALID!!"
        return invalid

def coco4_bush():

    pok_bush = random.choice([poke_tier3_eletrico,poke_tier3_fogo,poke_tier3_grama,poke_tier3_fantasma,poke_tier3_fada,poke_tier3_lutador,poke_tier3_normal,poke_tier3_pedra,poke_tier3_venenoso,poke_tier3_psiquico,poke_tier3_voador])
    chance_found = random.randint(1, 1001)
    if chance_found < 250:
        nothing = "Nothing here..."
        return nothing
    elif chance_found == 251:
        coco_bush4 = random.choice(vantagenspoke.poke123, vantagenspoke.poke106,vantagenspoke.poke107)
        return coco_bush4
    elif chance_found > 252:
        coco_bush4 = random.choice(pok_bush)
        return coco_bush4
    else:
        invalid = "INVALID!!"
        return invalid
    
def crush_beach():
    pok_lake = random.choice([poke_tier3_agua, poke_tier3_voador])
    chance_found = random.randint(1, 1001)
    if chance_found <= 250:
        nothing = "Nothing here..."
        return nothing
    elif chance_found == 251:
        crush_beach1 = random.choice(vantagenspoke.poke130, vantagenspoke.poke131, vantagenspoke.poke144, vantagenspoke.poke117, vantagenspoke.poke091)
        return crush_beach1
    elif chance_found > 252:
        crush_beach1 = random.choice(pok_lake)
        return crush_beach1
    else:
        invalid = "INVALID!!"
        return invalid
    
