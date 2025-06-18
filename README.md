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
2. If the output shows Anaconda path like `/opt/anaconda3/bin/python`, switch interpreters
3. Select the Homebrew Python interpreter in VS Code settings
4. Re-run the script to confirm it uses the Homebrew Python installation

### Install Essential Packages
1. Create a virtual environment
2. Install packages in terminal:
    ```bash
    python3 -m pip install numpy scipy matplotlib
    ```
3. Verify installation:
    ```bash
    python3 -m pip list
    ```

### Install OpenAI Gymnasium
1. Install the package:
    ```bash
    pip install "gymnasium[all]"
    ```

2. Test with sample code:
    ```python
    import gymnasium as gym

    env = gym.make("CartPole-v1", render_mode="human")
    observation, info = env.reset(seed=42)

    for _ in range(1000):
         env.render()
         action = env.action_space.sample()
         observation, reward, terminated, truncated, info = env.step(action)

         if terminated or truncated:
              observation, info = env.reset()

    env.close()
    ```

**Success**: If you see an animated CartPole environment, OpenAI Gym is working correctly.
