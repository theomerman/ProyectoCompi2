import datetime
def multiply(a, b):
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return a * b, None
        if type(b) is str:
            raise Exception("Error: No se puede multiplicar un numero con un string o fecha")
    if type(a) is str:
        try:
            datetime.datetime.strptime(a.replace("'",""), '%d-%m-%Y')
            if type(b) is int or type(b) is float:
                raise Exception("Error: No se puede multiplicar una fecha con un numero")
            if type(b) is str:
                try:
                    datetime.datetime.strptime(b.replace("'",""), '%d-%m-%Y')
                    print('entro')
                    return None, "Error: No se puede multiplicar fecha con fecha"
                except:
                    return "'" + a.replace("'","") + b.replace("'","") + "'", None

        except:
            if type(b) is int or type(b) is float:
                raise Exception("Error: No se puede multiplicar un string con un numero")
            if type(b) is str:
                try:
                    datetime.datetime.strptime(b.replace("'",""), '%d-%m-%Y')
                    return "'" + a.replace("'","") + b.replace("'","") + "'", None
                except:
                    raise Exception("Error: No se puede multiplicar un string con un string")
    raise Exception("Error: tipo de dato no soportado")