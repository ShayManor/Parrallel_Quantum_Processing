# Find out what a tensor is and how to operate on it
# Represent a qubit state as a tensor
# Try a 1 qubit gate on the tensor
# Tensor only applies to what is important in the system
import copy
from venv import create
import numpy as np


def hadamard(tensor):
    T0JK = tensor[0]
    T1JK = tensor[1]
    added = add_tensor(copy.deepcopy(T0JK), copy.deepcopy(T1JK.copy()), num_qubits - 1)
    subtracted = subtract_tensor(T0JK.copy(), T1JK.copy(), num_qubits - 1)
    t = [added, subtracted]
    multiply_by_scalar(t, 1 / (2 ** 0.5))
    return t
    # T0JK = multiply_by_scalar(, (1 / (2 ** 0.5)))


def multiply_by_scalar(tensor, scalar):
    for i in range(2 ** num_qubits):
        binary = format(i, '#0' + str(2 + num_qubits) + 'b')[2:]
        multiply(tensor, scalar, binary)
    return tensor1


def multiply(tensor, scalar, indices):
    if str(tensor).count('[') == 1:
        tensor[int(indices[0])] *= scalar
        np.round(tensor[int(indices[0])], 3)
        return tensor
    return multiply(tensor[int(indices[0])], scalar, indices[1:])


def sub_tensor_subtraction(first_tensor, second_tensor, indices):
    if str(first_tensor).count('[') == 1:
        num = second_tensor[int(indices[0])]
        first_tensor[int(indices[0])] = first_tensor[int(indices[0])] - num
        return first_tensor
    first_tensor[int(indices[0])] = sub_tensor_subtraction(first_tensor[int(indices[0])], second_tensor[int(indices[0])], indices[1:])
    return first_tensor


def subtract_tensor(tensor1, tensor2, num_qubits):
    for i in range(2 ** num_qubits):
        binary = format(i, '#0' + str(2 + num_qubits) + 'b')[2:]
        sub_tensor_subtraction(tensor1, tensor2, binary)
    return tensor1


def add_tensor_addition(first_tensor, second_tensor, indices):
    if str(first_tensor).count('[') == 1:
        first_tensor[int(indices[0])] += second_tensor[int(indices[0])]
        return first_tensor
    return add_tensor_addition(first_tensor[int(indices[0])], second_tensor[int(indices[0])], indices[1:])


def add_tensor(tensor1, tensor2, num_qubits):
    for i in range(2 ** num_qubits):
        binary = format(i, '#0' + str(2 + num_qubits) + 'b')[2:]
        add_tensor_addition(tensor1, tensor2, binary)
    return tensor1


def get_tensor(indices, tensor):
    return get_state(tensor, indices, np.log2(len(tensor)))


def create_tensor(num_qubits, state=None):
    if state == None:
        state = [1, 0]

    if num_qubits == 1:
        return state

    return [create_tensor(num_qubits - 1, state).copy(), create_tensor(num_qubits - 1, state).copy()]


def set_tensor(values, tensor, num_qubits):
    for i in range(2 ** num_qubits):
        binary = format(i, '#0' + str(2 + num_qubits) + 'b')[2:]
        tensor = set_value(binary, values[i], tensor, num_qubits)
    return tensor


def set_value(indices, num, state, num_qubits):
    get_state(state, num, indices)
    return state


def add_to_state(state, num, indices):
    if len(indices) == 1:
        state[int(indices[0])] += num
        return state
    return get_state(state[int(indices[0])], num, indices[1:])


def get_state(state, num, indices):
    if len(indices) == 1:
        state[int(indices[0])] = num
        return state
    return get_state(state[int(indices[0])], num, indices[1:])


num_qubits = 3
tensor1: list = create_tensor(num_qubits)
tensor2: list = create_tensor(num_qubits)
set_tensor([1, 0, 1, 0, 1, 0, 0, 1], tensor1, num_qubits)
tensor1.reverse()
# set_tensor([1, 0, 0, 1, 0, 1, 1, 1], tensor2, num_qubits)
print(tensor1)
print(hadamard(tensor1))
