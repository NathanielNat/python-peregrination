import re
with open('madlibs.txt') as madlibFile:
    adjetive = input('Enter an adjective: \n')
    noun1 = input('Enter a noun: \n')
    verb = input('Enter a verb: \n')
    noun2 = input('Enter a noun: \n')

#     old_words = ('ADJECTIVE','NOUN','VERB','NOUN')
#     replacements = (adjetive,noun1,verb,noun2)

    for line in madlibFile:
        line.replace('ADJECTIVE', adjetive).replace('NOUN', noun1).replace('VERB',verb)

    


# txt = 'Agent Alice gave the secret documents to Agent Bob.'
# namesRegex = re.compile(r'Agent \w+')
# namesRegex.sub('CENSORED', txt) 

# print(namesRegex.sub('CENSORED', txt) )
# print(txt.replace('Alice', 'police').replace('Agent', 'YYY'))
