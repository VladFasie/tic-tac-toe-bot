from activation import relu, leaky_relu, tanh, sigmoid

import numpy as np
import pickle
import os


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
            layer = NeuralNetwork.init_layer(input_size, neurons, activation_function_name)
            self.layers.append(layer)
            input_size = neurons

    @staticmethod
    def init_layer(number_of_inputs, neurons_in_layer, activation_function_name):
        weights = np.random.rand(neurons_in_layer, number_of_inputs)
        biases = np.random.rand(neurons_in_layer, 1)
        activation = NeuralNetwork.activations[activation_function_name]
        activation_vectorized = np.vectorize(activation)
        return weights, biases, activation_vectorized, activation_function_name

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

    def save(self, file_name):
        directory = os.path.join(os.path.dirname(__file__), 'models')
        if not os.path.exists(directory):
            os.makedirs(directory)
        name = os.path.join(directory, str(file_name))
        with open(name, 'wb') as f:
            f.write(pickle.dumps(self))

    @classmethod
    def load(cls, file_name):
        directory = os.path.join(os.path.dirname(__file__), 'models')
        name = os.path.join(directory, str(file_name))
        with open(name, 'rb') as f:
            return pickle.load(f)
