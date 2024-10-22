# --- Conceptual Differential Privacy using OpenDP ---

import opendp.smartnoise.core as sn

def differentially_private_sum(data, epsilon):
  """
  Calculates a differentially private sum of the data.

  Args:
    data: The data to be summed.
    epsilon: The privacy parameter.

  Returns:
    The differentially private sum.
  """
  with sn.Analysis() as analysis:
    data_vector = sn.Dataset(value=data, num_columns=1)
    sum_result = sn.dp_sum(data_vector, privacy_usage={'epsilon': epsilon})

  analysis.release()
  return sum_result.value

# Example usage
data = [1, 2, 3, 4, 5]
epsilon = 1.0

dp_sum = differentially_private_sum(data, epsilon)

print(f"Original sum: {sum(data)}")
print(f"Differentially private sum: {dp_sum}")
