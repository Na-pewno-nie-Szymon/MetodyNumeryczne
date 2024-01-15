import numpy as np

class HunterPreyModel:
    def __init__(self, 
                 epsilon1: float, epsilon2: float, 
                 gamma1: float, gamma2: float, 
                 h1: float, h2: float, 
                 t0 = .0, tf = 30., 
                 interval = 10000, 
                 n1_init = 3., 
                 n2_init = 4.) -> None:
        
        self.N1_init = n1_init
        self.N2_init = n2_init
        self.epsilon_1 = epsilon1
        self.epsilon_2 = epsilon2
        self.gamma_1 = gamma1
        self.gamma_2 = gamma2
        self.h1 = h1
        self.h2 = h2
        self.timeline = np.linspace(t0, tf, interval)
        self.interval = interval
        self.N1 = self.model_eulera()[0]
        self.N2 = self.model_eulera()[1]
        

    def model_eulera(self) -> list:
        N1 = np.zeros(self.interval)
        N2 = np.zeros(self.interval)

        N1[0] = self.N1_init
        N2[0] = self.N2_init

        h = 1/1000

        for i in range(1, self.interval):
            N1[i] = N1[i-1] + h * ((self.epsilon_1 - self.gamma_1 * (self.h1 * N1[i-1] + self.h2 * N2[i-1])) * N1[i-1])
            N2[i] = N2[i-1] + h * ((self.epsilon_2 - self.gamma_2 * (self.h1 * N1[i-1] + self.h2 * N2[i-1])) * N2[i-1])
              
        return [N1, N2]
