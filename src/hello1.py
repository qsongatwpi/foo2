import numpy as np

msg = "hello world"
print(msg)

try:
    print("NumPy is installed, version:", np.__version__)
except ImportError:
    print("NumPy is not installed")