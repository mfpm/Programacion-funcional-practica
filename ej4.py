def filtra_lista(funcion,lista):
    l=[]
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def par(n):
    return n%2==0

print(filtra_lista(par,[1,2,3,4,5,6,7,8]))