def notas(puntos):
    if puntos < 5:
       return "SS"
    elif puntos < 7:
        return "AP"
    elif puntos < 9:
        return "NT"
    elif puntos < 10:
        return "SB"
    else:
        return "MH"

def aplicar_notas(puntos):
    return [notas(x) for x in puntos]

print(aplicar_notas([6.5,5,7.6,9,10,3]))