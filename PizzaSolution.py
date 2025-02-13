def pythonPizza():
    print("Welcome to the pizza Plus")
    sp=150
    mp=250
    lp=450
    total_price=0
    print(f"Small Pizza: {sp} \nMedium Pizza: {mp} \nLarge Pizza: {lp}")
    order=input("What kind of pizza you like to buy: Small(s), Medium(m), Large(l)")
    peppironi=input("Would ou like to add Pepporini 'Y' or 'N': " )
    chees=input("Would you like to add extra cheas 'Y' or 'N': ")
    if order=="s":
        if peppironi=="y":
            if chees=="y":
                total_price=sp+50+20
            else:
                total_price=sp+50
        else:
            if chees=="y":
                total_price=sp+20
            else:
                total_price=sp
            
    elif order=="m":
        if peppironi=="y":
            if chees=="y":
                total_price=mp+50+20
            else:
                total_price=mp+50
        else:  
            if chees=="y":
                total_price=mp+20
            else:
                total_price=mp
    else:
        if peppironi=="y":
            if chees=="y":
                total_price=lp+50+20
            else:
                total_price=lp+50
        else:
            if chees=="y":
                total_price=lp+20
            else:
                total_price=lp

    print(total_price)

pythonPizza()