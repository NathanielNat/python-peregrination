#Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
import sys
num = int(input())

# create empty phonebook
phone_book = {}

for i in range(0, num):
    # get name and phone numbers from user to create phonebook dictionary
    entry = sys.stdin().split("\n")

    # get names as keyss
    name = entry[0]
    # get phone numbers as values
    phone = int(entry[1])
    # set key value pairs of phone and name in our phonebook dictionary
    phone_book[name] = phone

for j in range(0,num):
    # accept names  to be queried from user
    name = str(input())

    # check if name is in phone book
    if name in phone_book:
        phone = phone_book[name]
        print(name + '='+ str(phone))
    else:
        print('Not found')