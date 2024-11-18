def palabras(s):
    p=s.split()
    largo=map(len,p)
    return dict(zip(p,largo))

print(palabras("Bienvenido a python"))