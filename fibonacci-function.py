def fibonacci(n):
    n1 = 0
    n2 =1
    count = 0

    if n <= 0:
        print('ENter a positive')
    else:
        while count < n:
            nth = n1 +n2
            n1 = n2
            n2 = nth
            count+=1
    return n1

def recFibonacci(n):
    

    if n <=0:
        return 'print a positive number '
    elif n==1:
        return 0
    elif n ==2:
        return 1

    else:
         return recFibonacci(n-1) + recFibonacci(n-2)
    

print(fibonacci(9))
print(recFibonacci(9))


            
        # i = 0 
        # First_Value = 1
        # Second_Value =2
        # if(self.number <= 0):
        #     Next = i
        # else:
        #     while(i < self.number):
        #         Next = First_Value + Second_Value
        #         First_Value = Second_Value
        #         Second_Value = Next
        #         i = i + 1
        # return Next