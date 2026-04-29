import numpy as np
import seaborn as sns
from black_scholes_formula import black_scholes
import matplotlib.pyplot as plt

def calculate_data(r,S_min,S_max,T,V_min,V_max,K):
    call_data=np.zeros((10,10))
    put_data=np.zeros((10,10))

    V=np.linspace(V_min,V_max,10)
    S=np.linspace(S_min,S_max,10)
    
    for i in range(10):
        for j in range(10):
            output = black_scholes(r,S[j],T,V[i],K)
            call_data[i,j]=output[0]
            put_data[i,j]=output[1]
    return(call_data,put_data,V,S)

def visualize_black_scholes(call_data,put_data,V,S):
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    cmap = sns.color_palette("flare", as_cmap=True)
    sns.heatmap(call_data,cmap=cmap,yticklabels=np.round(V,2),annot=True,fmt=".2f",ax=ax1)
    ax1.set_xlabel("Spot Price")
    ax1.set_xticklabels(np.round(S,2),rotation=0)
    ax1.set_ylabel("Volatility")
    ax1.tick_params(axis='x', labelsize=7)
    ax1.tick_params(axis='y', labelsize=7)
    ax1.set_title("CALL")
    sns.heatmap(put_data,cmap=cmap,yticklabels=np.round(V,2),annot=True,fmt=".2f",ax=ax2)
    ax2.set_xlabel("Spot Price")
    ax2.set_xticklabels(np.round(S,2),rotation=0)
    ax2.set_ylabel("Volatility")
    ax2.tick_params(axis='x', labelsize=7)
    ax2.tick_params(axis='y', labelsize=7)
    ax2.set_title("PUT")
    return fig1, fig2