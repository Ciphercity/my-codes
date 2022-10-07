def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i
res=tuple (numbers(11))
print(res)

             