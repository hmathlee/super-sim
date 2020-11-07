import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3
import matplotlib.animation as animation
import pandas as pd


def generate_data(iterations, elements):
    """
    Generates dummy data.
    Random initial conditions for position and speed.

    Arguments:
        iterations (int): Number of iterations for which data needs to be generated
        elements (int): Number of elements (points) that will move

    Returns:
        list: list of positions of elements
    """
    dims = (3, 1)

    # Random initial positions
    gaussian_mean = np.zeros(dims)
    gaussian_std = np.ones(dims)
    init_pos = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [elements] * dims[0]))).T

    # Random speed
    init_speed = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [elements] * dims[0]))).T

    # Trajectory
    data = [init_pos]
    for i in range(iterations):
        prev_pos = data[-1]
        new_pos = prev_pos + init_speed
        data.append(new_pos)

    return data


a = np.random.rand(2000, 3)*10  # we'll need to adjust a here to represent the actual positions, determined by gravity
t = np.array([np.ones(100)*i for i in range(20)]).flatten()  # adjust 20 to actual orbital period
df = pd.DataFrame({"time": t, "x": a[:, 0], "y": a[:, 1], "z": a[:, 2]})


def update_graph(num):
    df2 = df[df['time'] == num]
    graph._offsets3d = (df2.x, df2.y, df2.z)
    title.set_text('3D Test, time={}'.format(num))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('3D Test')

data_f = df[df['time'] == 0]
graph = ax.scatter(data_f.x, data_f.y, data_f.z)

ani = animation.FuncAnimation(fig, update_graph, 19,
                              interval=40, blit=False)

plt.show()


def main(data, save=True):
    """
    Creates the 3D figure and animates it with the input data.
    Args:
        data (list): List of the data positions at each iteration.
        save (bool): Whether to save the recording of the animation. (Default to False).
    """

    # Attaching 3D axis to the figure
    f = plt.figure()
    axes = p3.Axes3D(fig)

    # Initialize scatters
    scatters = [axes.scatter(data[0][i, 0:1], data[0][i, 1:2], data[0][i, 2:]) for i in range(data[0].shape[0])]

    # Number of iterations
    iterations = len(data)

    # Setting the axes properties
    axes.set_xlim3d([-50, 50])
    axes.set_xlabel('X')

    axes.set_ylim3d([-50, 50])
    axes.set_ylabel('Y')

    axes.set_zlim3d([-50, 50])
    axes.set_zlabel('Z')

    axes.set_title('3D Animated Scatter Example')

    # Provide starting angle for the view.
    axes.view_init(25, 10)

    anmte = animation.FuncAnimation(f, scatters, iterations, fargs=(data, scatters),
                                    interval=50, blit=False, repeat=True)

    if save:
        w = animation.writers['ffmpeg']
        writer = w(fps=30, metadata=dict(artist='Me'), bitrate=1800, extra_args=['-vcodec', 'libx264'])
        anmte.save('3d-animated.mp4', writer=writer)

    plt.show()
