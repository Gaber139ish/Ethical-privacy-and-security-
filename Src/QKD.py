# --- Conceptual QKD using Qiskit ---

from qiskit import QuantumCircuit, Aer, execute

def qkd_protocol(alice_bits):
  """
  Simulates a basic QKD protocol.

  Args:
    alice_bits: A list of bits that Alice wants to send.

  Returns:
    A tuple containing the shared key and the indices of the matching bits.
  """
  qc = QuantumCircuit(len(alice_bits), len(alice_bits))

  # Alice prepares qubits in random bases
  for i, bit in enumerate(alice_bits):
    if bit == 1:
      qc.h(i)  # Hadamard gate for superposition

  # Bob measures qubits in random bases
  qc.measure(range(len(alice_bits)), range(len(alice_bits)))

  # Simulate the circuit
  simulator = Aer.get_backend('qasm_simulator')
  job = execute(qc, simulator, shots=1)
  result = job.result()
  bob_bits = list(result.get_counts().keys())[0]

  # Determine shared key and matching indices
  shared_key = []
  matching_indices = []
  for i, (a, b) in enumerate(zip(alice_bits, bob_bits)):
    if a == b:
      shared_key.append(a)
      matching_indices.append(i)

  return shared_key, matching_indices

# Example usage
alice_bits = [1, 0, 1, 1, 0]
shared_key, matching_indices = qkd_protocol(alice_bits)

print(f"Alice's bits: {alice_bits}")
print(f"Shared key: {shared_key}")
print(f"Matching indices: {matching_indices}")
