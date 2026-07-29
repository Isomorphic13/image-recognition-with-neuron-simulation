This is a rewritten project from my Computational Physics course for demonstration purposes. The topic of the project is chessboard recognition using the Hodgkin-Huxley model of neurons.

In short, the Hodgkin-Huxley model describes the membrane voltage of a neuron using a system of differential equations. The voltage depends on the membrane capacitance $C_m$, external current $I_{\mathrm{ext}}$, sodium current $I_{\mathrm{Na}}$, potassium current $I_{\mathrm{K}}$, and leak current $I_{\mathrm{L}}$:

I_{\mathrm{ext}}

I_{\mathrm{Na}}
I_{\mathrm{K}}
I_{\mathrm{L}}
$$

with

$$
I_{\mathrm{Na}} = g_{\mathrm{Na}}m^3h(V-E_{\mathrm{Na}})
$$

$$
I_{\mathrm{K}} = g_{\mathrm{K}}n^4(V-E_{\mathrm{K}})
$$

$$
I_{\mathrm{L}} = g_{\mathrm{L}}(V-E_{\mathrm{L}})
$$

Therefore,

I_{\mathrm{ext}}

g_{\mathrm{Na}}m^3h(V-E_{\mathrm{Na}})
g_{\mathrm{K}}n^4(V-E_{\mathrm{K}})
g_{\mathrm{L}}(V-E_{\mathrm{L}})
=
f_V(V,n,m,h,t)
$$

The remaining state variables are described by:

\alpha_n(V)(1-n)-\beta_n(V)n

f_n(V,n,m,h,t)
$$

\alpha_m(V)(1-m)-\beta_m(V)m

f_m(V,n,m,h,t)
$$

\alpha_h(V)(1-h)-\beta_h(V)h

f_h(V,n,m,h,t)
$$

The system can be written in short form using the state vector $\vec{s}$:

$$
\vec{s}(t) := (V,n,m,h)^T
$$

F(V,n,m,h,t)
:=
(f_V,f_n,f_m,f_h)^T
$$

There is no analytical solution for this system, so we use the fourth-order Runge-Kutta method for numerical calculations.

For example, the following plots show the membrane voltage over time for different constant external currents:







As we can see, different external currents produce different voltage dynamics. We will use this property later by applying different external currents to white and black pixels.

Neural Network

The second important property of current in physiological neurons is how the voltage of neuron $i$ in a neuron chain contributes to the current of neuron $j$:

$$
I_j = \sum_{i<j} w_{ij}V_i
$$

where $i$ denotes a preceding neuron in the chain and $w_{ij}$ is the coupling parameter, which later serves as a weight.

In this project, we use the following simple topology:




Here, $R_i$ represents a receptor neuron that receives an input current depending on the corresponding pixel color, while $E$ is the deciding neuron whose voltage is used to make the final classification.

The corresponding weights are shown below. The deciding neuron $E$ is labeled as $R_5$ in this diagram for readability:


In the next cell, the voltage trajectories for all possible $2 \times 2$ pixel grids are shown using manually selected weights. We can see that some signals cross the threshold $V = 0$. Our goal is to use a machine learning algorithm to find weights such that the voltage crosses this threshold for chessboard inputs but not for the other inputs.



