import random
import vantagenspoke
import Game_Main_Poke
import Function
Penny_Team1 = []
Penny_Team2 = []
Bag_Pok = [vantagenspoke.poke150]
Bag_Items = []
Bag_pc = []
Wallet = 5000
Bag_fainted = [vantagenspoke.poke149,vantagenspoke.poke145]

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