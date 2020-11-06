
import pprint

languages = [{'name':'Java','level':'Intermediate'},{'name':'Python','level':'Intermediate'},{'name':'PHP', 'level':'Intermediate'
}]

pprint.pformat(languages)

# fileObj = open('my_laguages.py','w')

# fileObj.write('languages  = ' + pprint.pformat(languages) + '\n')

# fileObj.close()


# 2nd method


with open('my_laguages.py','w') as fileObj:
    fileObj.write('languages = ' + pprint.pformat(languages) + '\n')

