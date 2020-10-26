from name_func import get_formatted_name

print("Enter 'q' to quit")

while True:
    first = input('Enter your first name: ')
    if first == 'q':
        break
    last = input('Enter your Last Name: ')
    if last == 'q':
        break
    formatted_name  = get_formatted_name(first,last)
    print(f'Well formatted name: {formatted_name}')

