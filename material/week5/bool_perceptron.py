from random import randrange

inputs = [[0,0],[0,1],[1,0],[1,1]]
inputsNOT = [[0],[1]]

targetsAND = [-1,-1,-1,1]
targetsOR = [-1,1,1,1]
targetsNAND = [1,-1,-1,-1]
targetsNOT = [-1,1]

targetsXOR = [-1,1,1,-1]

eta = 0.1


def update(target, output, inputs):
	perceptron[0] = perceptron[0] + eta*(target-output)*1
	for i in range(len(inputs)):
		perceptron[i+1] = perceptron[i+1] + eta*(target-output)*inputs[i]

def train(inputs, targets):
	for i in range(1000):
		idx = randrange(len(inputs))
		out = forward(perceptron, inputs[idx])
		update(targets[idx], out, inputs[idx])

def weightedsum(weights, values):
	return sum(weights[i]*values[i] for i in range(len(weights)))

def forward(perceptron, inputs):
	return perceptron[0] + weightedsum(perceptron[1:], inputs)



print '\nTRAIN AND'
perceptron = [0.2, 0.1, 0.3]

train(inputs,targetsAND)
print forward(perceptron, [0, 0])
print forward(perceptron, [0, 1])
print forward(perceptron, [1, 0])
print forward(perceptron, [1, 1])

print '\nTRAIN OR'
perceptron = [0.2, 0.1, 0.3]
train(inputs,targetsOR)
print forward(perceptron, [0, 0])
print forward(perceptron, [0, 1])
print forward(perceptron, [1, 0])
print forward(perceptron, [1, 1])

print '\nTRAIN NAND'
perceptron = [0.2, 0.1, 0.3]
train(inputs,targetsNAND)
print forward(perceptron, [0, 0])
print forward(perceptron, [0, 1])
print forward(perceptron, [1, 0])
print forward(perceptron, [1, 1])

print '\nTRAIN NOT'
perceptron = [0.2, 0.1]
train(inputsNOT,targetsNOT)
print forward(perceptron, [0])
print forward(perceptron, [1])

print '\nTRAIN XOR'
perceptron = [0.2, 0.1, 0.3]
train(inputs,targetsXOR)
print forward(perceptron, [0, 0])
print forward(perceptron, [0, 1])
print forward(perceptron, [1, 0])
print forward(perceptron, [1, 1])
