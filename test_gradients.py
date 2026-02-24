import torch

x_relu = torch.tensor([0.0], requires_grad=True)
y_relu = torch.relu(x_relu)
y_relu.backward()
print(f"Gradient of ReLU at 0: {x_relu.grad}")

x_abs = torch.tensor([0.0], requires_grad=True)
y_abs = torch.abs(x_abs)
y_abs.backward()
print(f"Gradient of abs at 0: {x_abs.grad}")
