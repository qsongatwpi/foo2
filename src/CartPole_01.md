# CartPole Q-Learning Implementation

## What is CartPole?

CartPole can be modeled as a Markov decision process (MDP)

$$
(\mathcal{S}, \mathcal{A}, P, R, \gamma),
$$

where the state is typically

$$
s_t = \bigl(x_t, \dot{x}_t, \theta_t, \dot{\theta}_t\bigr),
$$

with $x_t$ the cart position, $\dot{x}_t$ the cart velocity, $\theta_t$ the pole angle, and $\dot{\theta}_t$ the pole angular velocity.

The action space is discrete:

$$
\mathcal{A} = \{\text{left},\,\text{right}\},
$$

which can also be written as $a_t \in \{-1, +1\}$ when using a signed force convention. At each time step, the agent applies a force $F_t$ to the cart, and the environment evolves according to the following nonlinear dynamics of the cart-pole system:

$$
\ddot{x}_t = \frac{F_t + m_p \sin(\theta_t) \bigl(l \dot{\theta}_t^2 + g \cos(\theta_t)\bigr)}{m_c + m_p \sin^2(\theta_t)}
$$

$$
\ddot{\theta}_t = \frac{-F_t \cos(\theta_t) - m_p l \dot{\theta}_t^2 \sin(\theta_t) \cos(\theta_t) - (m_c + m_p) g \sin(\theta_t)}{l (m_c + m_p \sin^2(\theta_t))}
$$

where $m_c$ is the mass of the cart, $m_p$ is the mass of the pole, $l$ is the length of the pole, and $g$ is the acceleration due to gravity.

The control objective is to keep the pole balanced near the upright position $\theta = 0$ while keeping the cart near the track center. A standard reward choice is

$$
r_t = 1
$$

for every step before termination. An episode ends when the cart leaves the allowed position range or when the pole angle exceeds a threshold.

For Q-learning, the action-value function $Q(s,a)$ is updated by

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha
\Bigl(r_t + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t)\Bigr),
$$

where $\alpha$ is the learning rate and $\gamma$ is the discount factor.
