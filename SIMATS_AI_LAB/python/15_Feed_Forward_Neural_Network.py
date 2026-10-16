import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(42)
w1 = np.random.uniform(size=(2, 2))
w2 = np.random.uniform(size=(2, 1))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for epoch in range(5000):
    hidden = sigmoid(np.dot(X, w1))
    output = sigmoid(np.dot(hidden, w2))

    error = y - output
    d_output = error * output * (1 - output)

    error_hidden = d_output.dot(w2.T)
    d_hidden = error_hidden * hidden * (1 - hidden)

    w2 += hidden.T.dot(d_output) * 0.5
    w1 += X.T.dot(d_hidden) * 0.5

print('Predictions:')
for i in range(4):
    print(X[i], '->', int(output[i][0] > 0.5))
