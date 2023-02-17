import torch
import torch.nn as nn
import numpy as np
from pydmd import OptDMD

# generate sample data
closing_prices = np.random.rand(100)

# set up OptDMD object and compute dynamic modes
optdmd = OptDMD(svd_rank=2)
optdmd.fit(closing_prices)
dynamic_modes = optdmd.modes.T

# set up LSTM model
class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(input_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        lstm_out, _ = self.lstm(x.view(len(x), 1, -1))
        y_pred = self.fc(lstm_out[-1].view(1, -1))
        return y_pred.view(-1)

# set up hyperparameters
input_dim = 3 # use dynamic modes and the previous 2 closing prices as input
hidden_dim = 10
output_dim = 1
num_epochs = 100
learning_rate = 0.01

# prepare data for LSTM input
X = np.zeros((len(closing_prices)-2, input_dim))
for i in range(len(X)):
    X[i, 0:2] = closing_prices[i:i+2]
    X[i, 2:] = dynamic_modes[i+2]
y = closing_prices[2:]

# convert data to PyTorch tensors
X = torch.Tensor(X)
y = torch.Tensor(y)

# set up LSTM model and optimizer
model = LSTM(input_dim, hidden_dim, output_dim)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# train the LSTM model
for epoch in range(num_epochs):
    optimizer.zero_grad()
    y_pred = model(X)
    loss = nn.MSELoss()(y_pred, y)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss {loss.item()}")

# make a prediction for the next closing price
prev_prices = closing_prices[-2:]
next_dynamic_modes = optdmd.predict(closing_prices[-optdmd.s-1:])
next_input = np.concatenate((prev_prices, next_dynamic_modes))
next_input = torch.Tensor(next_input).unsqueeze(0)
next_pred = model(next_input).item()
print(f"Predicted next closing price: {next_pred}")
