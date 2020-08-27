import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# constants
S_naught = 99
I_naught = 1
R_naught = 0
N = S_naught + R_naught + I_naught
beta = 0.5
gamma = 0.01
time_len = 100

def calcDerivs(initial, t):
    S, I, R = initial
    dS = -1 * beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return dS, dI, dR

def calcResults():
    t = np.linspace(0, time_len, time_len*2)
    initial_conditions = S_naught, I_naught, R_naught
    result = odeint(calcDerivs, initial_conditions, t)
    #print(result)

    plt.plot(t, result[:,0], color = 'blue', label = "Susceptible")
    plt.plot(t, result[:,1], color = 'red', label = "Infected")
    plt.plot(t, result[:,2], color = 'green', label = "Recovered")
    plt.show()

calcResults()


