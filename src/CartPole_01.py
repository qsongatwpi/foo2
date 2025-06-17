import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")  # Important: set render_mode
observation, info = env.reset(seed=42)

for _ in range(1000):
    env.render()  # This displays the environment
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
# Note: The `render()` method is used to visualize the environment.