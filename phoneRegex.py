import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# mo = phoneNumRegex.search('My number is 415-555-4242.')

heroRegex =re.compile(r'Batman|Robben')

# grp1 = heroRegex.search('Batman and Robben')

# print(grp1.group())

# grp2 = heroRegex.search('Robben and Batman')

# print(grp2.group())


# batRegex = re.compile(r'Bat(man|mobile|girl|woman|signal)')

# try1 = batRegex.search('The Batsignal was on')

# print(try1.group())

# batRegex = re.compile(r'Bat(wo)?man')

# xy = batRegex.search('The adventures of Batman')
# print(xy.group())

# xy1 = batRegex.search('The adventures of Batwoman')
# print(xy1.group())

# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())

# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# print(mo2.group())

# telRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# findReg = telRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

# print(findReg)

# vowelRegex = re.compile(r'[aeiouAEIOU]')
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD. Stadium chelsea pseudopodia')
# consonant = consonantRegex.findall('RoboCop eats baby food. BABY FOOD. Stadium chelsea pseudopodia')
# print(vowels)
# print(consonant)

# txt = 'Nathaniel is a DevOps Engineer and makes link 12K monthly 12'
# beginsWithNathaniel = re.search('^Nathaniel',txt)
# endsWithNum = re.findall('\d+$',txt)
# print(beginsWithNathaniel)
# print(endsWithNum)

# txt   = 'The cat in the hat sat on the flat mat after Nat killed the fat rat who spat on the bat. Pat will eat the food'
# endsWithAt = re.findall('.at',txt)

txt = 'RoboCop is part man part machine, all cop.'
robocop = re.compile(r'robocop', re.I)
robo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(robo)

# txt = re.search('robocop',re.I).group()

# phRegex = 

