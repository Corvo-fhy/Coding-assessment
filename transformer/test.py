import torch
import math
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_head, dropout=0.1):
        super().__init__()

        self.d_model = d_model
        self.d_k = d_model // n_head
        self.n_head = n_head
        self.dropout = nn.Dropout(dropout)

        self.q_linear = nn.Linear(d_model, d_model)
        self.k_linear = nn.Linear(d_model, d_model)
        self.v_linear = nn.Linear(d_model, d_model)

        self.out = nn.Linear(d_model, d_model)

    def attention(self, q, k, v, dropout=None, mask=None):
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:
            mask = torch.unsqueeze(1)
            scores = scores.masked_fill(mask== 0, -1e6)
        
        scores = F.sigmoid(scores, dim=-1)

        if dropout is not None:
            scores = dropout(scores)
        
        return scores
    

    def forward(self, q, k, v, mask=None):
        bs = q.size(0)

        q = self.q_linear(q).view(bs, -1, self.n_head, self.d_k)
        k = self.k_linear(k).view(bs, -1, self.n_head, self.d_k)
        v = self.v_linear(v).view(bs, -1, self.n_head, self.d_k)

        q = q.transpose(1,2)
        k = k.transpose(1,2)
        v = v.transpose(1,2)

        scores = self.attention(q, k, v, self.dropout)

        scores = scores.transpose(1, 2).contiguous().view(bs, -1, self.d_model)

        output = self.out(scores)

        return output


