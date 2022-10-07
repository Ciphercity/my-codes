def even_nums(x):
    return x%2==0
nums ={2,3,4,5,6,7,8,9,10,11}
result=list(filter(even_nums,nums))
print(result)