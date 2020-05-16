"""
    Program: Warehouse Management System
    Functionality:
        -Replete Menu
        -Register items to the catalog
            id
            title
            category
            price
            stock
        -Display a Catalog
        -Saving / retrieving data to/from file
        -Update the stock of an item
            -show the list of items
            -ask the user to choose an id
            -ask the user for the new stock value
            -update the stock
            -save changes

        Register a Sale
            -show the list of items 
            -ask the user to choose an id
            -ask the user to provide the amount
            -update the stock
        
        -Have a log of events
            -file name for the logs
            -list for the log
            -add_log_event
            -save_log
            -read_log
            -update existing fns to register entries

        -Display list of categories

        Print the Total value of the stock(sum (price * stock))
"""
#from/file(where)/import/function(what)
from menu import menu, clear, header
from item import Item
import pickle
import datetime

# global vars
catalog = []
log = []
last_id = 0
data_file = 'warehouse.data'
log_file = 'data.log'

# functions

def save_catalog():
    global data_file
    writer = open(data_file, "wb")  #create a file
    pickle.dump(catalog, writer)
    writer.close()
    print("**Data Saved!**")

def read_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
                catalog.append(item)

        last = catalog[-1]
        last_id = last.id

        how_many = len(catalog)
        print("** Loaded " + str(how_many) + " items")
    except:
        print("** There is no data in the DB**")

def save_log():
    global log_file
    writer = open(log_file, "wb")  #create a file
    pickle.dump(log, writer)
    writer.close()
    print("**Data Logged!**")

def read_log():
    try:
        global log_file
        reader = open(log_file, "rb")
        temp_list = pickle.load(reader)

        for entry in temp_list:
            log.append(entry)

        how_many = len(log)
        print("** Loaded " + str(how_many) + " log entries")
    except:
        print("** There is no logged data in the DB**")


#instructions
def register_item():
    global last_id
    clear()
    header("Register an item")

    title = input("New item title: ")
    cat = input("New item category: ")
    price = float(input("New item price: "))
    stock = int(input("New item stock: "))        
            

    new_item = Item() # how to create new objects
    last_id += 1
    new_item.id = last_id
    new_item.title = title
    new_item.category = cat
    new_item.price = price
    new_item.stock = stock

    catalog.append(new_item)
    add_log_events("New Item", "Added item: " + str(last_id))
    print("Item created!")

def display_catalog():
    size = len(catalog)
    header('Current Catalog (' + str(size)+ ' items')

    print(" | " + 'ID'.rjust(2)
        + " | " + 'Title'.ljust(20) 
        + " | " + 'Category'.ljust(15) 
        + " | " + 'Price'.rjust(10) 
        + " | " + 'Stock'.ljust(5) + " | " )
    print("-" * 70)


    for item in catalog:
        print(" | " + str(item.id) 
        + " | " + item.title.ljust(20) 
        + " | " + item.category.ljust(15) 
        + " | " + str(item.price).rjust(10) 
        + " | " + str(item.stock).ljust(5) + " | ")

    print("-" * 70)

def print_log():
    header('Log of Events')
    for entry in log:
        print(entry)

def display_no_stock():
    size = len(catalog)
    header('Out of Stock (' + str(size)+ ' items')

    print(" | " + 'ID'.rjust(2)
        + " | " + 'Title'.ljust(20) 
        + " | " + 'Category'.ljust(15) 
        + " | " + 'Price'.rjust(10) 
        + " | " + 'Stock'.ljust(5) + " | " )
    print("-" * 70)


    for item in catalog:
        if(item.stock == 0):
            print(" | " + str(item.id) 
            + " | " + item.title.ljust(20) 
            + " | " + item.category.ljust(15) 
            + " | " + str(item.price).rjust(10) 
            + " | " + str(item.stock).ljust(5) + " | ")

    print("-" * 70)

def stock_value():
    total = 0
    for item in catalog:
            total += (item.price * item.stock)
    print("Total Stock Value: $" +str(total))
            
def delete_item():
    display_catalog()
    id = int(input("Please select the ID of the item to delete: "))
    found = False
    for item in catalog:
        if(item.id == id):
            catalog.remove(item)
            found = True
            break

    if(found):
        print(item.title + " has been removed!")
        add_log_events("Remove", "Item removed: " +str(item.title))
        input("Please press enter to continue...")
        
    else:
            print(" -" + id + " not exist.")

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%b/%d/%Y %T")

def add_log_events(event_type, event_description):
    entry = get_current_time() +  " | " + event_type.ljust(10) + " | " + event_description
    log.append(entry)
    save_log
    
def update_stock(opc):
    display_catalog()
    id = int(input("Please select the ID of stock to update: "))
    found = False
    for item in catalog:
        if(item.id == id):
            found = True

            if(opc == 1):
                stock = int(input("New stock value:  "))
                item.stock = stock
                print('Stock updated!')
                add_log_events("Stock Updated", str(item.title) + " had its stock updated")
            else:
                sold = int(input("Number of items to sale: "))
                item.stock -= sold
                print('Sale updated!')
                add_log_events("Dslr", str(item.title) + " has been sold")

    if(not found):
            print("Error: Selected ID does not exist.")

def list_categories():
    print('Current Catagories')
    print("-" * 30)
    for item in catalog:
        print(str(item.category)) 

# Start Menu

read_catalog()
read_log()
input("Please press enter to continue...")

opc = ''
while(opc != 'x'):
        clear()
        menu()
        print("\n")
        opc = input("Please input an option: ")
        if(opc == '1'):
            register_item()
            save_catalog()
        elif (opc == '2'):
            display_catalog()
        elif (opc == '3'):
            display_no_stock()
        elif (opc == '4'):
            update_stock(1) #update a stock
            save_catalog()
        elif (opc == '5'):
            stock_value()
        elif (opc == '6'):
            delete_item()
            save_catalog()
        elif (opc == '7'):
            update_stock(2) # register a sale
            save_catalog()
        elif (opc == '8'):
            print_log()
        elif (opc == '9'):
            list_categories()
        print("\n")
        input("Please press enter to continue...")
