import torch
import torch.nn as nn


class Embedding(nn.Module):
    def __init__(self):
        super(Embedding, self).__init__()
        self.embedding = nn.Embedding(4, 100)

    def forward(self, x):
        return self.embedding(x)
