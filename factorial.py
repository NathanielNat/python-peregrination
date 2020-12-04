def factorial(n):
    """ returns the factorial of a given number"""
    n_factorial = 1
    # loop through all numbers from one to n a and
    if n == 0: 
        n_factorial = 1
        print(n_factorial)
    else:
        for i in range(1,n+1):
            n_factorial = i * n_factorial
            print(n_factorial)
    return n_factorial


def main():
    """ Accept input from user"""
    n = int(input('Enter a number whose factorial you want to find: '))
    return factorial(n)
    

if __name__ == '__main__':
    main()