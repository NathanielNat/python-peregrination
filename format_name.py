def formatName(first_name='',last_name=''):
    """ returns a formatted version of a name provided by a user """
    if first_name and last_name :
        name = f'Name: {first_name}, {last_name}'
    elif first_name:
        name = f'Name: {first_name}'
    elif last_name:
        name = f'Name: {last_name}'
    else:
        name = ''
    return name


def main():
    first_name = input('Enter your first name: ')
    last_name = input('\nEnter your last name: ')
    print(formatName(first_name,last_name))
    # print(formatName('Nat','Nathaniel'))
    # print(formatName('Nat',''))
    # print(formatName('','Nathaniel'))
    # print(formatName('',''))


if __name__ == "__main__":
    main()