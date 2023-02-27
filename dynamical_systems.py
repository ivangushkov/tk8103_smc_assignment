import numpy as np

class inverted_pendulum:

    def __init__(self, m, l, g, k):

        self.m = m
        self.l = l
        self.g = g
        self.k = k

        self.name = "inverted_pendulum"

    def x_dot(self, state, delta, u):
        # state = [angle, angular_acc]
        # delta = desired angle offset
        # u     = input torque

        x1 = state[0]
        x2 = state[1]

        x1_dot = x2
        x2_dot = -(self.g/self.l) * np.sin(x1 + delta) - (self.k/self.m) * x2 + (1/(self.m*self.l)) * u

        return np.array([x1_dot, x2_dot])

    def x_dot_augmented(self, state, delta, u):
        # Augments an integral state for the integral smc
        # state = [angle, angular_acc, int_angle]
        x_dot_nom = self.x_dot(state, delta, u)

        int_state = state[0]

        return np.concatenate((x_dot_nom, np.array([int_state])))
