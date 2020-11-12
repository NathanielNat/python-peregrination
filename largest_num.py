smallest = None 

print('smallest number at the beginning is %s'%(smallest))

for i  in [7,3,5,6,0,54,3,567,8,9,2345,3]:
    if smallest is None or i <  smallest:
        smallest = i
        continue
   

print('smallest number in list is %s' %smallest)