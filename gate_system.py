import math
from math import *
import numpy as np
from qiskit.providers import BackendV2
from qiskit.providers.fake_provider import FakeBackend
from qiskit.quantum_info import Statevector
from qiskit_aer import *
from typing import Optional
import qiskit
from qiskit import QuantumRegister, QuantumCircuit, transpile

import numpy as np


def CX(state_vector, control=0, target=1):
    """
    Applies a CNOT gate to the given quantum state vector using Qiskit,
    accounting for qubit ordering conventions.

    Parameters:
    - state_vector: List or numpy array representing the quantum state vector.
    - control: Index of the control qubit (default is 0).
    - target: Index of the target qubit (default is 1).

    Returns:
    - output_state: The resulting state vector after applying the CNOT gate.
    """
    # Ensure the state vector is a numpy array and normalized
    state_vector = np.array(state_vector, dtype=complex)
    norm = np.linalg.norm(state_vector)
    if norm == 0:
        raise ValueError("State vector cannot be zero.")
    state_vector = state_vector / norm

    # Determine the number of qubits needed
    num_qubits = int(np.log2(len(state_vector)))
    if len(state_vector) != 2 ** num_qubits:
        raise ValueError("Length of state vector must be a power of 2.")
    if num_qubits < 2:
        raise ValueError("At least 2 qubits are required for a CNOT gate.")
    if control >= num_qubits or target >= num_qubits:
        raise ValueError("Control and target qubit indices must be within the number of qubits.")

    # Reverse the state vector to match Qiskit's qubit ordering
    reversed_state_vector = state_vector.copy()[::-1]

    # Create a quantum circuit with the required number of qubits
    qc = QuantumCircuit(num_qubits)

    # Initialize the qubits to the desired state
    qc.initialize(reversed_state_vector, qc.qubits)

    # Apply CNOT gate with specified control and target qubits
    # Adjust qubit indices to match Qiskit's ordering
    adjusted_control = num_qubits - 1 - control
    adjusted_target = num_qubits - 1 - target
    qc.cx(adjusted_control, adjusted_target)

    # Simulate the circuit to get the resulting state vector
    backend = Aer.get_backend('statevector_simulator')
    result = backend.run(transpile(qc, backend)).result()
    output_state = result.get_statevector(qc)

    # Reverse the output state vector back to original qubit ordering
    # output_state = output_state[::-1]

    return output_state


# Write a 2 qubit gate system for cnot, hadamard
# 2 qubit matrix, Cnot matrix, hadamard matrix
# Run code and initialize qubits, then can apply gates and it works as expected
# |00> H then CNOT -> 1/sqrt2 |00> + 1/sqrt2 |11>
# Express each qubit as a matrix of [a, b] (a over b) then tensor product of another matrix to return the expected value
# Tensor products
class qubits:
    def __init__(self, A):
        self.A = np.array(A)
        n = float(np.log2(len(self.A)))
        if not n.is_integer():
            raise ValueError("Array needs to be a value of 2^n")
        self.num_qubits = int(n)

    def get_qubit_value(self, q):
        sum = 0
        for i in range(len(q[1:])):
            sum += (i+1) * q[i+1]
        return sum

    def H(self):
        arr = np.array([[1, 1], [1, -1]])
        return (1 / sqrt(2)) * np.tensordot(np.array(self.A), arr, 1)

    def Cnot(self):
        arr = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        return np.array(np.dot(self.A, arr))
        # if self.A[0] == 0 and self.A[1] == 1:
        #     self.A[2] = 1 - self.A[2]
        #     self.A[3] = 1 - self.A[3]
        # return self.A
    # def Cnot(self, control=0, target=1):
    #     if not self.num_qubits.is_integer():
    #         raise ValueError("Array must be power of two")
    #
    #     values = self.qubit_to_int(self.A)
    #     if values[control] == 1:
    #         values[target] = 1 - values[control]
    #     return values

    def qubit_to_int(self, cx=None):
        if cx is None:
            cx = self.A
        res = []
        for i in range(int(len(cx) / self.num_qubits)):
            res.append(int(self.get_qubit_value(cx[np.power(2, self.num_qubits-1) * i:np.power(2, self.num_qubits-1) * (i+1)])))
        return res




arrs = [[1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 0, 1], [1, 0, 1, 0]]
for arr in arrs:
    q = qubits(arr)
    d = CX(Statevector(arr)).data
    b = []
    for a in range(len(d)):
        b.append(float(2 * np.round(np.abs(d[a] * d[a]), 2).real))
    # print("Given: " + str(qubit_to_int(arr)) + " Result: " + str(qubit_to_int(b)))
    # print("Result :" + str(qubit_to_int(q.Cnot())))
    # print("Original: " + str(arr))
    print("Original: " + str(q.qubit_to_int(arr)))
    print("Expected: " + str(b))
    print("Result: " + str(q.Cnot()))
    print('______________')
# Represent an N dimensional qubit system as a tensor

# Find out what a tensor is and how to operate on it
# Represent a qubit state as a tensor
# Try a 1 qubit gate on the tensor
# Tensor only applies to what is important in the system
# Professor David