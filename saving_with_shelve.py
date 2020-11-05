import shelve

# writing to a binary file with shelve 


# // method 1
# shelfFile = shelve.open('my_languages')

# languages = ['Python','PHP',"JS",'Java']

# shelfFile['languages'] = languages

# shelfFile.close()


# method 2 
# with shelve.open('my_language_data') as shelfFile:
#     languages = ['Python','PHP','JS','Java']

#     shelfFile['languages'] = languages




# reading from a binary file with shelve
# method 1
# shelfFile = shelve.open('my_language_data')
# languages = shelfFile['languages']
# print(languages)
# shelfFile.close()

# method 2
with shelve.open('my_language_data') as shelfFile:
    languages = shelfFile['languages']
    print(languages)
