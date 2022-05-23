import torch
import torch.nn as nn
import torch.nn.functional as F

EPS = 0.00001


class EntityEmbeddingLayer(nn.Module):
    """离散变量连续化处理"""

    def __init__(self, num_level, embedding_dim, centroid):
        super(EntityEmbeddingLayer, self).__init__()
        self.embedding = nn.Embedding(num_level, embedding_dim)
        self.centroid = torch.tensor(centroid).detach_().unsqueeze(1)

    def forward(self, x):
        """
        :param x: x must be batch_size times 1
        :return:
        """
        x = x.unsqueeze(1)
        d = 1.0 / ((x - self.centroid).abs() + EPS)
        w = F.softmax(d.squeeze(2), 1)
        v = torch.mm(w, self.embedding.weight)
        return v


if __name__ == '__main__':
    batch_size = 4
    embedding_dim = 5
    num_level = 10
    centroid = torch.randn(num_level)
    x = torch.randn(batch_size, 1)
    entity_embedding = EntityEmbeddingLayer(num_level, embedding_dim, centroid)
    result = entity_embedding(x)
