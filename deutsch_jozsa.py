from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def dj_query(num_qubits):

    qc=QuantumCircuit(num_qubits + 1)

    if np.random.randint(0,2):
        qc.x(num_qubits)
    if np.random.randint(0,2):
        return qc

    on_states= np.random.choice(range(2**num_qubits), 2**num_qubits //2, replace=False)

    def add_cx(qc,bit_string):
        for qubit, bit in enumerate(reversed(bit_string)):
            if bit=="1":
                qc.x(qubit)
        return qc

    for state in on_states:
        qc.barrier()
        qc=add_cx(qc, f"{state:0{num_qubits}b}")
        qc.mcx(list(range(num_qubits)), num_qubits)
        qc=add_cx(qc, f"{state:0{num_qubits}b}")
    
    qc.barrier()

    return qc

    
def compile_circuit(function: QuantumCircuit):

    n=function.num_qubits - 1
    qc = QuantumCircuit(n+1, n)

    qc.x(n)
    qc.h(range(n+1))
    qc.barrier()
    qc.compose(function, inplace=True)
    qc.barrier()
    qc.h(range(n))

    qc.measure(range(n), range(n))

    return qc

def dj_algorithm(function: QuantumCircuit):

    qc=compile_circuit(function)

    result=AerSimulator().run(qc, shots=1, memory=True).result()

    measurement=result.get_memory()

    if "1" in measurement[0]:
        return "balanced"
    return "constant"


num_qubits = int(input("Enter the number of input qubits: "))

f = dj_query(num_qubits)

qc=compile_circuit(f)
print("\nThe Oracle circuit:")
print(f.draw())

print("\nThe final Deutsch-Jozsa circuit:")
print(qc.draw())

print("\nDeutsch-Jozsa result:", dj_algorithm(f))
