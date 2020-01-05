#Define a function even_or_odd, which takes an integer as input and returns the string even and odd, if the given number is even and odd respectively.
#Categorise the numbers of list n = [10, 14, 16, 22, 9, 3 , 37] into two groups namely even and odd based on above defined function.
#Hint : Use groupby method of itertools module.
#Iterate over the obtained groupby object and print it's group name and list of elements associated with a group.

from itertools import *

def even_or_odd(x):
    if x%2==0:
        return 'even'
    else:
        return 'odd'

n = [10, 14, 16, 22, 9, 3 , 37]

even = ['even']
odd = ['odd']

dict = {}

for item in n:
    isEvenOrOdd = even_or_odd(item)
    if isEvenOrOdd=='even':
        dict[item] = 'even'
    else:
        dict[item] = 'odd'
    
#convert dict to list
dictlist = []
for key, value in dict.items():
    temp = [key,value]
    dictlist.append(temp)

from operator import itemgetter

even = []
odd = []

for key, items in groupby(dictlist, itemgetter(1)):
    for i in items:
        if i[0]%2==0:
            even.append(i[0])
        else:
            odd.append(i[0])
    if key=='even':
        print({key : even})
    else:
        print({key : odd})
