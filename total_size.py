"""get total size of folder"""
import os

# folder = input('Enter the absolute path of folder whose size you want: ')
# totalSize = 0
# folder  = os.path.abspath(folder)
# try:
#    for filename in os.listdir(folder):
#        totalSize += os.path.getsize(filename)
# except FileNotFoundError as identifier:
#     print('Your path you provided does not exist on your system')
# else:
#     print(totalSize)
# # finally:
# #     pass


# print(os.path.exists('/Users/Nat'))
folder = '/Users/Nat/src-code'
totalSize = 0
for filename in os.listdir(folder):
    totalSize += os.path.getsize(filename)

print(totalSize)