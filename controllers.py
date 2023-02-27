import numpy as np

class conventional_smc():

    def __init__(self, k, lam, eps):

        self.k_smc = k
        self.lam = lam
        self.eps = eps

    def sliding_surface(self, state):
        sigma = self.lam * state[0] + state[1]
        return sigma

    def calculate_u(self, state, t):
        
        sigma = self.sliding_surface(state)
        
        return -self.k_smc * np.sign(sigma)

    def continious_smc(self, state, t):
        # Continious approximation of the sliding mode
                        
        sigma = self.sliding_surface(state)

        if abs(sigma) <= self.eps:
            return -sigma/self.eps
        else:
            return -self.k_smc * np.sign(sigma)
        
class integral_smc():

    def __init__(self, k, lam, eps):

        self.k_smc = k
        self.lam = lam
        self.eps = eps

    def sliding_surface(self, state):
        sigma = (self.lam**2) * state[2] + 2*self.lam * state[0] + state[1]
        return sigma

    def calculate_u(self, state, t):
        
        sigma = self.sliding_surface(state)
        
        return -self.k_smc * np.sign(sigma)

    def continious_smc(self, state, t):
        # Continious approximation of the sliding mode

        sigma = self.sliding_surface(state)

        if abs(sigma) <= self.eps:
            return -self.k_smc*sigma/self.eps
        else:
            return -self.k_smc * np.sign(sigma)
        