from qiskit import transpile
from qiskit.providers.aer import QasmSimulator
backend = QasmSimulator()
qc_compiled = transpile(qc, backend)  
job = backend.run(qc_compiled, shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)


from qiskit.visualization import plot_histogram
plot_histogram(counts)

from qiskit import QuantumCircuit
qc = QuantumCircuit
qc.mcry()