
import datetime


def sum(a, b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a + b, None
        if type(b) == str:
            try:
                datetime.datetime.strptime(b.replace("'",""), '%Y-%m-%d')
                return None, "Error: No se puede sumar un entero con una fecha"
            except:
                return "'" + str(a) + b.replace("'","") + "'", None
    if type(a) == str:
        try:
            datetime.datetime.strptime(a.replace("'",""), '%Y-%m-%d')
            return None, "Error: No se puede sumar una fecha con un ningun tipo de dato"
        except:
            return "'" + a.replace("'","") + str(b) + "'", None
    print(type(a), type(b))
    return None, "Error: tipo de dato no soportado"

