import random
import vantagenspoke

lista_pokemon = vantagenspoke.lista_pokemon

lista_pokemon_t1 = []
lista_pokemon_t2 = []
lista_pokemon_t3 = []
lista_pokemon_t4 = []

for Pokemon in lista_pokemon:
    if Pokemon.tier == 1:
        lista_pokemon_t1.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier == 2:
        lista_pokemon_t2.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier == 3:
        lista_pokemon_t3.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier <= 4:
        lista_pokemon_t4.append(Pokemon)

# print("Choose the Pokemon you want to start!")
# print('''Choose the Pokemon: 
#   1 -- Bulbasauro
#   2 -- Charmande
#   3 -- Squirtle''')

# str_pokemon = input("Choose your starter pokemon:")
# match str_pokemon:
#     case "1":
#         str_pokemon = lista_pokemon[0]
#         lista_pokemon_t1.remove(lista_pokemon[0])
#     case "2":
#         str_pokemon = lista_pokemon[3]
#         lista_pokemon_t1.remove(lista_pokemon[3])
#     case "3":
#         str_pokemon = lista_pokemon[6]
#         lista_pokemon_t1.remove(lista_pokemon[6])
#     case _:
#         print("The chosen Pokemon is invalid! Choose a valid initial.")

# str_pokemon.Battle(random.choice(lista_pokemon_t1))    