import numpy as np

def compute_dot_product(arr1, arr2):
  if len(arr1) == len(arr2):
    dot_product = arr1.dot(arr2)
    return dot_product
  else:
    print("Can't compute the dot product between two different length arrays.")
