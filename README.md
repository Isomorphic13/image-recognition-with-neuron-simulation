This is a rewritten project from my computational physics course for demonstration purpose. The topic of the project is chess board recognition using the Hodgkin-Huxley model for neurons. The model describes the membrane voltage dynamics in a single neuron with a system of differential equations. A description of this model and its equations you can find in Wikipedia: https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model . More detailed explanation of mathematical methodology with visualization you can find in Jupyter notebook file named 'demonstration.ipynb'. In the following you can read the summary of the methodology.

Using the the dependence (1) between voltages in neuron cells and outer currents in other cells,
we can make a model that recognize patterns such as chess arranged pixel grids 

$$ I_j = \sum_{i < j} w_{ij} V_i \ \ \ \ \ (1)$$ 


![Voltage over time](images/voltage_dynamics_diff_currents1.png) ![Voltage over time](images/voltage_dynamics_diff_currents2.png)

As we see, different currents cause different voltage dynamics. We will use this property later, when we will set different apllied currents for white and black pixels. The second important property of current in physiological neurons is how voltages $V_i$ in neuron chains cause current in neuron $j$: 

$$ I_j = \sum_{i < j} w_{ij} V_i $$ 

where i is a previous neuron in chain and $w_{ij}$ is activation parameter later weight. In this project we use the following simple topology: If we write state of a single neuron with state vector:

$$
\vec{s}(t) := (V(I,n,m,h,t), n(t), m(t), h(t), t)^T, \\
\frac{d \vec{s}}{t} := F(V,n,m,h,t)
$$

![topology](images/topology1.png) 

where $R_i$ is receptor neuron, which receive current signal depending on the pixel colour, $E$ is deciding neuron, which voltage we use for the decision. Here are the corresponding weights ($E$ was changed to $R_5$ for readability): 

![topology](images/topology2.png) 

We can describe this problem quantitatively in compact form. For the topology given above let $i \leq 5$ be index for a neuron.
Define 

$$
\vec{v} = (V_1(t), ..., V_5(t))^T \text{vector of voltages}
$$

$$
\vec{i_{0}} = (I_{1,0}, ..., I_{5,0})^T \text{currents from input}
$$

$$
\vec{w_i} = (w_{i,1}, w_{i,2}, ..., w_{i,5})^T \text{connection from i-th neuron to others}
$$
Then we can write:

$$
\vec{i_{out}}(t) = W \vec{v}(\vec{i_{tot}}, t)
$$

where $\vec{v_{out}}$ currents in neurons from other neuron, $\vec{i_{tot}} = \vec{i_{out}} + \vec{v_{0}}$ total current applied to the neurons








