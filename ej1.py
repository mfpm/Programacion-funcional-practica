def descuento(precio,descuento):
    #Funcion que aplica descuente
    return precio-precio*descuento/100

def impuesto(precio,porcentaje):
    #Funcion que aplica impuesto
    return precio+precio*porcentaje/100

def total(cesta, funcion):
    total=0
    for precio, descuento in cesta.items():
        total+=funcion(precio,descuento)
    return total

print("El precio de la compra tras aplicar los descuentos es: ",total({1000:20,500:10,2500:35},descuento))
print("El precio despues de aplicar impuestos es ",total({1000:20,500:10,2500:35},impuesto))

