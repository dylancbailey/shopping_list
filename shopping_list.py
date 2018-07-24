shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to view your items.
""")

    
def add_to_list(item):
    shopping_list.append(item)
    if len(shopping_list) <= 1:
        print(item, "was added! There is {} item in your list.".format(len(shopping_list)))
    else:
        print(item, "was added! There are {} items in your list.".format(len(shopping_list)))
    

def show_list():
    print("Items in your list:")
    for item in shopping_list:
        print("* ", item)

        
show_help()  
while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
        
        
    add_to_list(new_item)
    
show_list()
