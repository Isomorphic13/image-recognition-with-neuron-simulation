import numpy as np
import matplotlib.pyplot as plt
from ode_solver_runge_kutta import runge_kutta_method
import set_of_boards
from neural_network import NeuralNetwork

tuple_of_constants = (1, 36, 120, 0.3, -77, 50, -54.387)

def visualise_state_of_single_neuron(initial_state : np.ndarray, time_array : np.ndarray, dt : float, current: float):

    s = runge_kutta_method(initial_state, time_array, dt, current, tuple_of_constants)
    v = s[0:, 0]
    n = s[0:, 1]
    m = s[0:, 2]
    h = s[0:, 3]

    plt.figure(figsize=(10, 5))
    plt.plot(time_array, v, linewidth=2)
    plt.xlabel("Time $t$, ms")
    plt.ylabel("Voltage $V$, mV")
    plt.title(f"Membrane voltage $V$ over time for current I = {current} nA.")
    plt.grid(True)

    plt.figure(figsize=(10, 5))
    plt.plot(time_array, n, linewidth=2)
    plt.xlabel("Time $t$, ms")
    plt.ylabel("$n$")
    plt.title(f"Gating variable $n$ over time for current I = {current} nA.")
    plt.grid(True)

    plt.figure(figsize=(10, 5))
    plt.plot(time_array, m, linewidth=2)
    plt.xlabel("Time $t$, ms")
    plt.ylabel("$m$")
    plt.title(f"Gating variable $m$ over time for current I = {current} nA.")
    plt.grid(True)

    plt.figure(figsize=(10, 5))
    plt.plot(time_array, h, linewidth=2)
    plt.xlabel("Time $t$, ms")
    plt.ylabel("$h$")
    plt.title(f"Gating variable $h$ over time for current I = {current} nA.")
    plt.grid(True)

    plt.show()


def visualize_voltage_for_different_currents(initial_state : np.ndarray, time_array : np.ndarray, dt : float):

    plt.figure(figsize=(10, 5))

    current_values = list(range(-3, 5))


    for i in current_values:
        temp = runge_kutta_method(initial_state, time_array, dt, i, tuple_of_constants)[:, 0]
        plt.plot(time_array, temp, linewidth=2, label=f"$I_0 = {i}$nA")

    plt.xlabel("Time $t$,, ms")
    plt.ylabel("Voltage $V$, mV")
    plt.title("Membrane voltage $V(I,t)$ over time different currents.")
    plt.grid(True)

    plt.legend(loc="upper right", fontsize="small")

    # another plot
    plt.figure(figsize=(10, 5))

    current_values = list(range(6, 11))


    for i in current_values:
        temp = runge_kutta_method(initial_state, time_array, dt, i, tuple_of_constants)[:, 0]
        plt.plot(time_array, temp, linewidth=2, label=f"$I_0 = {i}$nA")

    plt.xlabel("Time $t$,, ms")
    plt.ylabel("Voltage $V$, mV")
    plt.title("Membrane voltage $V(I,t)$ over time different currents.")
    plt.grid(True)

    plt.legend(loc="upper right", fontsize="small")

    plt.show()


def visualize_test(optimal_weights, time_interval : float):
    weights = optimal_weights
    network = NeuralNetwork(weights, 2, 2)
    network.set_time_array(np.arange(0, time_interval, 0.01))
    boards = set_of_boards.get_set_of_boards()

    tpoints = network.time_array

    fig, ax = plt.subplots(len(boards), 1, figsize=(10, 24), sharex=True)
    ax = ax.flatten()
    fig.suptitle("Voltage dynamics in the deciding neuron over time and prediction of the model depending on the signal.")
    fig.subplots_adjust(top=0.9, hspace=0.3)

    i = 0

    cb1 = set_of_boards.get_set_of_chess_boards()[0]
    cb2 = set_of_boards.get_set_of_chess_boards()[1]

    for b in boards:
        network.input_board(b)
        voltage = network.get_deciding_neuron_voltage()
        voltage_max = round(voltage.max(), 2)
        voltage_mean = round(voltage.mean(), 2)
        board_label = (
                f"{'Chess ' if np.array_equal(b, cb1) or np.array_equal(b, cb2) else ''}Board:\n{'▣' if b[0, 0] == 1 else '▢'} {'▣' if b[0, 1] == 1 else '▢'} \n{'▣' if b[1, 0] == 1 else '▢'} {'▣' if b[1, 1] == 1 else '▢'} \n"
                + "prediction:" + f"{'yes' if voltage_max >= 0 else 'no'}")
        ax[i].plot(tpoints, voltage, label=board_label)
        ax[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
        i += 1

    ax[-1].set_xlabel("Time t, (ms)")

    plt.show()


def visualize_error_history(error_history):
    tpoints = np.arange(0, len(error_history), 1)
    plt.figure(figsize=(10, 5))
    plt.plot(tpoints, error_history, linewidth=2)
    plt.xlabel("Number of iterations")
    plt.ylabel("Errors pro iteration")
    plt.title("Number of errors over time")
    plt.grid(True)


