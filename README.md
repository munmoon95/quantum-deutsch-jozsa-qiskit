# Deutsch-Jozsa Algorithm with Qiskit

A Qiskit implementation of the Deutsch-Jozsa algorithm with randomly generated constant and balanced oracles.

## Overview

The Deutsch-Jozsa algorithm determines whether a Boolean function is **constant** or **balanced**.

For a function

$$
f:\{0,1\}^n \rightarrow \{0,1\},
$$

- A **constant** function gives the same output for every possible input.
- A **balanced** function gives `0` for exactly half of the possible inputs and `1` for the other half.

This project implements the Deutsch-Jozsa algorithm using Qiskit and simulates the circuit using Qiskit Aer.

The number of input qubits is provided by the user when the program is run.

## Implementation

The program generates either a constant or balanced oracle randomly.

For a balanced function, exactly half of the possible input states are randomly selected:

$$
2^{n-1}
$$

where `n` is the number of input qubits.

For example, with three input qubits there are eight possible input states, so a balanced function must select four states.

The selected states are printed by the program. For example:


The selected states for balanced function are:
[7 5 4 0]


These correspond to:

111
101
100
000

The oracle is constructed by using X gates to transform the selected bit patterns, followed by a multi-controlled X (MCX) gate acting on the auxiliary qubit. The X gates are then applied again to undo the transformation.

Deutsch-Jozsa Circuit

The complete circuit follows these steps:

Initialize the auxiliary qubit in the state |1>.
Apply Hadamard gates to the input and auxiliary qubits.
Apply the generated oracle.
Apply Hadamard gates to the input qubits.
Measure the input qubits.
Determine whether the function is constant or balanced.

The auxiliary qubit is not measured.

Interpreting the Result

For an ideal Deutsch-Jozsa circuit:

A measurement of 000...0 indicates a constant function.
A measurement containing at least one 1 indicates a balanced function.

The program uses one measurement shot because the ideal Deutsch-Jozsa algorithm gives a deterministic result for a valid constant or balanced oracle.

Example

After running the program, the user is asked for the number of input qubits:

Enter the number of input qubits: 3

A possible balanced oracle may select:

[7 5 4 0]

The program then displays the oracle circuit, the complete Deutsch-Jozsa circuit, and the final result:

Deutsch-Jozsa result: balanced

The selected states and circuit change between executions because the oracle is generated randomly.

Requirements
Python 3
Qiskit 2.5.1
Qiskit Aer
NumPy

The required packages are listed in requirements.txt.

Installation

Clone the repository:

git clone https://github.com/munmoon95/quantum-deutsch-jozsa-qiskit.git

Move into the project directory:

cd quantum-deutsch-jozsa-qiskit

Install the dependencies:

pip install -r requirements.txt
Running the Program

Run:

python3 deutsch_jozsa.py

Enter the desired number of input qubits when prompted.

The program displays:

The selected states for a balanced oracle.
The oracle circuit.
The complete Deutsch-Jozsa circuit.
The final classification as constant or balanced.
Project Structure
quantum-deutsch-jozsa-qiskit/
├── deutsch_jozsa.py
├── requirements.txt
├── README.md
└── .gitignore
deutsch_jozsa.py

Contains the implementation of the Deutsch-Jozsa algorithm, including oracle generation, circuit construction, simulation, and classification.

requirements.txt

Lists the Python packages required to run the project.

.gitignore

Specifies files and directories that should not be tracked by Git.

Future Work

Possible extensions include:

Testing the algorithm with different numbers of input qubits.
Studying the effect of noise on the circuit.
Comparing the quantum algorithm with a classical approach.
Running the circuit on quantum hardware.
