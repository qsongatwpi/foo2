## Setting up Python with VS Code on macOS for OpenAI Gym and PINNs

### Prerequisites
- **Python in VS Code**: Search for *python in vs code* for setup instructions
- **Homebrew Python**: Ensure Python is installed via Homebrew (macOS package manager)

### Verify Python Installation
1. Check Python location:
    ```bash
    which python3
    ```
    Expected output: `/opt/homebrew/bin/python3`

2. Verify Python version:
    ```bash
    python3 --version
    ```

### Configure VS Code Python Interpreter
1. Run your Python script (e.g., `./src/hello1.py`) in VS Code
2. If the output shows Anaconda path like `/opt/anaconda3/bin/python`, you need to switch interpreters
3. Select the Homebrew Python interpreter in VS Code settings
4. Re-run the script to confirm it now uses the Homebrew Python installation


### Install some essential packages
1. Create virtual environment
2. run in terminal: `python3 -m pip install numpy` and similarly scipy, matplotlib
3. run `python3 -m pip list` to check installed packages

### install open ai gymnasium
1. run command: `pip install "gymnasium[all]"` 
2. run python code: 
```
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
```
We are done for open ai gym if you see an animation.



