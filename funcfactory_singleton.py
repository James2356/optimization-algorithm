import threading
import numpy as np
from funcs import funcs

class funcfactory_singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    # 实例化时先执行该方法，保证任何初始化方式都可以实现单例
    def __new__(cls, *args, **kwargs):
        if not hasattr(funcfactory_singleton, "_instance"):
            with funcfactory_singleton._instance_lock:
                if not hasattr(funcfactory_singleton, "_instance"):
                    funcfactory_singleton._instance = object.__new__(cls)  
        return funcfactory_singleton._instance

    def createfuncByName(self,funcname,X,Y):
        if(funcname=='Rastrigin'):
            return funcs().Rastrigin(X,Y)
        if(funcname=='Ackley'):
            return funcs().Ackley(X,Y)
        if(funcname=='Sphere'):
            return funcs().Sphere(X,Y)
        if(funcname=='Booth'):
            return funcs().Booth(X,Y)
        if(funcname=='Beale'):
            return funcs().Beale(X,Y)
        if(funcname=='Bukin'):
            return funcs().Bukin(X,Y)
        if(funcname=='Holder-Table'):
            return funcs().Holder_table(X,Y)
        return funcs().three_humpCamel(X,Y)
            