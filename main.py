import numpy as np
import os
import shutil as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PSO import PSO
from LWDPSO import LWDPSO

class funcpic:
    def __init__(self,cmapval='hot',fig=1,fig_contour=1):
        self.cmapval = cmapval
        self.fig = fig
        self.fig_contour = fig_contour
    def funcPic_3D(self,X, Y, Z, z_max, title, z_min=0,num=111):
        if(self.fig!=1):
            ax = self.fig.add_subplot(num,projection='3d')
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=self.cmapval)
            # ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=self.cmapval)
            ax.set_zlim(z_min, z_max)
            ax.set_title(title)
            # plt.savefig("./myProject/Algorithm/pic/%s.png" % title) # 保存图片
            # plt.show()
        else:
            print("give a instance of figure")

    def funcPic_contour(self,X,Y,Z,z_max,title,z_min=0,num=111):
        if(self.fig_contour!=1):
            ax = self.fig_contour.add_subplot(num,projection='3d')
            # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=self.cmapval)
            ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=self.cmapval)
            ax.set_zlim(z_min, z_max)
            ax.set_title(title)
    
    def funcPic_all(self,X,Y,Z,z_max,title,z_min=0,num=111):
        self.funcPic_3D(X,Y,Z,z_max,title,z_min,num)
        self.funcPic_contour(X,Y,Z,z_max,title,z_min,num)
    
    # def SaveFig_all(self):
    #     plt.savefig()

    def get_X_AND_Y(self,X_min, X_max, Y_min, Y_max):
        X = np.arange(X_min, X_max, 0.1)
        Y = np.arange(Y_min, Y_max, 0.1)
        X, Y = np.meshgrid(X, Y)
        return X, Y


    #  rastrigin测试函数
    def Rastrigin(self,X_min = -5.12, X_max = 5.12, Y_min = -5.12, Y_max = 5.12):
        A = 10
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = 2 * A + X ** 2 - A * np.cos(2 * np.pi * X) + Y ** 2 - A * np.cos(2 * np.pi * Y)
        return X, Y, Z, 100, "Rastrigin function"


    # Ackley测试函数
    def Ackley(self,X_min = -5, X_max = 5, Y_min = -5, Y_max = 5):
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = -20 * np.exp(-0.2 * np.sqrt(0.5 * (X**2 + Y**2))) - \
            np.exp(0.5 * (np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y))) + np.e + 20
        return X, Y, Z, 15, "Ackley function"


    # Sphere测试函数
    def Sphere(self,X_min = -3, X_max = 3, Y_min = -3, Y_max = 3):
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = X**2 + Y**2
        return X, Y, Z, 20, "Sphere function"


    #  beale测试函数
    def Beale(self,X_min = -4.5, X_max = 4.5, Y_min = -4.5, Y_max = 4.5):
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = np.power(1.5 - X + X * Y, 2) + np.power(2.25 - X + X * (Y ** 2), 2) \
            + np.power(2.625 - X + X * (Y ** 3), 2)
        return X, Y, Z, 150000, "Beale function"


    # Booth测试函数
    def Booth(self,X_min = -10, X_max = 10, Y_min = -10, Y_max = 10):
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = np.power(X + 2*Y - 7, 2) + np.power(2 * X + Y - 5, 2)
        return X, Y, Z, 2500, "Booth function"


    # Bukin测试函数
    def Bukin(self,X_min = -15, X_max = -5, Y_min = -3, Y_max = 3):
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = 100 * np.sqrt(np.abs(Y - 0.01 * X**2)) + 0.01 * np.abs(X + 10)
        return X, Y, Z, 200, "Bukin function"


    #  Three-hump camel测试函数
    def three_humpCamel(self,X_min = -5, X_max = 5, Y_min = -5, Y_max = 5):
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = 2 * X**2 - 1.05 * X**4 + (1/6) * X**6 + X*Y + Y*2
        return X, Y, Z, 2000, "three-hump camel function"


    # Hölder table测试函数
    def Holder_table(self,X_min = -10, X_max = 10, Y_min = -10, Y_max = 10):
        X, Y = self.get_X_AND_Y(X_min, X_max, Y_min, Y_max)
        Z = -np.abs(np.sin(X) * np.cos(Y) * np.exp(np.abs(1 - np.sqrt(X**2 + Y**2)/np.pi)))
        # Z = -Z
        return X, Y, Z, 0, "Hölder table function", -20
    # def GetFunc(self):

if __name__ == "__main__":
    # 测试函数
    z_min = None
    # 绘制测试函数图像
    fig = plt.figure(figsize=(12,7))
    fig_contour = plt.figure(figsize=(12,7))
    # testobj = funcpic('gray',fig)
    # testobj = funcpic('hot',fig,fig_contour)
    # X, Y, Z, z_max, title = testobj.Rastrigin()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,331)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,331)
    # X, Y, Z, z_max, title = testobj.Ackley()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,332)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,332)
    # X, Y, Z, z_max, title = testobj.Sphere()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,333)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,333)
    # X, Y, Z, z_max, title = testobj.Beale()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,334)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,334)
    # X, Y, Z, z_max, title = testobj.Booth()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,335)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,335)
    # X, Y, Z, z_max, title = testobj.Bukin()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,336)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,336)
    # X, Y, Z, z_max, title = testobj.three_humpCamel()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,337)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,337)
    # X, Y, Z, z_max, title, z_min = testobj.Holder_table()
    # # testobj.funcPic_3D(X, Y, Z, z_max, title, z_min,338)
    # testobj.funcPic_all(X, Y, Z, z_max, title, z_min,338)

    # plt.savefig("%s.jpg" % "result")
    # # 绘制迭代的适应度数据图 初始化部分
    # plt.figure()

    # PSO算法
    psoobj = PSO()
    LWDobj = LWDPSO()
    # 函数名称:
    # Rastrigin,Ackley,Sphere,Beale,Booth,Bukin
    # Three-hump-camel,Holder-Table
    
    labelpara = 'Rastrigin'
    result,bestpop,pbestfitness = psoobj.run(labelpara)
    x = np.arange(0,result.size,1)
    plt.plot(x,-result,'x--b',label="PSO")

    # labelpara = 'Rastrigin'
    result,bestpop,pbestfitness = LWDobj.run(labelpara)
    x = np.arange(0,result.size,1)
    plt.plot(x,-result,'d-r',label="LWDPSO")

    # labelpara = 'Ackley'
    # result,bestpop,pbestfitness = psoobj.run(labelpara)
    # x = np.arange(0,result.size,1)
    # plt.plot(x,-result,'x:m',label="PSO")

    # result,bestpop,pbestfitness = LWDobj.run(labelpara)
    # x = np.arange(0,result.size,1)
    # plt.plot(x,-result,'d-.y',label="LWDPSO")

    # labelpara = 'Sphere'
    # result,bestpop,pbestfitness = psoobj.run(labelpara)
    # x = np.arange(0,result.size,1)
    # plt.plot(x,-100*result,'o--g',label="PSO")

    # result,bestpop,pbestfitness = LWDobj.run(labelpara)
    # x = np.arange(0,result.size,1)
    # plt.plot(x,-100*result,'s-r',label="LWDPSO")

    plt.legend()
    plt.title("Rastrigin function optimization")
    plt.xlabel("iterations")
    plt.ylabel("Test Function Value")
    plt.show()


