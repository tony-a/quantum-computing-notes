# QC notes

Quantum computing takes advantage of two quantum phenomena that we don't observe at the macro scale. The two phenomena being:
- **Superposition** - The ability of a particle to switch itself from one state to another, following some knowable probabilistic distribution. 
[13 minute overview](https://www.youtube.com/watch?v=VwWRX9IdblE)
- **Entanglement** - When a property of a particle (such as spin, polarization or momentum) is coupled with a counter particle, such that the state of one cannot be described without taking into account the state of the other.
[17 minute video on the topic](https://www.youtube.com/watch?v=-WSWz1H3mJg&t=616s)

Preformance:
Measuring the preformance of a quantum computer, is dependent on multiple aspects:
1. Number of qubits in the system.
2. Quantum volume, a new measuring-concept recently introduced by IBM that takes into consideration the number of qubits along with the number of gates and measurement errors, device cross talk, as well as device connectivity and circuit compiler efficiency.
[article](https://newsroom.ibm.com/2019-03-04-IBM-Achieves-Highest-Quantum-Volume-to-Date-Establishes-Roadmap-for-Reaching-Quantum-Advantage)


# Learning materials:

To learn the CS and Math side of quantum computing:
[Hour and half video](https://www.youtube.com/watch?v=F_Riqjdh2oM), requires some basic background of linear algebra. 

To learn the programming side of quantum computing:
[Playlist of 9 vides, about 15 minutes each](https://www.youtube.com/playlist?list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY). Using Qiskit, a python library, doesn't require understanding of quantum mechanics.

## Qubits:
Several quantum particules can be used as a qubit, including [the outer electron of a phosphours atom](https://www.youtube.com/watch?v=zNzzGgr2mhk), or by leveraging the polarization property of a photon.


## Quantum gates:
Understanding how to preform operations on qubits.
[10 minutes](https://www.youtube.com/watch?v=gz5rjhiU4ao)


## Quantum Decoherence
Why does it take so long for us to increase the number of qubits in a circuit?

Why can't we slap more curcuits together?

[First 3 minutes of this video](https://www.youtube.com/watch?v=LsxJmHS0cc8)

[Quantum volume](https://www.youtube.com/watch?v=-7L5o-mzLqU)
