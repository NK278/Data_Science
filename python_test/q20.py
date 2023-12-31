from functools import reduce
l=[12,13,14,66,77,99,100]
res=reduce( lambda x,y: y-x, l)
print(res)
    