# deep_learning
- USER
请生成一段深度学习的pytorch框架代码
- GPT 
```
import torch
import torch.nn as nn
import torch.optim as optim

# 定义一个简单的深度学习模型
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)  # 输入层到隐藏层
        self.fc2 = nn.Linear(256, 128)  # 隐藏层到隐藏层
        self.fc3 = nn.Linear(128, 10)  # 隐藏层到输出层

    def forward(self, x):
        x = x.view(-1, 784)  # 将输入展平为一维向量
        x = torch.relu(self.fc1(x))  # 隐藏层1使用ReLU激活函数
        x = torch.relu(self.fc2(x))  # 隐藏层2使用ReLU激活函数
        x = self.fc3(x)  # 输出层不使用激活函数
        return x

# 创建模型实例
model = SimpleNet()

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 加载训练数据
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

# 训练模型
for epoch in range(num_epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()  # 梯度清零
        output = model(data)  # 前向传播
        loss = criterion(output, target)  # 计算损失
        loss.backward()  # 反向传播
        optimizer.step()  # 更新参数

    # 每个epoch结束后打印损失
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))
```
- USER
exit
