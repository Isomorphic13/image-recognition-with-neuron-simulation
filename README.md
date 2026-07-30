This is a rewritten project from my computational physics course for demonstration purpose. The topic of the project is chess board recognition using the Hodgkin-Huxley model for neuronal cells. The model describes membrane voltage dynamics depending on outer current in a single neuron with a system of differential equations. A description of this model and its equations you can find in Wikipedia: https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model . More detailed explanation of mathematical methodology with visualization you can find in Jupyter notebook file named 'demonstration.ipynb'. In the following you can read the summary of the methodology.

Using the the dependence (1) between voltages in neuron cells and outer currents in other other that these voltages cause ,
we can make a model that recognize patterns such as chess arranged pixel grids. 

$$ I_j = \sum_{i < j} w_{ij} V_i \ \  (1), \text{where } i \text{ is a previous neuron in neural chain}$$ 

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

We compute the state of whole network with state matrix:

$$
S(t) = (\vec{s_1}^T(t), ... , \vec{s_n}^T(t)
$$

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








