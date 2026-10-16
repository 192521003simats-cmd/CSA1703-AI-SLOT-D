tree = {
    'Sunny': {'High': 'No', 'Normal': 'Yes'},
    'Overcast': 'Yes',
    'Rain': {'High': 'No', 'Normal': 'Yes'}
}

def predict(sample):
    outlook, humidity = sample
    decision = tree[outlook]
    if isinstance(decision, dict):
        return decision[humidity]
    return decision

test = ('Sunny', 'Normal')
print('Sample:', test)
print('Play Decision:', predict(test))
