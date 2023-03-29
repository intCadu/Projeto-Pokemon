# Loja POKEBALL
Bag_Items = ["Potion","Potion","Potion","Pokeball","Pokeball","Greatball","Greatball","Ultraball","Ultraball","Ultraball","Ultraball","Ultraball","Ultraball","Ultraball"]

Wallet = 1000

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
            
            
                
                
                
               
                    
    
    
    
        

            
                
    

   