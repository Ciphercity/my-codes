def less_than_five(x):
    return x<5
nums=[1,2,3,4,5,6,7,8,9,10,11]
res=list(filter(less_than_five,nums))
print(res)    