# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
from funcfactory_singleton import funcfactory_singleton
# from funcfactory import funcfactory

##
# PSO算法一些参数说明:
# weight 惯性权重w
# pop 粒子位置向量可理解为[pop1,pop2,pop3......popn]
# v 粒子速度向量可理解为[v1,v2,v3,......vn]
# rangespeed 速度范围 rangepop 位置范围
# lr 因子参数向量 可理解为(c1,c2)
# fitness 适应度值 PSO算法中规定：适应度越大，当前粒子位置越逼近最优解 
# 所以目标函数值要取反以求其最大值，即得最优解
##
class PSO:
    def getweight(self):
        # 惯性权重
        weight = 0.9
        return weight

    def getlearningrate(self):
        # 分别是粒子的个体和社会的学习因子，也称为加速常数
        lr = (1.49445,1.49445)
        return lr

    def getmaxgen(self):
        # 最大迭代次数
        maxgen = 25
        return maxgen

    def getsizepop(self):
        # 种群规模
        sizepop = 20
        return sizepop

    def getrangepop(self,min=-100.0,max=100.0):
        # 粒子的位置的范围限制,x、y方向的限制相同
        # self.rangepop = (-2*math.pi , 2*math.pi)
        self.rangepop = (min,max)
        #rangepop = (-2,2)
        return self.rangepop

    def getrangespeed(self):
        # 粒子的速度范围限制
        rangespeed = (-0.5,0.5)
        return rangespeed

    def func(self,x):
        # x 输入粒子位置
        # y 粒子适应度值
        if (x[0]==0)&(x[1]==0):
            y = np.exp((np.cos(2*np.pi*x[0])+np.cos(2*np.pi*x[1]))/2)-2.71289
        # else:
        #     y = np.sin(np.sqrt(x[0]**2+x[1]**2))/np.sqrt(x[0]**2+x[1]**2)+np.exp((np.cos(2*np.pi*x[0])+np.cos(2*np.pi*x[1]))/2)-2.71289
        # return y
        else:
            factory = funcfactory_singleton()
            # factory = funcfactory()
            # print(factory)
            y = factory.createfuncByName(self.fitnessfuncname,x[0],x[1])
        return y

    def initpopvfit(self,sizepop):
        pop = np.zeros((sizepop,2))
        v = np.zeros((sizepop,2))
        fitness = np.zeros(sizepop)

        for i in range(sizepop):
            pop[i] = [(np.random.rand()-0.5)*self.rangepop[0]*2,(np.random.rand()-0.5)*self.rangepop[1]*2]
            v[i] = [(np.random.rand()-0.5)*self.rangepop[0]*2,(np.random.rand()-0.5)*self.rangepop[1]*2]
            fitness[i] = self.func(pop[i])
        return pop,v,fitness

    def getinitbest(self,fitness,pop):
        # 群体最优的粒子位置及其适应度值
        gbestpop,gbestfitness = pop[fitness.argmax()].copy(),fitness.max()
        #个体最优的粒子位置及其适应度值,使用copy()使得对pop的改变不影响pbestpop，pbestfitness类似
        pbestpop,pbestfitness = pop.copy(),fitness.copy()

        return gbestpop,gbestfitness,pbestpop,pbestfitness  

    def run(self,fitnessfuncname):
        self.fitnessfuncname = fitnessfuncname
        w = self.getweight()
        lr = self.getlearningrate()
        maxgen = self.getmaxgen()
        sizepop = self.getsizepop()
        rangepop = self.getrangepop()
        rangespeed = self.getrangespeed()

        pop,v,fitness = self.initpopvfit(sizepop)
        gbestpop,gbestfitness,pbestpop,pbestfitness = self.getinitbest(fitness,pop)
        
        # 初始化结果
        result = np.zeros(maxgen)
        for i in range(maxgen):
                t=0.5
                #速度更新
                for j in range(sizepop):
                    v[j] = w*v[j]+lr[0]*np.random.rand()*(pbestpop[j]-pop[j])+lr[1]*np.random.rand()*(gbestpop-pop[j])
                # v[v<rangespeed[0]] = rangespeed[0]
                # v[v>rangespeed[1]] = rangespeed[1]
                np.putmask(v,v<rangespeed[0],rangespeed[0])
                np.putmask(v,v>rangespeed[1],rangespeed[1])

                #粒子位置更新
                for j in range(sizepop):
                    #pop[j] += 0.5*v[j]
                    pop[j] = t*v[j]+(1-t)*pop[j]
                # pop[pop<rangepop[0]] = rangepop[0]
                # pop[pop>rangepop[1]] = rangepop[1]
                np.putmask(pop,pop<rangepop[0],rangepop[0])
                np.putmask(pop,pop>rangepop[1],rangepop[1])

                #适应度更新
                for j in range(sizepop):
                    fitness[j] = self.func(pop[j])

                for j in range(sizepop):
                    if fitness[j] > pbestfitness[j]:
                        pbestfitness[j] = fitness[j]
                        pbestpop[j] = pop[j].copy()

                if pbestfitness.max() > gbestfitness :
                    gbestfitness = pbestfitness.max()
                    gbestpop = pop[pbestfitness.argmax()].copy()

                result[i] = gbestfitness
        return result,gbestpop,pbestfitness