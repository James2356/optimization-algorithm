import numpy as np
from funcs import funcs

class funcfactory:
    def creatfunc(self,funcname,X,Y):
        if(funcname=='rastrigin'):
            return funcs().Rastrigin(X,Y)
        if(funcname=='Ackley'):
            return funcs().Ackley(X,Y)
        if(funcname=='Sphere'):
            return funcs().Sphere(X,Y)
        if(funcname=='Booth'):
            return funcs().Booth(X,Y)
        if(funcname=='beale'):
            return funcs().Beale(X,Y)
        return funcs().three_humpCamel(X,Y)

