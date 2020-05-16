import os

def menu():
    header("Register a new item")
    print(' [1] Register Items')
    print(' [2] Display Catalog')
    print(' [3] Display out of Stock Items')
    print(' [4] Update Stock')
    print(' [5] Stock Worth')
    print(' [6] Delete Item')
    print(' [7] Register a Sale')
    print(' [8] Transaction Log')
    print(' [9] List Categories')

    print(" [x] Exit")

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

def header(title):
    print("-" * 60)
    print(" " + title)
    print("-" * 60)
    print("\n")