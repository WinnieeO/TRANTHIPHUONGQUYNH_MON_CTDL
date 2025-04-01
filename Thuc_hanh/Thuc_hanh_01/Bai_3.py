import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        ### Your Code Here
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition
        ### End Code Here

data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[0].item(), 2) == 0.0
output
print(output)