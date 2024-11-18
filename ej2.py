from math import sin,cos,tan,exp,log

def aplicar_funcion(f,n):
    funciones={"sin":sin,"cos":cos,"tan":tan,"exp":exp,"log":log}
    resultado={}
    for i in range(n+1):
        resultado[i]=funciones[f](i)
    return resultado

def calculadora():
    f=input("Ingresa la funcion a aplicar(sin,cos,tan,exp,log): ")
    n= int(input("Ingresa un numero entero positivo: "))
    for i, j in aplicar_funcion(f,n).items():
        print(i,"\t",j)
    return

calculadora()