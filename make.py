def make_name(x):
    name =""
    for c in x:
        name+=c
        yield name
print(list(make_name("junior")))