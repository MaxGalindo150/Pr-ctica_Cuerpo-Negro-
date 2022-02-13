import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib.font_manager import FontProperties

def f(x, m, b):
    return m*x + b

def run():
    df = pd.read_csv('./data/datos.csv') 
    
    T = df['T']
    WL = df['WL']
    Tin = []
    wl = []

    for i in range(len(T)):
        Tin.append(1/T[i])
        wl.append(WL[i])
    
    Tin = np.array(Tin)
    wl = np.array(wl)
  
    reg = LinearRegression()
    reg.fit(Tin.reshape(-1,1), wl)    
    
    m = float(reg.coef_)
    b = reg.intercept_


    print("m = ", m, " b = ", b) 
   
    
    x = np.linspace(0,0.25,100)   
    
   
    fig, ax = plt.subplots()
    ax.scatter(Tin, wl, marker = 'o', color='red', label="Puntos Exp.")
    ax.plot(x,f(x, m, b), label="2.898 x - 5.460", linewidth=2)
    plt.xlim(0.05,0.25)
    plt.ylim(0.2,0.7)
    plt.legend(loc='upper left')
    plt.xlabel("$1/T [1/kK]$", fontsize='large', fontweight='bold')
    plt.ylabel("$\lambda [\mu m]$", fontsize='large', fontweight='bold')
    plt.show()

if __name__ == "__main__":
    run()