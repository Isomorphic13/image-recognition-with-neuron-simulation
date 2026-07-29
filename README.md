This is a rewritten project from my computational physics course for demonstration purpose. The topic of the project is chess board recognition 
using the Hodgkin-Huxley model for neurons. Shortly said, the model describes the membrane voltage of neuron with a system of differential equations. The voltage depends on membrane capacity $C_m$, outer current $I_{ext}$, currents $I_{Na}$, $I_K$ from Na and K ions inside and outside the membrane, leak current $I_L$:

$$
C_m \frac{dV}{dt} = I_{\mathrm{ext}} - I_{Na} - I_{Ka} - I_{L} = g_{\mathrm{Na}}m^3h(V-E_{\mathrm{Na}}) - g_{\mathrm{K}}n^4(V-E_{\mathrm{K}}) - g_{\mathrm{L}}(V-E_{\mathrm{L}}) = f_{V}(V,n,m,h,t)
$$
$$
\frac{dn}{dt} = \alpha_n(V)(1-n) - \beta_n(V)n = f_{n}(V,n,m,h,t)
$$
$$
\frac{dm}{dt} = \alpha_m(V)(1-m) - \beta_m(V)m = f_{m}(V,n,m,h,t)
$$
$$
\frac{dh}{dt} = \alpha_h(V)(1-h) - \beta_h(V)h = f_{h}(V,n,m,h,t)
$$
or in short form with state vector $\vec{s}$:
$$
\vec{s}(t) := (V, n, m , h, t)^T
$$
$$
\frac{d\vec{s}}{dt} = F(V,n,m,h,t) := (f_v, f_n, f_m, f_h, t)^T
$$

For example, this is membrane voltage over time for different constant current:
![Voltage over time](images/voltage_dynamics_diff_currents1.png)

![Voltage over time](images/voltage_dynamics_diff_currents2.png)

