from Matrix import Matrix
import math
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def dsigmoid(x):
    return x * (1 - x)


class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        # Initializing weights
        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        # Initializing biases
        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        # Initializing node values
        self.inputs = 0
        self.hidden = 0
        self.outputs = 0
        # Learning Rate
        self.lr = 0.1

    def FeedForward(self, arr):
        # Hidden nodes
        self.inputs = Matrix.FromArray(arr)
        self.hidden = Matrix.Multiply(self.weights_ih, self.inputs)
        self.hidden.Add(self.bias_h)
        self.hidden.Map(sigmoid)
        # Output nodes
        self.outputs = Matrix.Multiply(self.weights_ho, self.hidden)
        self.outputs.Add(self.bias_o)
        self.outputs.Map(sigmoid)
        return self.outputs

    def Train(self, inputs, targets):
        # Calc errors
        self.FeedForward(inputs)
        targets = Matrix.FromArray(targets)
        output_errors = Matrix.Subtract(targets, self.outputs)
        weights_ho_T = Matrix.Transpose(self.weights_ho)
        hidden_errors = Matrix.Multiply(weights_ho_T, output_errors)
        # Calc gradients
        gradient_o = Matrix.StaticMap(self.outputs, dsigmoid)
        gradient_o.ElementMultiply(output_errors)
        gradient_o.ElementMultiply(self.lr)
        hidden_T = Matrix.Transpose(self.hidden)
        delta_weights_ho = Matrix.Multiply(gradient_o, hidden_T)

        gradient_h = Matrix.StaticMap(self.hidden, dsigmoid)
        gradient_h.ElementMultiply(hidden_errors)
        gradient_h.ElementMultiply(self.lr)
        input_T = Matrix.Transpose(self.inputs)
        delta_weights_ih = Matrix.Multiply(gradient_h, input_T)

        # Adjusting weights and biases
        # self.weights_ih.Display()
        self.weights_ih.Add(delta_weights_ih)
        self.bias_h.Add(gradient_h)
        # delta_weights_ho.Display()
        self.weights_ho.Add(delta_weights_ho)
        self.bias_o.Add(gradient_o)
