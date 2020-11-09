import time

# print(time.time())

def calProd():
    '''calculate the product of the first 10000 numbers'''
    product =1
    for i in range(1,1000):
        product = product * i
    return product

start_time = time.time()
prod = calProd()
endTime = time.time()

print('The result of the is %s digits long.' %(len(str(prod))))
print('The operaton was done in %s seconds'% (endTime - start_time))
# cProfile.run()