import torch
import torch.nn as nn
from torch import Module
import torch.nn.functional as F


class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.first_layer = nn.Linear(1000, 50)
        self.second_layer = nn.Linear(50, 1)

    def forward(self, x):
        """
        :param x: batch of information
        :return:
        """
        x = torch.flatten(x, start_dim=1, end_dim=2)
        x = F.relu(self.first_layer(x))
        x = self.second_layer(x)
        return x
