# Tensor Class

This repository contains a Python class, `Tensor`, that facilitates the manipulation and grouping of data into multi-dimensional tensors. The `Tensor` class can be used to generate tensors of different shapes from a given list of data.

## How to Use

1. First, ensure you have Python 3 installed on your computer.

2. Clone or download this repository to your local machine.

3. Use the `Tensor` class to create your tensors. The class constructor takes two parameters:
   - `data`: A list containing the data elements that you want to form into a tensor.
   - `shape`: A list representing the shape of the desired tensor.

4. To create an instance of the `Tensor` class, simply provide the `data` and `shape` as arguments. For example:
   ```python
   data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
   shape1 = [2, 3, 2]
   tensor1 = Tensor(data1, shape1)
   ```

5. Once you have created an instance of the `Tensor` class, you can call the `shape_data()` method to generate the tensor. The method will group the data according to the specified shape. For example:
   ```python
   tensor1.shape_data()
   ```

## Example

```python
# Import the Tensor class from the module (assuming it's in a file named 'tensor.py')
from tensor import Tensor

# Create a tensor with data1 and shape1
data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape1 = [2, 3, 2]
tensor1 = Tensor(data1, shape1)
tensor1.shape_data()

# Create a tensor with data2 and shape2
data2 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape2 = [5, 2]
tensor2 = Tensor(data2, shape2)
tensor2.shape_data()

# Create a tensor with data3 and shape3
data3 = [0, 1, 2, 3, 4]
shape3 = [4]
tensor3 = Tensor(data3, shape3)
tensor3.shape_data()
```
# Building a Dense Neural Network Layer using Tensor Class Initialization and Usage

This repository provides code for initializing and using neural network layers, including a dense layer, using custom tensor manipulation. The repository includes a `Tensor` class and a `Dense` class to create and manipulate tensors and implement a dense layer.
Building a custom dense layer. Dense class that takes input, weight, and bias tensors (from tensor class) and implements the forward propagation algorithm to create a dense layer. The forward propagation involves a dot product between the input and weights, followed by the addition of bias.


## Usage

This section outlines how to use the provided code to create and utilize neural network layers.

### 1. Building Input Tensor

The `building_input_tensor` function constructs an input tensor. Modify `input_data` and the number of inputs as needed.

```python
from tensor import Tensor

def building_input_tensor(number_of_input, data):
    global x
    number_of_inputs = number_of_input
    tensor = Tensor(data, [number_of_input])
    x = tensor.shape_data()

# Example usage
input_data = [44, 55, 66, 77]
building_input_tensor(4, input_data)
```

### 2. Building Weight Tensor

The `building_weight_tensor` function constructs a weight tensor for a layer. Modify `number_of_node`, `number_of_input`, and `weights` as needed.

```python
def building_weight_tensor(number_of_node, number_of_input, weights):
    global w
    number_of_nodes = number_of_node
    number_of_inputs = number_of_input
    tensor_1l = Tensor(weights, [number_of_nodes, number_of_inputs])
    w = tensor_1l.shape_data()

# Example usage
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
building_weight_tensor(4, 4, weights)
```

### 3. Building Bias Tensor

The `building_bias_tensor` function constructs a bias tensor for a layer. Modify `number_of_input`, `data`, and `rows` as needed.

```python
def building_bias_tensor(number_of_input, data):
    global b
    number_of_inputs = number_of_input
    data = data * number_of_input
    tensor = Tensor(data, [number_of_input])
    b = tensor.shape_data()

# Example usage
rows = 4
bias = 8
building_bias_tensor(rows, bias)
```

### 4. Initialize a Dense Layer

The `Dense` class allows you to create and use a dense layer. Initialize the layer with input, weight, and bias tensors, and then use the `forward()` method for forward propagation.

```python

# Example usage
dense0 = Dense(x, w, b)
output = dense0.forward()
print("Layer output:", output)
```

### 5. Building Parameters for Multiple Layers

The `initialize_parameters` function initializes parameters for multiple layers. Modify `layers_dims` and customize the initialization as needed.

```python
def initialize_parameters(layers_dims):
    parameters = {}
    L = len(layers_dims)
    for l in range(1, L):
        t = Tensor([0], [layers_dims[l], layers_dims[l - 1]])
        parameters["W" + str(l)] = t.shape_data()
        bb = Tensor([0], [layers_dims[l], 1])
        parameters["b" + str(l)] = bb.shape_data()
    return parameters

# Example usage
parameters = initialize_parameters([4, 5, 3, 2])
print("Initialized parameters:", parameters)
```

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


---
