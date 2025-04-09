from numpy import sin, cos
def f(x):
    fdex = []
    for i in x:
        fdex.append(i**2)
    return fdex
    
def g(x,y):
    gdexy = []
    if len(x)==len(y):
        for i in range(len(x)):
            gdexy.append(sin(x[i])*cos(y[i]))
        return gdexy
    else:
        return "Error: Ambas variables deben tener la misma cantidad de valores"

def h(x,y,z):
    hdexyz = []
    if len(x)==len(y) and len(z)==len(y):
        for i in range(len(x)):
            hdexyz.append(x[i]*y[i]*z[i])
        return hdexyz
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