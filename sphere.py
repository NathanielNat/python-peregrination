

# 4/3 pi r 3
import math

def sphere(rad):
    """function to caculate the volume fo a sphere"""
    return ((4/3)* math.pi * math.pow(rad,3))

my_sphere = sphere(7)
# print(my_sphere)


def ran_check(num,low,high):
    if num in range(low,high):
        return True
    else:
        return False

check   = ran_check(18,4,9)
print(check)