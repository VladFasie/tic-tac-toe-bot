import numpy as np


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))


def tanh(Z):
    return np.tanh(Z)


def relu(Z):
    return np.maximum(0, Z)


def leaky_relu(Z):
    return np.maximum(0.1 * Z, Z)
