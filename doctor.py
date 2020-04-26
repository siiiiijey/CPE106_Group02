"""
Program: doctor.py
Author: Ken
Conducts an interactive session of nondirective psychotherapy.
"""
from sys import argv
import pandas as pd
import random
import sqlite3

conn = sqlite3.connect('doctor.db')

c = conn.cursor()

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"} 

def reply(sentence):
    """Implements two different reply strategies."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords) 

def main():
    """Handles the interaction between patient and doctor."""
    firstTime = input("Is this your first time visiting the doctor? ")
    if firstTime.lower() == "yes":
        newUserFN = input("Please register your first name: ")
        newUserLN = input("Please register your last name: ")
        c.execute("INSERT INTO doctor(firstName,lastName, history) VALUES (?,?,'None')",(newUserFN, newUserLN))
        conn.commit()
        print("\nYou're now registered!")
    inputName = input("Please input your last name: ")
    c.execute("SELECT * FROM doctor WHERE lastName == ?",(inputName,))
    data = c.fetchall()
    for entry in data:
        fn = entry[0]
        ln = entry[1]
        history = entry[2]
    print("Hi, " + fn + ". This is your history:\n" + history + "\n")
    print("What can I do for you? \n")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        response = reply(sentence)
        print(response)
        c.execute("UPDATE doctor SET history=? WHERE lastName ==?",(response,ln,)) 
        conn.commit()
# The entry point for program execution
if __name__ == "__main__":
    main()

