import torch
import matplotlib.pyplot as plt
import math

x = list(range(- 25, 25))
y1 = [(math.sin(x1) * x1) for x1 in x]
y3 = []
for i in range(-25, 25):
    x2 = torch.tensor(float(i), requires_grad=True)
    y2 = x2 * torch.sin(x2)
    y2.backward()
    y3.append(x2.grad.item())
plt.plot(x, y1, label="sin(x)*x")
plt.plot(x, y3, label="(sin(x)*x)'")
plt.xlabel("x")  # подписываем ось х
plt.ylabel("y")  # подписываем ось у
plt.title("График функции")  # подписываем график
plt.grid(True)
plt.legend()
plt.show()
