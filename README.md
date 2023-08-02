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

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
