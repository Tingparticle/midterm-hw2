import math
def sd_function(numbers):
    'self-defined sd function'
    N=len(numbers)
    summation = 0
    another_summation = 0
    for number in numbers:
        summation += number
    mu = summation / N
    for number in numbers:
        another_summation += (number - mu)**2
    return(math.sqrt(another_summation/N))     
my_list = range(1,6)
print(sd_function(my_list))

help(sd_function)