def sum_cuadrados(x,y):
    return x+y**2 

def modulo(v):
    from functools import reduce
    return reduce(sum_cuadrados,v,0)**0.5

print(modulo((3,4)))
print(modulo(((3,5,6))))