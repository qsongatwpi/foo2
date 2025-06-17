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
