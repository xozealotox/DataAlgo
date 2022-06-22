import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import torch.nn as nn
import numpy as np

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())

plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()


class Net(nn.Module):
    def __init__(self, in_feature, n_hidden, out_feature):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(in_feature, n_hidden)
        self.output = torch.nn.Linear(n_hidden, out_feature)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.output(x)
        return x


net = Net(1, 8, 1)
print(net)

plt.ion()
plt.show()

optimizer = torch.optim.Adam(net.parameters(), lr=0.1)
loss_func = nn.MSELoss()

for t in range(100):
    pred = net(x)
    loss = loss_func(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if t % 5 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), pred.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data, fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()