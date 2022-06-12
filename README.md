# QC notes

[Objective](#objective):
# Objective

These notes are a collection of videos and lectures I've found to be helpful on the theory and application of Quantum Computing. Along with personal notes and definitions of some key concepts.


Quantum computing takes advantage of two quantum phenomena that we don't observe at the macro scale. 

### What are these magical phenomena??
- **Superposition** - The ability for a particle to be in a linear combination of it's basis states.
	
  Possible values for a qubit |ψ>:

  - |0> 
  - |1> 
  - some combination of both: 75% |0> + 25% |1>
  - some other combination: 4% |0> + 96% |1>
  - and an infinite other ways of combining the two basis states: |0> and |1>


  (Here's a [13 minute video](https://www.youtube.com/watch?v=VwWRX9IdblE) on the topic by Up and Atom on Youtube)

- **Entanglement** - When a property of a particle (such as spin, polarization or momentum) is coupled with a counter particle, such that the state of one cannot be described without taking into account the state of the other.

  ([17 minute video on the topic](https://www.youtube.com/watch?v=-WSWz1H3mJg)

Performance:


Measuring the performance of a quantum computer, is dependent on multiple aspects:
1. Number of qubits in the system.
2. Quantum volume, a newly introduced measuring-concept by IBM that takes into consideration the number of qubits along with the number of gates and measurement errors, device cross talk, as well as device connectivity and circuit compiler efficiency.
[article](https://newsroom.ibm.com/2019-03-04-IBM-Achieves-Highest-Quantum-Volume-to-Date-Establishes-Roadmap-for-Reaching-Quantum-Advantage)


### So what is a Quantum State?

A quantum state is a description of what a quantum particle is.
a quantum state is a description of an isolated quantum system.
a quantum state provides a probability distribution for the value for each observable of a quantum system.

The mathematical a quantum state does not provide an exact value for an observable at any given moment of time, but instead, just a probability.
some observables, or measurable attributes of a quantum system are:
- position
- momentum
- energy
- spin
- polarization


# Learning materials:

To learn the theory and Math side of quantum computing:
[Hour and half video](https://www.youtube.com/watch?v=F_Riqjdh2oM), requires some basic background of linear algebra. 

To learn the programming side of quantum computing:
[Playlist of 9 videos, about 15 minutes each](https://www.youtube.com/playlist?list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY). Using Qiskit, a python library, doesn't require understanding of quantum mechanics.

## Qubits:
Several quantum particles can be used as a qubit, including [the outer electron of a phosphors atom](https://www.youtube.com/watch?v=zNzzGgr2mhk), or by leveraging the polarization property of a photon (https://www.youtube.com/watch?v=ofg335d3BJ8).


## Quantum gates:
Understanding how to preform operations on qubits.
[10 minutes](https://www.youtube.com/watch?v=gz5rjhiU4ao)

list of gates:

#### Single qubit gates:
- Hadamard gate (H) -- on qubit 0, puts it into the superposition state (|0⟩+|1⟩)/sqrt(2)


#### Controlled gates:
Controlled gates act on 2 or more qubits, where one qubit is the target qubit, and the rest act as controll for whether or not an operation happens

- CNOT 
  - The controlled NOT gate (or CNOT or CX) acts on 2 qubits, and performs the NOT operation on the second qubit only when the first qubit is 
|1⟩

https://quantum-computing.ibm.com/support/guides/gate-overview?section=5d00d964853ef8003c6d6820#

## Quantum Decoherence
Why does it take so long for us to increase the number of qubits in a circuit?

Why can't we slap more circuits together?

[First 3 minutes of this video](https://www.youtube.com/watch?v=LsxJmHS0cc8)

[Quantum volume](https://www.youtube.com/watch?v=-7L5o-mzLqU)




Algo:
https://en.wikipedia.org/wiki/Bernstein–Vazirani_algorithm

# Additional Resources:
[Basic Liner Algebra summary ](https://www.youtube.com/watch?v=rowWM-MijXU)



non locality
interference
superposition
entanglement 


