from sympy import *
import numpy as np

n=5000

def Logistic(x,n):
    for i in range(n):
        y = 4 * x * (1 - x)
        x = y
    return x

def LE_calculate():
    a = 0.123456789  # 混沌的初始值
    count = 0
    sum_value = 0  # 初始的求和值为0
    x = symbols('x')
    expr = 4 * x * (1 - x)  # 表达式
    diff_expr = diff(expr, x)  # 对表达式进行求导,得到导数的表达式。该表达式固定（带参数）
    # 先迭代混沌方程1000次消除初始影响,以第1001次的返回值作为初值
    a = Logistic(a, 1001)
    while (count < n):
        diff_value = diff_expr.subs(x, a)  # 带入当前迭代值，得到当前的导数值(数值)
        diff_value_ln = ln(abs(diff_value))  # 对当前导数值取绝对值然后取对数
        sum_value = sum_value + diff_value_ln  # 计算求和值
        a = Logistic(a, 1)  # 每次只迭代一次，获取当前的迭代值
        count = count + 1
    LE_value = sum_value / n
    print(LE_value)





# 4.57232016110001

np.set_printoptions(suppress=True)
U = 4
N = 64
n=40000
def PLM(x,n):
    for z in range(n):
        M=float(N)
        i=int(x*M)+1#i是一个整数，从0-N
        k=float(i)
        if(x==1):
            x1=x-1/(100*M)
        elif (i==x*M+1):
            x1=x+1/(100*M)
        elif(i%2==1):
            x1=M*M*U*(x-(k-1)/M)*(k/M-x)
        else:
            x1=1-M*M*U*(x-(k-1)/M)*(k/M-x)
        x=x1
    return x

def diff_expr_calculate(a):
    x = symbols('x')
    M = float(N)
    i = int(a * M) + 1
    k = float(i)
    if (a == 1):
        expr1 = x - 1 / (100 * M)
        diff_expr1 = diff(expr1, x)
        return diff_expr1
    elif (i == a * M + 1):
        expr2 = x + 1 / (100 * M)
        diff_expr2 = diff(expr2, x)
        return diff_expr2
    elif (i % 2 == 1):
        expr3 = M * M * U * (x - (k - 1) / M) * (k / M - x)
        diff_expr3 = diff(expr3, x)
        return diff_expr3
    else:
        expr4 = 1 - M * M * U * (x - (k - 1) / M) * (k / M - x)
        diff_expr4 = diff(expr4, x)
        return diff_expr4

# def LE_calculate():
#     a = 0.123456789  # 混沌的初始值
#     sum_value = 0  # 初始的求和值为0
#     x = symbols('x')
#     a = PLM(a, 1001)
#     for i in range(n):
#         diff_expr=diff_expr_calculate(a)   #根据不同的迭代值，得到不同的求导表达式
#         diff_value = diff_expr.subs(x, a)  # 带入当前迭代值，得到当前的导数值(数值)
#         diff_value_ln = ln(abs(diff_value))  # 对当前导数值取绝对值然后取对数
#         sum_value = sum_value + diff_value_ln  # 计算求和值
#         a = PLM(a, 1)  # 每次只迭代一次，获取当前的迭代值
#         print(i)
#     LE_value = sum_value / n
#     print(LE_value)


if __name__ == '__main__':
    LE_calculate()