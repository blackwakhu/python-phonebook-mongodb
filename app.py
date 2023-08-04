#!/usr/bin/python
from menufunctions import *


help = """this is the help page\n
            enter the following information
                n [fname] [lname] [nickname] [email] [contact] [provider] => new user but does not save any information 
                sn [fname] [lname] [nickname] [email] [contact] [provider] => new user saves all information 
                e [fname] [lname] => checks if the user exists
                ae [fname] [lname] [email].. => adds unlimited amount of emails to database
                ac [fname] [lname] [contact,provider].. => adds unlimited amount of contacts to database
                a => displays all information in the database
                eq [fname] [lname] => displays all information in the database about one person
            """
        

helpfunction = lambda: print(help)

if len(sys.argv) > 1:
    if sys.argv[1].lower() == "n":
        """creates a new user and prints out the user name"""
        user = enter_user_details(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
        print(user)

    elif sys.argv[1].lower() == "e":
        """creates an existing user and prints out the user name"""
        user, data = enter_existing_details(sys.argv[2], sys.argv[3])
        print(user)

    elif sys.argv[1].lower() == "sn":
        """saves a new users details"""
        user = enter_user_details(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
        save_new_details(user)
        print("{} details saved".format(user))

    elif sys.argv[1].lower() == "ae":
        """adds an unlimited amount of email addresses to the user"""
        emails = [email for email in sys.argv[4:]]
        user, data = enter_existing_details(sys.argv[2], sys.argv[3])
        update_existing_email(user, emails)
        print("the emails were added to {}".format(user))

    elif sys.argv[1].lower() == "ac":
        """adds an unlimited amount of contacts to the user"""
        contacts, providers = [], []
        try:
            for contact in sys.argv[4:]:
                a, b = contact.split(",")
                contacts.append(a)
                providers.append(b)
        except ValueError:
            print("enter a wrong value")
            sys.exit(1)

        user, data = enter_existing_details(sys.argv[2], sys.argv[3])
        update_existing_contact(user, contacts, providers)
        print("the contacts were added to {}".format(user))

    elif sys.argv[1].lower() == "a":
        """prints all the information available"""
        data = collection.find()
        for col in data:
            print("*"*30)
            print(f"name:\t{col['_id']}\ncontacts:")
            for contact in col["contacts"]:
                print(f"\t{contact['contact']}, {contact['provider']}")
            print("emails:")
            for email in col["email"]:
                print(f"\t{email}")
            print(f"relationship:\t{col['relationship']}\nnickname:\t{col['nickname']}\n")
            
    elif sys.argv[1].lower() == "eq":
        user, data = enter_existing_details(sys.argv[2], sys.argv[3])
        print("*"*30)
        print(f"name:\t{data[0]['_id']}\ncontacts:")
        for contact in data[0]["contacts"]:
            print(f"\t{contact['contact']}, {contact['provider']}")
        print("emails:")
        for email in data[0]["email"]:
            print(f"\t{email}")
        print(f"relationship:\t{data[0]['relationship']}\nnickname:\t{data[0]['nickname']}\n")

    else:
        helpfunction()

else:
    helpfunction()


    
