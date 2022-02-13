import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from sklearn.linear_model import LinearRegression

def f(x, m, b):
    return m*x + b

def run():
    df = pd.read_csv('./data/datos.csv') 
    
    T = df['T']
    E = df['E']
    T4 = []
    El = []

    for i in range(len(T)):
        T4.append((T[i])**4)
        El.append(E[i])

    T4 = np.array(T4)
    En = np.array(El)

    reg = LinearRegression()
    reg.fit(T4.reshape(-1,1), En)

    m = float(reg.coef_)
    b = reg.intercept_


    print("m = ", m, " b = ", b) 

    x = np.linspace(0,15000,100)   
    
   
    fig, ax = plt.subplots()
    ax.scatter(T4, En, marker = 'o', color='red', label="Puntos Exp.")
    ax.plot(x,f(x, m, b), label="0.05669 x - 0.06463", linewidth=2)
    plt.xlim(0,15500)
    plt.ylim(0,900)
    plt.legend(loc='upper left')
    plt.xlabel("$T^{4} [k^{4}K^{4}]$", fontsize='large', fontweight='bold')
    plt.ylabel("$E [MW/m^{2}]$", fontsize='large', fontweight='bold')
    plt.show()

if __name__ == "__main__":
    run()