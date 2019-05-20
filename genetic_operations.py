from nn import NeuralNetwork
from helpers import choose

from random import randint

mutation_rate = 2  # %
mutation_range = 15  # %

def crossover(n1: NeuralNetwork, n2: NeuralNetwork) -> NeuralNetwork:
    if n1.input_size != n2.input_size:
        raise Exception('not compatible networks')
    input_size = n1.input_size

    layers = []
    for l1, l2 in zip(n1.layers, n2.layers):
        a1 = l1[3]
        a2 = l2[3]
        if len(l1[0]) != len(l2[0]):
            raise Exception('not compatible layers')
        s = len(l1[0])
        layer = [s, choose(a1, a2)]
        layers.append(layer)

    result = NeuralNetwork(input_size, layers)
    for l in range(len(result.layers)):

        w = result.layers[l][0]
        for i in range(len(w)):
            for j in range(len(w[0])):
                val = choose(n1.layers[l][0][i][j], n2.layers[l][0][i][j])
                w[i][j] = mutate(val)

        b = result.layers[l][1]
        for i in range(len(b)):
            for j in range(len(b[0])):
                val = choose(n1.layers[l][1][i][j], n2.layers[l][1][i][j])
                b[i][j] = mutate(val)

    return result


def mutate(val):
    if randint(1, 100) <= mutation_rate:
        deviation = val * randint(1, mutation_range) / 100
        if randint(0, 1) == 0:
            return val + deviation
        else:
            return val - deviation
    return val

def test():
    a = NeuralNetwork(3, [[2, 'sigmoid'], [1, 'relu']])
    b = NeuralNetwork(3, [[2, 'sigmoid'], [1, 'sigmoid']])

    print(a.layers)
    print(b.layers)

    print(crossover(a, b).layers)

