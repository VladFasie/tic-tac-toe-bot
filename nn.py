from activation import relu, leaky_relu, tanh, sigmoid
import numpy as np

class NeuralNetwork:

    activations = {'sigmoid': sigmoid,
                   'relu': relu,
                   'tanh': tanh}

    def __init__(self, input_size, hidden_layer):
        self.layers = []
        self.input_size = input_size
        for i in range(len(hidden_layer)):
            neurons = hidden_layer[i][0]
            activation_function_name = hidden_layer[i][1]
            layer = self._init_layer(input_size, neurons, activation_function_name)
            self.layers.append(layer)
            input_size = neurons

    def _init_layer(self, number_of_inputs, neurons_in_layer, activation_function_name):
        weights = np.random.rand(neurons_in_layer, number_of_inputs)
        biases = np.random.rand(neurons_in_layer, 1)
        activation = NeuralNetwork.activations[activation_function_name]
        activation_vectorized = np.vectorize(activation)
        return (weights, biases, activation_vectorized)

    def unbind_neurons(self, hidden_layer_index, neuron_index, neuron_index_from_previous_layer):
        weights = self.layers[hidden_layer_index][0]
        weights[neuron_index][neuron_index_from_previous_layer] = 0.0

    def feed_forward(self, input):
        input = np.array(input)
        input.shape = (self.input_size, 1)
        for i in range(len(self.layers)):
            layer = self.layers[i]
            w = layer[0]
            b = layer[1]
            f = layer[2]
            input = f(np.matmul(w, input) + b)
        return input
