import torch
import math
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_head, dropout=0.1):
        self.d_model = d_model
        self.n_head = n_head
        self.d_k = d_model // n_head
        
        self.linear_Q = nn.Linear(d_model, d_model)
        self.linear_K = nn.Linear(d_model, d_model)
        self.linear_V = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

        self.output = nn.Linear(d_model, d_model)

    def attention(self, q, k, v, mask=None, dropout=None):
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:
            mask = mask.unsqueeze(1)
            scores = scores.masked_fill(mask==0, -1e9)
        
        scores = F.softmax(scores, dim=-1)

        if dropout is not None:
            scores = self.dropout(scores)

        output = torch.matmul(scores, v)
        
        return output

    def forward(self, q, k, v, mask=None):
        bs = q.size(0)

        # (batch_size, seq_length, n_head, d_k)
        q = self.linear_Q(q).view(bs, -1, self.n_head, self.d_k)
        k = self.linear_K(k).view(bs, -1, self.n_head, self.d_k)
        v = self.linear_V(v).view(bs, -1, self.n_head, self.d_k)

        # (batch_size, n_head, seq_length, d_k)
        q = q.transpose(1,2)
        k = k.transpose(1,2)
        v = v.transpose(1,2)
        
        scores = self.attention(q, k, v, mask=None, dropout=self.dropout)

        concat = scores.transpose(1, 2).contiguous().view(bs, -1, self.d_model)

        output = self.output(concat)

        return output