def isPlaindrome(test_string):
    return test_string == test_string[::-1]


def main():
    test_str = input('Enter test string: ')
    print(isPlaindrome(test_str))

if __name__ == "__main__":
    main()