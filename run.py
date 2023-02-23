import numpy as np
from scipy.integrate import odeint
import dynamical_systems
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## Code for sliding mode assignment in TK8103 - Advanced Nonlinear Analysis

def call_dynamics(state, t, dynamical_system, controller, parameters):

    if dynamical_system.name == "nomoto_heading":
        pass
    elif dynamical_system.name == "inverted_pendulum":
        u = 0
        x_dot = dynamical_system.x_dot(state, parameters, u)
    else:
        pass
    
    return x_dot

# Pendulum Parameters

m = 0.1
l = 1
k = 0.02
g = 9.81

delta = np.pi/2
init_state = [np.pi/3 - delta, 0.0]

# Simulation parameters

animate = True

T = 100
dt = 0.1
t = np.linspace(0, T, int(T/dt))

controller = None
dynamical_system = dynamical_systems.inverted_pendulum(m = m, l = l, g = g, k = k)

sol = odeint(call_dynamics, init_state, t, args=(dynamical_system, controller, delta))

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
        x, y = get_coords(theta[i])
        line.set_data([0, x], [0, y])
        circle.set_center((x, y))
    nframes = int(T/dt)
    interval = T
    ani = animation.FuncAnimation(fig, animate, frames=nframes, repeat=True,
                              interval=interval)
    plt.show()


plt.plot(t, theta, 'b', label='theta(t)')
plt.plot(t, theta_dot, 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
