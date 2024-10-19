from qiskit import *
# Write a 2 qubit gate system for cnot, hadamard
# 2 qubit matrix, Cnot matrix, hadamard matrix
# Run code and initialize qubits, then can apply gates and it works as expected
# |00> H then CNOT -> 1/sqrt2 |00> + 1/sqrt2 |11>
# Express each qubit as a matrix of [a, b] (a over b) then tensor product of another matrix to return the expected value
# Tensor products

class EdgeDetection:
    def __init__(self):
        self.A = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]

    def edge_detection(self):
        if len(self.A) <= 1:
            return
        num_qubits = 3  # Precision
        qc = QuantumCircuit(num_qubits * (len(self.A) - 1) * len(self.A[0]))
        for i in range(len(self.A) - 1):
            for j in range(len(self.A[0])):
                qc.h(num_qubits * (i * len(self.A[0]) + j))

    def grovers_temp(self, int_list, find_list):  # TODO: Implement Grover's Algorithm
        indices = []
        for i in range(len(int_list)):
            if int_list[i] in find_list:
                indices.append(i)
        return indices
