def isPlaindrome(test_string):
    return test_string == test_string[::-1]

# def check_palindrome_int(number):
#     # store a copy of number

#     temp = number
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
           if(string[first]==string[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break
    return int(status)  

def main():
    test_str = input('Enter test string: ')
    print(isPlaindrome(test_str))

if __name__ == "__main__":
    main()