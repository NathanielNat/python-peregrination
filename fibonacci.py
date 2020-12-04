# nth item is the sum of (n-1) and (n-1)th item 
# accep number of terms
n = int(input('Enter the term: '))

n1 = 0
n2 =1
count = 0


if n <= 0:
    print('Please enter a  positive number')

else:
    while count < n:
        nth = n1 +n2
        # swapping the values to the new ones
        n1 = n2
        n2  = nth
        count+=1
print(n1)

