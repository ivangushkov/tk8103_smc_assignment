import numpy as np

class conventional_smc():

    def __init__(self, k, lam, eps):

        self.k_smc = k
        self.lam = lam
        self.eps = eps

    def sliding_surface(self, state):
        sigma = 0 #TODO implement the sliding surface expression
        return sigma

    def calculate_u(self, state, t):
        
        sigma = self.sliding_surface(state)
        
        return 0 #TODO

    def continious_smc(self, state, t):
        # Continious approximation of the sliding mode

        sigma = self.sliding_surface(state)

        #TODO implement the boundary layer input

        return 0
        
class integral_smc():

    def __init__(self, k, lam, eps):

        self.k_smc = k
        self.lam = lam
        self.eps = eps

    def sliding_surface(self, state):
        sigma = 0 #TODO implement the sliding surface expression
        return sigma

    def calculate_u(self, state, t):
        
        sigma = self.sliding_surface(state)
        
        return 0 #TODO

    def continious_smc(self, state, t):
        # Continious approximation of the sliding mode

        sigma = self.sliding_surface(state)

        #TODO implement the boundary layer input
        return 0
        