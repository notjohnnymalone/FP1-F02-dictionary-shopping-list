############################################
#-Dictionary Shopping List
#-Reid A. Martin
#-7 October 2021
############################################

shop_list = {} #setting up shopping dictionary
tot_cost = shop_list.values() #setting up sum variable for total price
import time #importing time for a sleep function
##----Functions----##

def add_item():
    done = False #while variable
    while done == False: #while loop
        item = input("what do you want to add? if ur done type 'done' \n> ").lower() #item input, puts all input into lowercase
        if item == "done": #if done is true this breaks this loop and goes back to main
            done = True
        elif item != "done": #if aren't done takes you through this
            price = float(input("How much does the item cost? \n> ")) #number input that can be added to a sum
            print("Adding", item, ". It costs $",price) #shows what user inputted
            shop_list[item] = price #second input gets attached to item
            
def remove_item():
    done = False #while variable
    while done == False:
        print_list() #prints shopping list
        item = input("what do you want to remove? if ur done type 'done' \n> ").lower() #removing input
        if item == "done":
            done = True
        elif item != "done":
            if item in shop_list: #if the item is in the list
                print("Erasing", item) #status saying it is getting erased
                del shop_list[item] #erases item from dict
            else:
                print("maybe pick something that's in there :|") #some *personality*... also gently tells the user the get their poop in a group
                
                
def print_list():
    for (item,price) in shop_list.items(): #repeats for each item
        print("You have", item,". It costs $",price) #prints item and cost
    print("The total cost is $", sum(tot_cost)) #prints total cost
        
        
def main():
    prog = 1 #while variable
    else_ah = 1 #variable thats on the brink of a breakdown
    print("hi. this a shopping list. do stuff") #more *personality*
    while prog == 1: #LOOP
        print("\n----------------\n")#spaces out text
        print("whaddya want")#tad bit more personality
        option = input("Add, View, Remove, Quit? ").lower() #option input
        if option == "add" or option == 1: #if option 1
            add_item() #calls add funct
        elif option == "view" or option == 2:#if option 2
            print_list() #calls print funct
        elif option == "remove" or option == 3:#if option 3
            remove_item() #calls remove funct
        elif option == "quit" or option == 4:#if option 4
            prog = 0 #breaks loop
            print_list()#prints list
            time.sleep(2) #wait
            print("farewell *insert insult here*") #the creative juices weren't flowing too well
        else:
            if else_ah <= 5: #ifr the breakdown variable is under 6 it is only slightly passive aggressive
                print("try picking an actual option")
                else_ah = else_ah + 1 #gets closer and closer to the breakdown
            else:
                print("IS THERE SOMETHING THAT WRONG WITH YOU THAT YOU CANT PICK A REAL OPTION LIKE WHAT THE F--- IS WRONG WITH YOU AAAAAAAHHHHHHHHHH \nGET HELP YOU LUNATIC") #tantrum
        


main() #runs main
