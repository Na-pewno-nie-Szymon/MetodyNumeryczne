import numpy as np 
import matplotlib.pyplot as plt

def f(x: list):
    S = x[0]
    E = x[1]
    I = x[2]
    R = x[3]

    ds = -(beta * I * S)
    de = (beta * I * S) - sigma * E
    di = sigma * E - gamma * I
    dr = gamma * I

    return np.array([ds, de, di, dr])

def Runge_Kutta_4(x, t, dt):
    f1 = dt * f(x)
    f2 = dt * f(x + f1 / 2.)
    f3 = dt * f(x + f2 / 2.)
    f4 = dt * f(x + f3)

    next_x = x + 1/6 * (f1 + 2 * f2 + 2 * f3 + f4)
    return next_x

def zadanie_1():
    global gamma, sigma, beta, N
    gamma = .1
    sigma = 1
    beta  = 1

    time_start = 0
    time_end = 50
    time_interval = .01
    time_frame = np.arange(time_start, time_end, time_interval)

    S = .99
    E = .01
    I = 0
    R = 0

    x = np.zeros([time_frame.shape[0], 4])
    x[0, 0] = S
    x[0, 1] = E
    x[0, 2] = I
    x[0, 3] = R

    for i in range(time_frame.shape[0] - 1):
        x[i+1] = Runge_Kutta_4(x[i], time_frame[i], time_interval)

    t = time_frame.shape[0]
    ST = [x[j, 0] for j in range(t)]
    ET = [x[j, 1] for j in range(t)]
    IT = [x[j, 2] for j in range(t)]
    RT = [x[j, 3] for j in range(t)]

    plt.plot(time_frame, ST, color='blue', label='Susceptible')
    plt.plot(time_frame, ET, color='orange', label='Exposed')
    plt.plot(time_frame, IT, color='red', label='Infectious')
    plt.plot(time_frame, RT, color='grey', label='Removed')
    plt.xlabel('Time[t]')
    plt.ylabel('Normalised population')
    plt.legend()
    plt.show()

def zadanie_2():
    global gamma, sigma, beta, N
    gamma = .1
    sigma = 1
    beta  = .5

    time_start = 0
    time_end = 50
    time_interval = .01
    time_frame = np.arange(time_start, time_end, time_interval)

    S = .99
    E = .01
    I = 0
    R = 0

    x = np.zeros([time_frame.shape[0], 4])
    x[0, 0] = S
    x[0, 1] = E
    x[0, 2] = I
    x[0, 3] = R

    for i in range(time_frame.shape[0] - 1):
        x[i+1] = Runge_Kutta_4(x[i], time_frame[i], time_interval)

    t = time_frame.shape[0]
    ST = [x[j, 0] for j in range(t)]
    ET = [x[j, 1] for j in range(t)]
    IT = [x[j, 2] for j in range(t)]
    RT = [x[j, 3] for j in range(t)]

    plt.plot(time_frame, ST, color='blue', label='Susceptible')
    plt.plot(time_frame, ET, color='orange', label='Exposed')
    plt.plot(time_frame, IT, color='red', label='Infectious')
    plt.plot(time_frame, RT, color='grey', label='Removed')
    plt.legend()
    plt.ylabel('Normalised population')
    plt.xlabel('Time[t]')
    plt.show()

def zadanie_3_smaller_R():
    global gamma, sigma, beta, N
    gamma = .6
    sigma = 1
    beta  = .5

    time_start = 0
    time_end = 75
    time_interval = .01
    time_frame = np.arange(time_start, time_end, time_interval)

    S = .99
    E = .01
    I = 0
    R = 0

    R0 = (beta/gamma) * S

    x = np.zeros([time_frame.shape[0], 4])
    x[0, 0] = S
    x[0, 1] = E
    x[0, 2] = I
    x[0, 3] = R

    for i in range(time_frame.shape[0] - 1):
        x[i+1] = Runge_Kutta_4(x[i], time_frame[i], time_interval)

    t = time_frame.shape[0]
    ST = [x[j, 0] for j in range(t)]
    ET = [x[j, 1] for j in range(t)]
    IT = [x[j, 2] for j in range(t)]
    RT = [x[j, 3] for j in range(t)]

    print(R0)

    plt.plot(time_frame, ST, color='blue', label='Susceptible')
    plt.plot(time_frame, ET, color='orange', label='Exposed')
    plt.plot(time_frame, IT, color='red', label='Infectious')
    plt.plot(time_frame, RT, color='grey', label='Removed')
    plt.legend()
    plt.ylabel('Normalised population')
    plt.xlabel('Time[t]')
    plt.show()

def zadanie_3_bigger_R():
    global gamma, sigma, beta, N
    gamma = .6
    sigma = 1
    beta  = 1

    time_start = 0
    time_end = 75
    time_interval = .01
    time_frame = np.arange(time_start, time_end, time_interval)

    S = .99
    E = .01
    I = 0
    R = 0

    R0 = (beta/gamma) * S

    x = np.zeros([time_frame.shape[0], 4])
    x[0, 0] = S
    x[0, 1] = E
    x[0, 2] = I
    x[0, 3] = R

    for i in range(time_frame.shape[0] - 1):
        x[i+1] = Runge_Kutta_4(x[i], time_frame[i], time_interval)

    t = time_frame.shape[0]
    ST = [x[j, 0] for j in range(t)]
    ET = [x[j, 1] for j in range(t)]
    IT = [x[j, 2] for j in range(t)]
    RT = [x[j, 3] for j in range(t)]

    print(R0)

    plt.plot(time_frame, ST, color='blue', label='Susceptible')
    plt.plot(time_frame, ET, color='orange', label='Exposed')
    plt.plot(time_frame, IT, color='red', label='Infectious')
    plt.plot(time_frame, RT, color='grey', label='Removed')
    plt.legend()
    plt.ylabel('Normalised population')
    plt.xlabel('Time[t]')
    plt.show()

if __name__=='__main__':
    zadanie_1()
    zadanie_2()
    zadanie_3_smaller_R()
    zadanie_3_bigger_R()
