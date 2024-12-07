import os
import sys


def display(dic) :

    if len(dic) == 0 :
        print("Your contact list is empty ...!")
        return

    for key, value in dic.items() :
        print(key, value)

def add(dic) : 
    name = input("Input name contact : ")
    phone_number = input("Input phone number : ")

    dic["name"] = phone_number

def delete(dic) : 
    name = input("Input the name of contact to delte : ")
    if name in dic :
        del dic[name]
        print(name , "'s contact has been deleted successfuly ")
    else :
        print(name , "'s contact doesn't exist on the list ...")

contacts = {}
CONTACTS_FILE = "contacts.txt"

if os.path.exists(CONTACTS_FILE) : 
    with open(CONTACTS_FILE) as file : 
        for line in file :
            data = line.strip().split(',')
    
            name = data[0].strip()
            phone_number = data[1].strip()
    
            contacts[name] = phone_number

    while(True) : 
        print("\n---Menu ---")
        print("1. Display contacts")
        print("2. Add a new contact")
        print("3. Delete contact")
        print("4. exit")
        
        try :
            choice = int(input("Your choice: "))
        except ValueError :
            print("Please enter a valid number !")
            continue

        match choice :
            case 1 :
                display(contacts)
            case 2 :
                add(contacts)
            case 3 :
                delete(contacts)
            case 4 :
                print("Goodbye ...!")
                with open(CONTACTS_FILE, 'w') as file :
                    for name, phone_number in contacts.items() :
                        file.write(f"{name}, {phone_number}\n")

                sys.exit()
            case _:
                print("Unknown command ...!")
else :
    print("file not found ...!")












