from numpy import sin, cos
def f(x):
    return x**2
def g(x,y):
    if len(x)==len(y):
        return sin(x)*cos(y)
    else:
        return "Error: Ambas variables deben tener la misma cantidad de valores"

def h(x,y,z):
    if len(x)==len(y) and len(z)==len(y):
        return x*y*z
    else:
        return "Error: Las tres variables deben tener la misma cantidad de valores"

class Funcion:
    def __init__(self, expresion, variables):
        self.expresion = expresion
        self.variables = variables
    def evaluar(self,*valores):
        variables_dict = dict(zip(self.variables, valores))
        if len(valores) == len(self.variables):
            resultado = eval(self.expresion, variables_dict)
            return resultado
        else:
            return "Error: La cantidad de valores ingresados no coincide con la cantidad de variables"