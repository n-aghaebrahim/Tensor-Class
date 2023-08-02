class Dense:
    def __init__(self, x, weights, bias):
        self.weights = weights
        self.bias = bias
        self.x = x

    def forward(self):
        z_data = []
        for i in range(len(self.weights)):
            z = sum([a * b for a, b in zip(self.weights[i], self.x)]) + self.bias[i]
            z_data.append(z)
        return z_data
