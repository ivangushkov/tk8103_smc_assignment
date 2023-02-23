import numpy as np

class conventional_smc():

    def __init__(self, k, lam):

        self.k_smc = k
        self.lam = lam

    def sliding_surface(self, state):
        sigma = self.lam * state[0] + state[1]
        return sigma

    def calculate_u(self, state, t):
        
        sigma = self.sliding_surface(state)
        
        return -self.k_smc * np.sign(sigma)