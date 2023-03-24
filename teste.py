class Pokemon:
    def __init__(self, nome, lv, elemento, hp, at, de,):
        self.nome = nome
        self.lv = lv
        self.elemento = elemento
        self.hp = hp
        self.at = at
        self.de = de
   
    def batalha(self, oponente):
        print("Entrou na batalha o",self.nome,"vs",oponente.nome)
        contador = 1
        while True:
            print("Round",contador)
            contador = contador + 1

            vantagem = 1

            if self.elemento == "fogo":
                if oponente.elemento == "agua":
                    vantagem = 1.5
            if self.elemento == "agua":
                if oponente.elemento == "planta":
                    vantagem = 1.5
            if self.elemento == "planta":
                if oponente.elemento == "fogo":
                    vantagem = 1.5

            dano = self.at - oponente.de
            oponente.hp = oponente.hp - (dano*vantagem)
            print(self.nome,"deu",dano*vantagem,"de dano no",oponente.nome,"e ele ficou com",self.hp,"de HP.")

            dano = oponente.at - self.de
            self.hp = self.hp - (dano*vantagem)
            print(oponente.nome,"deu",dano*vantagem,"de dano no",self.nome,"e ele ficou com",oponente.hp,"de HP.")

            if self.hp <= 0:
                    print("O",self.nome,"ganhou a batalha.")
                    break
            if oponente.hp <= 0:
                    print("O",oponente.nome,"ganhou a batalha.")
                    break

pokemon1 = Pokemon("Charizard",100, "fogo", 250, 150, 60)
pokemon2 = Pokemon("Blastoise",100,"agua", 300, 100, 85)
pokemon3 = Pokemon("Venosauro",100,"planta", 450, 90, 75)

print("O pokemon",pokemon1.nome,"de lv",pokemon1.lv,"do elemento",pokemon1.elemento,"com o HP de ",pokemon1.hp,"e com AT de",pokemon1.at,"e DE de",pokemon1.de)
print("O pokemon",pokemon2.nome,"de lv",pokemon2.lv,"do elemento",pokemon2.elemento,"com o HP de ",pokemon2.hp,"e com AT de",pokemon2.at,"e DE de",pokemon2.de)
print("O pokemon",pokemon3.nome,"de lv",pokemon3.lv,"do elemento",pokemon3.elemento,"com o HP de ",pokemon3.hp,"e com AT de",pokemon3.at,"e DE de",pokemon3.de)

pokemon1.batalha(pokemon2)