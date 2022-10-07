# itertool is a standard library usefull in functional programming
# produces infinite operators
#COUNT = counts infinitely from a value
# cycle= iterates through an iterable
# repeat= repeats an object infinitely or specific number of times
# takewhile=take items from iterable while predicate function remains true
# chain= combines iterable into one long one
#accumulate= returns a running total of values in an iterable 
# Example
from itertools import count

for i in count(-3):
    print(i)
    if i >=20:
        break
