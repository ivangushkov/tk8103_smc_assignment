import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import time

import dynamical_systems
import controllers

## Code for sliding mode assignment in TK8103 - Advanced Nonlinear Analysis

# Pendulum Parameters

m = 0.1
l = 1
k = 0.02
g = 9.81

delta = np.pi/2
init_state = [0 - delta, 0.0]

# smc parameters
k_smc = 4
lam   = 1

# Simulation parameters

animate = True

T = 30
dt = 0.0001
N = int(T/dt)
t = np.linspace(0, T, N+1)


controller = controllers.conventional_smc(k_smc, lam)
dynamical_system = dynamical_systems.inverted_pendulum(m = m, l = l, g = g, k = k)

# Allocate arrays for results
sol = np.zeros((int(T/dt)+1, 2))
sol[0,:] = init_state

u_vec = np.zeros((N, 1))
s_vec = np.zeros((N, 1))

for i in range(N):

    u = controller.calculate_u(sol[i], i*dt)
    s = controller.sliding_surface(sol[i])
    x_dot = dynamical_system.x_dot(sol[i,:], delta, u)
    
    # Store input, sliding variable and steped state
    u_vec[i] = u
    s_vec[i] = s
    sol[i+1, :] = sol[i, :] + x_dot * dt

theta = sol[:,0] + delta
theta_dot = sol[:,1]


if animate == True:
    # Terible code to animate the pendulum

    def get_coords(theta_n):
        """Return the (x, y) coordinates of the bob at angle th."""
        return l * np.sin(theta_n), -l * np.cos(theta_n)


    fig = plt.figure()
    ax = fig.add_subplot(aspect='equal')
    # The pendulum rod, in its initial position.
    x0, y0 = get_coords(theta[0])
    line, = ax.plot([0, x0], [0, y0], lw=3, c='k')
    # The pendulum bob: set zorder so that it is drawn over the pendulum rod.
    bob_radius = 0.08
    circle = ax.add_patch(plt.Circle(get_coords(theta[0]), bob_radius,
                      fc='r', zorder=3))
    # Set the plot limits so that the pendulum has room to swing!
    ax.set_xlim(-l*1.2, l*1.2)
    ax.set_ylim(-l*1.2, l*1.2)

    def animate(i):
        """Update the animation at frame i."""
        x, y = get_coords(theta[i*100])# *100 due to downsampling of frames
        line.set_data([0, x], [0, y])
        circle.set_center((x, y))

    # downsample the frames by a factor of 100
    nframes = int(len(theta)/100)
    interval = dt
    
    ani = animation.FuncAnimation(fig, animate, frames=nframes, repeat=True,
                              interval=interval)
    plt.show()


fig1 = plt.figure(1)
plt.plot(t, theta, 'b', label='theta(t)')
plt.plot(t, theta_dot, 'g', label='omega(t)')
plt.axhline(y = delta, color = 'r', linestyle = '-', label='reference angle')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()

fig2 = plt.figure(2)
plt.plot(theta, theta_dot)
plt.xlabel('angle')
plt.ylabel('angular velocity')
plt.title('Trajectory of the system in state-space')
plt.grid()

fig3 = plt.figure(3)
plt.plot(t[1::], u_vec)
plt.xlabel('time')
plt.ylabel('input torque')
plt.title('Input')
plt.grid()

sliding_var_plot_time = 3
N_sliding_plot_time = int(sliding_var_plot_time/dt)
fig4 = plt.figure(4)
plt.plot(t[1:N_sliding_plot_time+1], s_vec[0:N_sliding_plot_time])
plt.xlabel('time [s]')
plt.ylabel('sliding variable')
plt.title('Sliding variable time evolution')
plt.grid()

plt.show()
