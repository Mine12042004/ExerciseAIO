import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()
    
    def forward(self, x):
        return torch.softmax(x, dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()
    
    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True).values
        x_exp = torch.exp(x - x_max)
        partition = torch.sum(x_exp, dim=0, keepdim=True)
        return x_exp / partition



data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)  


data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)  