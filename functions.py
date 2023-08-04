#!/usr/bin/python

"""
this file contains the Contact class that specifies how contact is to be manipulated
"""


from pymongo import MongoClient
import re


db = MongoClient("localhost", 27017)["Contacts"]
collection = db["Phone_Details"]


class Contact(object):
    """this class is going to represent a single user and their contact information"""

    def __init__(self, fname, lname, nickname, relationship="friend"):
        self.fname = fname
        self.lname = lname
        self.nickname = nickname
        self.email = []
        self.contact = []
        self.relationship = relationship
        self.name = self.fname+" "+self.lname

    def __str__(self):
        """returns the name of the contact holder"""
        return self.name
    
    def addContact(self, newcontact, provider):
        """adds a new contact to the existing contact since a user can have multiple contacts"""
        if self.validateContact(newcontact):
            self.contact.append({"provider": provider, "contact": newcontact}) 
        else: print(" invalid contact")

    def addContactDict(self, newcontact):
        """adds a new contact dictionary to the existing contact"""
        if self.validateContact(newcontact["contact"]):
            self.contact.append(newcontact)
        else: print(" invalid contact")

    def addEmail(self, newemail):
        """adds a new email since a user can have more than one email"""
        if self.validateEmail(newemail):
            self.email.append(newemail)
        else: print("invalid email")

    def setNickname(self, newnickname):
        """sets a nickname"""
        self.nickname = newnickname

    def setRelationship(self, newrelationship="friend"):
        """sets a relationship"""
        self.relationship = newrelationship

    def getEmail(self):
        return self.email
    
    def getContact(self):
        return self.contact

    def saveDetails(self):
        doc = { "_id": self.name,
            "nickname": self.nickname,
            "firstname": self.fname,
            "lastname": self.lname,
            "contacts": self.contact,
            "email": self.email,
            "relationship": self.relationship
        }
        collection.insert_one(doc)

    def updateDetail(self, detail):
        if detail == "relationship": update = self.relationship
        elif detail == "contacts": update = self.contact
        elif detail == "email": update = self.email
        elif detail == "nickname": update = self.nickname
        collection.update_one({"_id": self.name}, {"$set": {detail: update}})


    def validateEmail(self, email):
        return  re.search(r"^[a-zA-Z0-9.!]+@+[a-zA-Z0-9.!]+.+[a-zA-Z0-9.!]$", email) 
    
    def validateContact(self, contact):
        return re.search(r"^0+[0-9]{9}$", contact) 
    

