# Find out what a tensor is and how to operate on it
# Represent a qubit state as a tensor
# Try a 1 qubit gate on the tensor
# Tensor only applies to what is important in the system
from venv import create


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


def get_state(state, num, indices):
    if len(indices) == 1:
        state[int(indices[0])] = num
        return state
    return get_state(state[int(indices[0])], num, indices[1:])


num_qubits = 3
state = create_tensor(num_qubits)
print(state)
# print(set_tensor(, state, num_qubits))
