This is a rewritten project from my computational physics course for demonstration purpose. The topic of the project is chess board recognition using the Hodgkin-Huxley model for neuronal cells. The model describes membrane voltage dynamics depending on outer current in a single neuron with a system of differential equations. A description of this model and its equations you can find in Wikipedia: https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model . More detailed explanation of mathematical methodology with visualization you can find in Jupyter notebook file named 'demonstration.ipynb'. In the following you can read the summary of the methodology.

Using the the dependence (1) between voltages in neuron cells and outer currents in other other that these voltages cause,
we can make a model that recognize patterns such as chess arranged pixel grids. 

$$ I_j = \sum_{i < j} w_{ij} V_i , \text{where } i \text{ is a previous neuron in neural chain} \ \ \ (1)$$ 

First, let define state of a single neuron with state vector, which is calculated numerically with Runge-Kutta method:

$$
\vec{s}(t) := (V(I,n,m,h,t), n(t), m(t), h(t), t)^T \ \ \ (2), 
$$
$$
\frac{d \vec{s}}{dt} := F(V,n,m,h,t)^T \ \ \ (3)
$$

Then the we can describe a neural network with $n$ neurons with the following equations:

$$
\vec{i_{total}}(t) = \vec{i_{out}}(t) + \vec{i_{p}} \ \ \(4),
$$

$$
\vec{i_{out}}(t) = W \vec{v}(\vec{i_{tot}}(t),t) \ \ \ (5),
$$

$$
W = (\vec{w_1}, \vec{w_2}, ..., \vec{w_n}) \ \ \ (6),
$$

Where index of each element corresponds to a neural cell in the network. $\vec{i_{total}}$ is total currents applied to a cell, $\vec{i_{out}}$ outer currents caused from other cells, $\vec{i_{p}}$ is currents coming from input in each pixel, \vec{v} is membrane voltages, $\vec{w_{n}}$ connections from one neuron to the rest including itself (which is of course equal to to zero). Here is an example for a neural network and it topology: 

![topology](images/topology1.png) 

![topology](images/topology2.png) 

The module 'neural_network.py' computes the state dynamics over a time interval and gives the voltage function over time for the neuron E. 'neural_network' calls module 'ode_solver_runge_kutta.py' to calculate the state matrix over time, which itself calls module 'equations' to find the state matrix in time point $t_0$.

$$
S(t) = (\vec{s_1}^T(t), ... , \vec{s_n}^T(t) \ \ \ (7)
$$

Our goal is to find weights, such that voltage in the cell E passes the threshold $V_0 = 0$ for chess arranged pixel grids and remains under zero for other grids. To find optimal weights, the module 'learning_model' implements random walk algorithm and calls the module 'neural_network' in each iteration. Below is the result of the method for the given topology example:

![topology](images/test.png) 

 









