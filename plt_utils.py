# chatgpt helped me write this
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interactive
from IPython.display import display
import numpy as np


def visq(q):
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    # Find the minimum and maximum Q-values across all actions and states
    min_q = min(q[state].get(action, 0)
                for action in range(4) for state in range(64))
    max_q = max(q[state].get(action, 0)
                for action in range(4) for state in range(64))
    for action in range(4):
        # Convert 'q' for the specific action to a 2D numpy array
        q_array = np.zeros((8, 8))
        for state in range(64):
            row, col = divmod(state, 8)
            q_value = q[state].get(action, 0)
            q_array[row][col] = q_value
        # Create a heatmap for this action with a common color scale
        ax = axes[action // 2, action % 2]
        im = ax.imshow(q_array, cmap='hot',
                       interpolation='nearest', vmin=min_q, vmax=max_q)
        ax.set_title(f'Action {action}')
        plt.colorbar(im, ax=ax)

    plt.tight_layout()
    plt.show()


def intq(qq):
    def plot_qq(i):
        visq(qq[i])

    i_slider = widgets.IntSlider(
        value=0, min=0, max=len(qq) - 1, description='iterations')
    interactive_plot = interactive(plot_qq, i=i_slider)
    display(interactive_plot)


def visualize_value_and_policy(v, policy):
    # Convert 'v' to a 2D numpy array
    v_array = np.zeros((8, 8))
    for state in v:
        row, col = divmod(state, 8)
        v_array[row][col] = v[state]

    # Create a grid of coordinates for arrows
    x, y = np.meshgrid(np.arange(8), np.arange(8))

    # Create an array of action vectors based on the policy
    dx = np.zeros_like(v_array, dtype=int)
    dy = np.zeros_like(v_array, dtype=int)

    for state in range(64):
        row, col = divmod(state, 8)
        action = policy[state]
        if action == 0:  # Left
            dx[row, col] = -1
        elif action == 1:  # Down
            dy[row, col] = 1
        elif action == 2:  # Right
            dx[row, col] = 1
        elif action == 3:  # Up
            dy[row, col] = -1

    # Create a combined plot with value function and policy arrows
    fig, ax = plt.subplots()
    cax = ax.matshow(v_array, cmap='hot')
    plt.colorbar(cax)
    ax.quiver(x, y, dx, dy, angles='xy',
              scale_units='xy', scale=3, color='blue')
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 8)
    plt.gca().invert_yaxis()
    # Show the plot
    plt.show()


def intvp(vv, pp):

    def vvap(i, row, col):
        pos = 8*row+col
        print(f"val({pos}) = {vv[i][pos]}")
        print(f"for fininte horizon this is f{len(vv)-i},v{len(vv)-i}")
        visualize_value_and_policy(vv[i], pp[i])
    i_slider = widgets.IntSlider(value=0, min=0, max=min(
        len(vv), len(pp)) - 1, description='iterations')
    row_slider = widgets.IntSlider(
        value=0, min=0, max=7, description='rowpos of val')
    col_slider = widgets.IntSlider(
        value=0, min=0, max=7, description='colpos of val')
    interactive_plot = interactive(
        vvap, i=i_slider, row=row_slider, col=col_slider)
    display(interactive_plot)
