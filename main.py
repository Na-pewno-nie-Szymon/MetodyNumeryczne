import numpy as np
import matplotlib.pyplot as plt
import hunter_prey_model as hpm

def zadanie_1():
    K = 100000  # max quantity
    r = .4      # growth factor

    t0 = 75     # starting point
    tf = 115    # limit point
    interval = 1000 

    timeline = np.linspace(t0, tf, interval) 
    h = abs(timeline[1] - timeline[0]) # difference between two time points

    # Gompertz equation
    gompertz = np.zeros(interval)
    gompertz[0] = 10

    for i in range(1, interval):
        gompertz[i] = gompertz[i-1] + h * r * gompertz[i-1] * np.log(K/gompertz[i-1])
    
    # Verhult equation
    verhulst = np.zeros(interval)
    verhulst[0] = 10

    for i in range(1, interval):
        verhulst[i] = verhulst[i-1] + h * r * verhulst[i - 1] * (1 - verhulst[i-1]/K)    


    # Visual graph
    plt.plot(timeline, gompertz, label='Równanie Gompertza')
    plt.plot(timeline, verhulst, label='Równanie Verhulsta')
    plt.ylabel('Quantity of population')
    plt.xlabel('Time')
    plt.title('Comparison of Gompertz and Verhulst equations (1st graph)')
    plt.legend()
    plt.show()
    
def zadanie_2_part_1():
    przyklad_a = hpm.HunterPreyModel(1.25, .5, .5, .2, .1, .2)
    n1_a = przyklad_a.N1
    n2_a = przyklad_a.N2
    
    przyklad_b = hpm.HunterPreyModel(5, 5, 4, 8, 1, 4)
    n1_b = przyklad_b.N1
    n2_b = przyklad_b.N2

    timeline = przyklad_a.timeline
 
    
    plt.plot(timeline, n1_a, color='#6666ff', label='N1 a')
    plt.plot(timeline, n2_a, color='#0000b2', label='N2 a')
    plt.plot(timeline, n1_b, color='#ffd27f', label='N1 b')
    plt.plot(timeline, n2_b, color='#cc8400', label='N2 b')
    plt.ylabel('Population')
    plt.xlabel('Time [t]')
    plt.title('Comparrison of different predefined values (2nd graph)')
    plt.legend()
    plt.show()

def zadanie_2_part_2():
    # New predefined values
    epsilon1 = .8
    gamma1 = 1
    h1 = .3

    epsilon2 = .4
    gamma2 = .5
    h2 = .4

    

    # Test examples for different starting values
    przyklad_c = hpm.HunterPreyModel(epsilon1, epsilon2, gamma1, gamma2, h1, h2, n1_init=4, n2_init=8)
    przyklad_d = hpm.HunterPreyModel(epsilon1, epsilon2, gamma1, gamma2, h1, h2, n1_init=8, n2_init=8)
    przyklad_e = hpm.HunterPreyModel(epsilon1, epsilon2, gamma1, gamma2, h1, h2, n1_init=12, n2_init=8)

    n1_c, n2_c = przyklad_c.N1, przyklad_c.N2
    n1_d, n2_d = przyklad_d.N1, przyklad_d.N2
    n1_e, n2_e = przyklad_e.N1, przyklad_e.N2

    timeline = przyklad_c.timeline
    
    # Visual graphs
    plt.plot(timeline, n1_c, label='N1')
    plt.plot(timeline, n2_c, label='N2')
    plt.show()
    plt.plot(timeline, n1_d, label='N1')
    plt.plot(timeline, n2_d, label='N2')
    plt.show()
    plt.plot(timeline, n1_e, label='N1')
    plt.plot(timeline, n2_e, label='N2')
    plt.show()
    

    # Phase portrait
    x = np.linspace(0, 13, 26)
    y = np.linspace(0, 13, 26)

    X, Y = np.meshgrid(x, y)

    dX = np.zeros(X.shape)
    dY = np.zeros(Y.shape)


    for i in range(X.shape[0]): # nie rozumiem
        for j in range(Y.shape[0]):
            dX[i, j] = (epsilon1 - gamma1 * (h1 * X[i, j] + h2 * Y[i, j])) * X[i, j]
            dY[i, j] = (epsilon2 - gamma2 * (h1 * X[i, j] + h2 * Y[i, j])) * Y[i, j]

    plt.quiver(X, Y, dX, dY)
    plt.plot(n1_c, n2_c, label='N1 = 4, N2 = 8')
    plt.plot(n1_d, n2_d, label='N1 = 8, N2 = 8')
    plt.plot(n1_e, n2_e, label='N1 = 12, N2 = 8')
    plt.legend()
    plt.xlabel('N1 population')
    plt.ylabel('N2 population')
    plt.title('Phase graph with 3 different curves (3rd graph)')
    plt.show()

def zadanie_2():
    zadanie_2_part_1()
    zadanie_2_part_2()

if __name__ == '__main__':
    zadanie_1()
    zadanie_2()
