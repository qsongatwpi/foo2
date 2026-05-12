# Foundations of Reinforcement Learning: MDPs and Q-Learning

*Reinforcement Learning Primer*

## The Markov Decision Process (MDP) Framework

The control problem in reinforcement learning is formally defined using a Markov Decision Process, represented by the tuple $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$.

### Components

- **State Space ($\mathcal{S}$):** The set of all possible environment configurations.
- **Action Space ($\mathcal{A}$):** The set of all available moves for the agent.
- **Transition Probability ($P$):** The mapping $P(s' \mid s, a)$, defining the probability of reaching state $s'$ from state $s$ via action $a$.
- **Reward Function ($R$):** The immediate feedback $R(s, a)$ received after taking an action.
- **Discount Factor ($\gamma$):** A constant $\gamma \in [0, 1)$ that balances immediate and future rewards.

### The Objective Function

The agent's goal is to maximize the expected discounted return $G_t$:

$$
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}
$$

## The Q-Learning Algorithm

Q-learning is a model-free, off-policy algorithm used to find the optimal action-value function $Q^*(s, a)$.

### The Bellman Optimality Equation

The optimal Q-value, denoted by $Q^*(s, a)$, is the maximum expected return achievable from a given state-action pair $(s, a)$, and it satisfies the Bellman optimality equation:

$$
Q^*(s, a) = \mathbb{E} \left[ r + \gamma \max_{a'} Q^*(s', a') \mid s, a \right],
\quad \forall (s, a) \in \mathcal{S} \times \mathcal{A}
$$

where $s'$ is the next state resulting from taking action $a$ in state $s$.

We denote:

$$
\left[ r + \gamma \max_{a'} Q^*(s', a') \mid s, a \right] = F(Q^*, s, a, \omega),
\quad \forall (s, a) \in \mathcal{S} \times \mathcal{A}
$$

where $\omega$ represents the randomness in the environment. Then, the optimal Q-value can be expressed as the fixed point of the stochastic Bellman operator $F[Q]$:

$$
Q^*(s, a) = \mathbb{E} \left[ F(Q^*, s, a, \omega) \right],
\quad \forall (s, a) \in \mathcal{S} \times \mathcal{A}
$$

### Temporal Difference (TD) Update Rule

It is well known in the literature of stochastic approximation that the fixed point of

$$
x = \mathbb{E}[f(x, \omega)]
$$

can be found by the following iterative procedure: for an appropriate condition of $f$ and a sequence of i.i.d. samples $\{\omega_n\}$, the sequence $\{x_n\}$ is defined by

$$
x_{n+1} = (1 - \alpha)x_n + \alpha f(x_n, \omega_n)
$$

where $\alpha$ is the learning rate. Applying this result to the Bellman optimality equation, we derive the Q-learning update rule:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

where $\alpha$ is the **learning rate**.

## Control and Policy

Once the Q-values converge to $Q^*$, the optimal policy $\pi^*$ is derived by selecting the action with the highest value in each state:

$$
\pi^*(s) = \arg\max_{a \in \mathcal{A}} Q^*(s, a)
$$

The above Q-learning algorithm is pure exploitation (zero-greedy). In practice, we often use an $\epsilon$-greedy policy to balance exploration and exploitation during learning.

The $\epsilon$-greedy policy selects a random action with probability $\epsilon$ and the action with the highest Q-value with probability $1 - \epsilon$.
