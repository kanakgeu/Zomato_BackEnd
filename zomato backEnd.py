zomato_menu={
        'dominos':{'owner name':'Tom Monaghan','rating':'4.0',
        'items':{'country special':'600','farm house':'700','5 pepper':'1000'}},
        'pizza hut':{ 'owner name':'Dan carney','rating':'4.0',
        'items':{'veg onion':'400','tomato':'450','capseicum':'550'}}}
print "Welcome to zomato"
zomato_res=int(raw_input("Are you !.Owner \n2.customer"))
if zomato_res==1:
    owner_choice=raw_input("Do you want to updte information? YES/NO")
    if owner_choice=='No':
        print "It's OK!"
    elif owner_choice=='YES':
        print "In which restaurant do you update"
        own_choice=raw_input("1.Dominos \n2.Pizza Hut")
        if own_choice=='1':
            print "What do you want:"
            own1_choice=raw_input("1.change prize \n2.add item \n3.delete item")
            if own1_choice=='1':
                name=raw_input("enter neme of item")
                if name in zomato_menu['dominos']['items']:
                    price1=int(raw_input("enter new price of item:"))
                    zomato_menu['dominos']['items'][name]=price1
                    print "price update!"
                else:
                    print "Sorry! this item is not prsent"
                    exit()

            elif  own1_choice=='2':
                item_name=raw_input("enter name of item")
                item_prize=int(raw_input("Enter price of item"))
                zomato_menu['dominos']['items'].update({item_name:item_prize})
                print "New item added!"
            elif own1_choice=='3':
                name=raw_input("enter name of item do you want to delete")
                if name in zomato_menu['dominos']:
                    del zomato_menu['dominos']['items'][name]
                    print "Item deleted!"
                else:
                    print "Sorry! THIs item is not present in list."
                    exit()
            else:
                print "Wrong input... "
        elif own_choice=='2':
            print "What do you want:"
            own1_choice = raw_input("1.change prize \n2.add item \n3.delete item")
            if own1_choice == '1':
                name = raw_input("enter neme of item")
                if name in zomato_menu['dominos']['items']:
                    price1 = int(raw_input("enter new price of item:"))
                    zomato_menu['dominos']['items'][name] = price1
                    print "price update!"
                else:
                    print "Sorry! this item is not prsent"
                    exit()

            elif own1_choice == '2':
                item_name = raw_input("enter name of item")
                item_prize = int(raw_input("Enter price of item"))
                zomato_menu['dominos']['items'].update({item_name:item_prize})
                print "New item added!"

            elif own1_choice == '3':
                name = raw_input("enter name of item do you want to delete")
                if name in zomato_menu['pizza hut']['items']:
                    del zomato_menu['pizza hut']['items'][name]
                    print "Item deleted!"
                else:
                    print "Sorry! THIs item is not present in list."
                    exit()
            else:
                print "Wrong input..."


elif zomato_res==2:
    print"Do you want order:"
    cus_choice=raw_input("!.Yes \n2.No")

    if cus_choice=='2':
        print "Thanks for visit!"
    elif cus_choice=='1':
        print"Which restaurant do you want to prefer?"
        cus_choice1=int(raw_input("1.Dominos \n2.Pizza Hut"))
        if cus_choice1==1:
            print "SeLect your item?"
            cus_choice3=int(raw_input("1.country special \n2.farm House \n3.5 Pepper"))
            if cus_choice3 in (1,2,3):
                print "Order successful"
            else:
                print "Sorry unavailable"
                exit()
        elif cus_choice1==2:
            print "Which one do you order?"
            cus_choice3 = int(raw_input("1.Veg onion \n2.Tomato \n3.Cepseicum"))
            if cus_choice3 in (1, 2, 3):
                print "Order successful"
            else:
                print "Sorry unavailable"
                exit()
        print "Enter your choice:"
        cus_choice4=int(raw_input("1.Home delivery \n2. Walk in"))
        if cus_choice4==1:
            print "choosen method is delivery"
            if cus_choice1==1:
                fo=zomato_menu['dominos']['items']
                fo=fo.keys()
                cost=fo[cus_choice3+1]
                cost= zomato_menu['pizza hut']['items'][cost]

                bill=cost +(.1*cost) + (.06*cost) + (.15*cost)
                print bill
            elif cus_choice1==2:
                fo = zomato_menu['pizza hut']['items']
                cost = int(fo[cus_choice3 + 1])
                bill = cost + (.1 * cost) + (.06 * cost) + (.15 * cost)
                print bill

        elif cus_choice4==2:
            print "choosen method is walk in"
            if cus_choice1 == 1:
                fo = zomato_menu['dominos']['items']
                cost = int(fo[cus_choice3 + 1])
                bill = cost + (.1 * cost) + (.06 * cost) + (.15 * cost)
                print bill
            elif cus_choice1 == 2:
                fo = zomato_menu['pizza hut']['items']
                cost = int(fo[cus_choice3 + 1])
                bill = cost + (.1 * cost) + (.06 * cost) + (.15 * cost)
                print bill
        print "D0 you wish to rate the restaurant"
        cus_choice5=raw_input("YES/NO")
        if cus_choice5=='YES':
            print "In which restaurant do you want rating"
            choice=int(raw_input("1.dominos \n 2.pizza hut"))
            if choice==1:
                zomato_menu['dominos']['rating']=rating
            elif choice==2:
                zomato_menu['pizza hut']['rating'] = rating
            print "Have a nice day!"
        else:
                print "Have a nice day!"











