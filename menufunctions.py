from functions import *
import sys

def save_new_details(user):
    """saves the details for a new user"""
    user.saveDetails()

def enter_user_details(fname, lname, nickname, email, contact, relationship, provider):
    """instantiates a new user"""
    user = Contact(fname, lname, nickname, relationship)
    user.addEmail(email)
    user.addContact(contact, provider)

    return user

def enter_existing_details(fname, lname):
    """instantiates an existing user"""
    try:
        name = fname+" "+lname
        data = collection.find({"_id": name})    
        user = Contact(fname, lname, data[0]['nickname'], data[0]['relationship'])
        for email in data[0]['email']:
            user.addEmail(email)
        for contact in data[0]['contacts']:
            user.addContactDict(contact)
             
        return user, data
    
    except IndexError as e: 
        print("the user of name {} does not exist".format(name))
        sys.exit(1)

def update_existing_email(user, emails):
    for email in emails:
        user.addEmail(email)
    user.updateDetail("email")

def update_existing_contact(user, contacts, providers):
    for contact, provider in zip(contacts, providers):
        user.addContact(contact, provider) 
    user.updateDetail("contacts")