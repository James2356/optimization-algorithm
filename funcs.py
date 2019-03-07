import numpy as np
# 我们定义的函数类 都是二维函数
class funcs:
    # rastrigin测试函数
    def Rastrigin(self,X,Y):
        A = 10
        Z = 2 * A + X ** 2 - A * np.cos(2 * np.pi * X) + Y ** 2 - A * np.cos(2 * np.pi * Y)
        # 取反
        Z = -Z
        return Z 


    # Ackley测试函数
    def Ackley(self,X,Y):
        Z = -20 * np.exp(-0.2 * np.sqrt(0.5 * (X**2 + Y**2))) - \
            np.exp(0.5 * (np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y))) + np.e + 20
        Z = -Z
        return Z


    # Sphere测试函数
    def Sphere(self,X,Y):
        Z = X**2 + Y**2
        Z = -Z
        return Z


    #  beale测试函数
    def Beale(self,X,Y):
        Z = np.power(1.5 - X + X * Y, 2) + np.power(2.25 - X + X * (Y ** 2), 2) \
            + np.power(2.625 - X + X * (Y ** 3), 2)
        Z= -Z        
        return Z


    # Booth测试函数
    def Booth(self,X,Y):
        Z = np.power(X + 2*Y - 7, 2) + np.power(2 * X + Y - 5, 2)
        Z= -Z        
        return Z


    # Bukin测试函数
    def Bukin(self,X,Y):
        Z = 100 * np.sqrt(np.abs(Y - 0.01 * X**2)) + 0.01 * np.abs(X + 10)
        Z= -Z 
        return Z

    #  Three-hump camel测试函数
    def three_humpCamel(self,X,Y):
        Z = 2 * X**2 - 1.05 * X**4 + (1/6) * X**6 + X*Y + Y*2
        Z= -Z        
        return Z

    # Hölder table测试函数
    def Holder_table(self,X,Y):
        Z = -np.abs(np.sin(X) * np.cos(Y) * np.exp(np.abs(1 - np.sqrt(X**2 + Y**2)/np.pi)))
        Z= -Z
        return Z