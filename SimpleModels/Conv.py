import torch
import torch.nn as nn
import torch.nn.functional as F


class Conv(nn.Module):
    def __init__(self):
        super(Conv, self).__init__()
        self.conv1d = nn.Conv1d(100, 50, 2)

    def forward(self, x):
        return self.conv1d(x)
