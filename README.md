This is a rewritten project from my computational physics course for demonstration purpose. The topic of the project is chess board recognition 
using the Hodgkin-Huxley model for neurons. Shortly said, the model describes the membrane voltage of neuron with a system of differential equations:

$$
[
\begin{aligned}
C_m\frac{dV}{dt} &= I_{\mathrm{ext}}

* \bar{g}*{\mathrm{Na}}m^3h(V-E*{\mathrm{Na}})
* \bar{g}*{\mathrm{K}}n^4(V-E*{\mathrm{K}})
* g_{\mathrm{L}}(V-E_{\mathrm{L}}),[4pt]
  \frac{dm}{dt} &= \alpha_m(V)(1-m)-\beta_m(V)m,[4pt]
  \frac{dh}{dt} &= \alpha_h(V)(1-h)-\beta_h(V)h,[4pt]
  \frac{dn}{dt} &= \alpha_n(V)(1-n)-\beta_n(V)n.
  \end{aligned}
  ]

$$
