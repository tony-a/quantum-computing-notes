## Notes & Exercises on Quantum Computing

### [Udemy Course](https://github.com/tony-a/quantum-computing-notes/tree/main/udemy_course):
Coding exercises following lecture notes from this [Udemy course](https://www.udemy.com/course/quantum-computing-in-python-using-qiskit/) on quantum computing.

#### Setup:
Using anaconda-navigator launch Jupyter notebook after having installed the following two libraries, and then navigate to the folder containing the Jupyter notebooks using the UI.

- pip install qiskit
- pip install pylatexenc


#### Topics covered:

- **Section 5:**
Exercises highlighting different quantum gates acting on single qubits in ground state, |0⟩, and excited state, |1⟩.

- **Section 7:**
Demonstrating how to construct various gates (such as Identity, Hadamard, and Pauli gates) using the most general single qubit gate, U.

- **Section 8:**
An example of quantum interference

- **Section 9:**
A collection of exercises showcasing multi-qubit quantum gates:
  - 9.59: Demonstrating how a SWAP gate can be constructed from a series of CNOT gates.
  - 9.61: Constructing all 4 Bell's states and showing how they are truly entangled states.
  - 9.64: Toffoli gate, and other multi-controlled general gates.
---
### [Cheat Sheet](https://github.com/tony-a/quantum-computing-notes/tree/main/cheat_sheet):
A collection of basic definitions, terminology and common gates.

---
### Random learning materials:
A collection of videos and lectures I've found to be helpful on the theory and application of Quantum Computing.
Most cover the concepts at a high level in laymen terms.

- Quantum computing takes advantage of two quantum phenomena that we don't observe at the macro scale.
   - **Superposition** - The ability for a particle to be in a linear combination of it's basis states.
     [13 minute video](https://www.youtube.com/watch?v=VwWRX9IdblE) on the topic by Up and Atom

   - **Entanglement**- When a property of a particle (such as spin, polarization or momentum) is coupled with a counter particle, such that the state of one cannot be described without taking into account the state of the other.
     [17 minute video on the topic](https://www.youtube.com/watch?v=-WSWz1H3mJg)


- Qubits:
Several quantum particles can be used as a qubit:
  - [The outer electron of a phosphors atom](https://www.youtube.com/watch?v=zNzzGgr2mhk)
  - [The polarization property of a photon](https://www.youtube.com/watch?v=ofg335d3BJ8)
  - [Superconducting qubits](https://www.youtube.com/watch?v=daQJMwvxC_U)


- Quantum decoherence [7 minute video.](https://www.youtube.com/watch?v=LsxJmHS0cc8)


- Quantum volume: A measure to benchmark computers that take into consideration the number of qubits, along with the number of gates and measurement errors, device cross talk, as well as device connectivity and circuit compiler efficiency.
  - [2 minute video](https://www.youtube.com/watch?v=-7L5o-mzLqU)
  - [Article](https://newsroom.ibm.com/2019-03-04-IBM-Achieves-Highest-Quantum-Volume-to-Date-Establishes-Roadmap-for-Reaching-Quantum-Advantage)


- Quantum gates:
Understanding how to preform operations on qubits.
[10 minute video.](https://www.youtube.com/watch?v=gz5rjhiU4ao)


- [A comprehensive and interactive guide to quantum computing by IBM](https://quantum-computing.ibm.com/support/guides/gate-overview?section=5d00d964853ef8003c6d6820#)


- [Quantum algorithms](https://quantumalgorithmzoo.org)

### Additional learning materials and resources:

- To learn the theory and Math side of quantum computing:
[Hour and half video](https://www.youtube.com/watch?v=F_Riqjdh2oM), requires some basic background of linear algebra.


- To learn the programming side of quantum computing:
[Playlist of 9 videos, about 15 minutes each](https://www.youtube.com/playlist?list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY). Using Qiskit, a python library, doesn't require understanding of quantum mechanics.


- [Basic Liner Algebra summary.](https://www.youtube.com/watch?v=rowWM-MijXU)

