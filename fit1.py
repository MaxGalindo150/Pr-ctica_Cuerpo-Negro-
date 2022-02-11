import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.font_manager import FontProperties


def run():
    df = pd.read_csv('./data/datos.csv') 
    
    def f1(x, a0, a1):
        return a0 + a1*x

    results, cov = curve_fit(f1, df['T'], df['E'])
    print(results)


    x = np.linspace(0,12,100)   
    
   
    fig, ax = plt.subplots()
    ax.scatter(df['T'], df['E'], marker = 'o', color='red', label="Puntos Exp.")
    ax.plot(x,f1(x,results[0],results[1]), label="$E_{T}(T) = -553.28 + 109.87 T$", linewidth=2)
    plt.xlim(3,15)
    plt.ylim(-10,850)
    plt.legend(loc='upper left')
    plt.xlabel("T [kK]", fontsize='large', fontweight='bold')
    plt.ylabel("E [MW/m²]", fontsize='large', fontweight='bold')
    plt.show()

if __name__ == "__main__":
    run()