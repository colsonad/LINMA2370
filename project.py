import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 
from matplotlib.collections import PolyCollection

def rate_change(t,T) : 
    r = r_m * R/(h_R + R)
    return r*T*(1-T/k) - m_n*T*h_n/(T+h_n)-m_f*T*(h_f)**p/((T)**p+(h_f)**p)
    
r_m=0.3
h_R=0.5
m_n=0.15
h_n=0.1
m_f=0.11
h_f=0.6
p=7
k=0.9
b=2
r_R=1


t_start =0
t_end = 600
R_ = np.linspace(0,5,100)
T_0 = [0.05, 0.25, 0.50, 0.75, 1]



for i in range(len(T_0)) :
    fig=plt.figure()
    ax = fig.add_subplot(projection='3d')
    for r in R_ :  
        R=r
        sol = solve_ivp(rate_change,(t_start,t_end),[T_0[i]])
        ax.plot(sol.t,sol.y[0],zs=r,zdir='y')
    ax.set(xlim=(0, 600), ylim=(0, 5), zlim=(0, 1),
        xlabel='t', ylabel='R', zlabel='T')
    plt.show()