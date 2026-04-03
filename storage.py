import json

FILE_NAME = "contacts.json"

try:
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)

except:
    contacts = {}


def save_contact():

    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file)
