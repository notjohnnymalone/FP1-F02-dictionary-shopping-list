############################################
#-Dictionary Shopping List
#-Reid A. Martin
#-7 October 2021
############################################

shop_list = {}
tot_cost = shop_list.values()
import time
##----Functions----##

def add_item():
    done = False
    while done == False:
        item = input("What do you want to add? Type 'done' to exit \n> ").lower()
        if item == "done":
            done = True
        elif item != "done":
            price = float(input("How much does the item cost? \n> "))
            print("Adding", item, ". It costs $",price)
            shop_list[item] = price
            
def remove_item():
    done = False
    while done == False:
        print_list()
        item = input("What do you want to remove? Type 'done' to exit \n> ").lower()
        if item == "done":
            done = True
        elif item != "done":
            if item in shop_list:
                print("Erasing", item)
                del shop_list[item]
            else:
                print("maybe pick something that's in there :|")
                
                
def print_list():
    for (item,price) in shop_list.items():
        print("You have", item,". It costs $",price)
    print("The total cost is $", sum(tot_cost))
        
        
def main():
    prog = 1
    else_ah = 1
    print("hi. this a shopping list. do stuff")
    while prog == 1:
        print("")
        print("whaddya want")
        option = input("Add, View, Remove, Quit? ").lower()
        if option == "add" or option == 1:
            add_item()
        elif option == "view" or option == 2:
            print_list()
        elif option == "remove" or option == 3:
            remove_item()
        elif option == "quit" or option == 4:
            prog = 0
            print_list()
            time.sleep(2)
            print("farewell *insert insult here*")
        else:
            if else_ah <= 5:
                print("try picking an actual option")
                else_ah = else_ah + 1
            else:
                print("IS THERE SOMETHING THAT WRONG WITH YOU THAT YOU CANT PICK A REAL OPTION LIKE WHAT THE F--- IS WRONG WITH YOU AAAAAAAHHHHHHHHHH \nGET HELP YOU LUNATIC")
        


main()