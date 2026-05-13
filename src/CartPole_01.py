import gymnasium as gym
import numpy as np


def build_bins(num_bins: int = 12):
    """Create discretization bins for CartPole observations."""
    return [
        np.linspace(-4.8, 4.8, num_bins - 1),
        np.linspace(-3.0, 3.0, num_bins - 1),
        np.linspace(-0.418, 0.418, num_bins - 1),
        np.linspace(-3.5, 3.5, num_bins - 1),
    ]


def discretize_state(observation: np.ndarray, bins):
    return tuple(np.digitize(observation[i], bins[i]) for i in range(len(observation)))


def choose_action(state, q_table: np.ndarray, epsilon: float, rng: np.random.Generator):
    if rng.random() < epsilon:
        return int(rng.integers(q_table.shape[-1]))
    return int(np.argmax(q_table[state]))


def train_q_learning(
    episodes: int = 5000,
    max_steps: int = 500,
    learning_rate: float = 0.1,
    discount: float = 0.99,
    epsilon_start: float = 1.0,
    epsilon_min: float = 0.02,
    epsilon_decay: float = 0.995,
    num_bins: int = 12,
    seed: int = 42,
):
    env = gym.make("CartPole-v1")
    rng = np.random.default_rng(seed)
    bins = build_bins(num_bins)

    obs_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    q_table = np.zeros((num_bins,) * obs_dim + (action_dim,), dtype=np.float32)

    epsilon = epsilon_start
    episode_rewards = []

    for episode in range(episodes):
        observation, _ = env.reset(seed=seed + episode)
        state = discretize_state(observation, bins)
        total_reward = 0.0

        for _ in range(max_steps):
            action = choose_action(state, q_table, epsilon, rng)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            next_state = discretize_state(next_observation, bins)

            best_next_q = float(np.max(q_table[next_state]))
            td_target = reward if done else reward + discount * best_next_q
            td_error = td_target - q_table[state + (action,)]
            q_table[state + (action,)] += learning_rate * td_error

            state = next_state
            total_reward += reward

            if done:
                break

        episode_rewards.append(total_reward)
        epsilon = max(epsilon_min, epsilon * epsilon_decay)

        if (episode + 1) % 250 == 0:
            recent_avg = np.mean(episode_rewards[-100:])
            print(
                f"Episode {episode + 1:4d} | "
                f"epsilon={epsilon:.4f} | "
                f"avg_reward(last100)={recent_avg:.2f}"
            )

    env.close()
    return q_table, bins, episode_rewards


def evaluate_policy(
    q_table: np.ndarray,
    bins,
    episodes: int = 10,
    max_steps: int = 500,
    render: bool = False,
    seed: int = 2026,
):
    env = gym.make("CartPole-v1", render_mode="human" if render else None)
    rewards = []

    for episode in range(episodes):
        observation, _ = env.reset(seed=seed + episode)
        state = discretize_state(observation, bins)
        total_reward = 0.0

        for _ in range(max_steps):
            action = int(np.argmax(q_table[state]))
            observation, reward, terminated, truncated, _ = env.step(action)
            state = discretize_state(observation, bins)
            total_reward += reward

            if terminated or truncated:
                break

        rewards.append(total_reward)

    env.close()
    return float(np.mean(rewards)), rewards




if __name__ == "__main__":
    q_table, bins, rewards = train_q_learning()
    avg_reward, eval_rewards = evaluate_policy(q_table, bins, episodes=20, render=True)

    print("\nTraining complete")
    print(f"Final average reward (last 100 train episodes): {np.mean(rewards[-100:]):.2f}")
    print(f"Evaluation average reward (20 episodes): {avg_reward:.2f}")
    print(f"Evaluation rewards: {eval_rewards}")
    