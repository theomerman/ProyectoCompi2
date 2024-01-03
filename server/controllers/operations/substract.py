
def substract(a, b):
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return a - b
        if type(b) is str:
            raise Exception("Error: No se puede restar un numero con un string o fecha")
    raise Exception("Error: tipo de dato no soportado")
        
