def fl(funcion,lista):
    l=[]
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n*n

print(fl(cuadrado,[1,4,5,7,8]))