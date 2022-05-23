import torch
import torch.nn as nn
import torch.nn.functional as F


class LSTM(nn.Module):
    def __init__(self):
        super(LSTM, self).__init__()
        self.lstm = nn.LSTM(10,
                            15,
                            num_layers=1,
                            bidirectional=True,
                            dropout=0.1)

    def forward(self, x):
        output, (hidden, cell) = self.lstm(x)
        return output, hidden, cell


if __name__ == '__main__':
    x = torch.rand([8, 100, 10]).detach()
    permute_x = x.permute([1, 0, 2])
    lstm = LSTM()
    ouput_lstm1 , output_lstm2, output_lstm3 = lstm(permute_x)