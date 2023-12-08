import torch
import torchvision
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch.nn as nn
from torchvision.transforms import transforms
import torch.nn.functional as F


# Define the CNN model (you can also use 2 connected layers (fc1 and fc2), the second connected layer (fc2) is just commented out)
class CNN_MNIST(nn.Module):
    def __init__(self, input_channels=1, output_size=10):
        super(CNN_MNIST, self).__init__()
        self.conv1 = nn.Conv2d(input_channels, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(64 * 7 * 7, output_size) #singe layer.  7 * 7 here because 28 (input dimension of image) / 2 * 2 (pooling size * number of layers)
        #self.fc1 = nn.Linear(64 * 7 * 7, 128)
        #self.fc2 = nn.Linear(128, output_size)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = x.view(-1, 64 * 7 * 7) # single layer
        #x = F.relu(self.fc1(x))
        #x = self.fc2(x)
        x = self.fc1(x)
        return x

# Load MNIST dataset
train_dataset = torchvision.datasets.MNIST('./data', train=True, transform=transforms.Compose([transforms.ToTensor()]))
test_dataset = torchvision.datasets.MNIST('./data', train=False, transform=transforms.Compose([transforms.ToTensor()]))

# Create data loaders
train_dataloader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=100, shuffle=True)
test_dataloader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=100, shuffle=True)

# Instantiate the CNN model
input_size = 1
output_size = 10
cnn_model = CNN_MNIST(input_channels=input_size, output_size=output_size)

# Define the optimizer and criterion
lr_rate = 0.01
optimizer = torch.optim.Adam(cnn_model.parameters(), lr=lr_rate)
criterion = nn.CrossEntropyLoss()

# Training loop
num_epochs = 4
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_dataloader):
        optimizer.zero_grad()
        outputs = cnn_model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# Save the trained model
torch.save(cnn_model.state_dict(), 'trained_cnn_model.pth')

# Evaluation on the test set
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_dataloader:
        output = cnn_model(images)
        _, prediction = torch.max(output, 1)
        n_samples += labels.size(0)
        n_correct += (prediction == labels).sum().item()

accuracy = (n_correct / n_samples) * 100
print(f'Test Accuracy: {accuracy:.2f}%')
