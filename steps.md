# Burrows-Wheeler Transform – Algorithm Steps

## Pseudocode for BWT


1. Append a special end-of-string symbol '$' to input_string.
2. Generate all cyclic rotations of the input_string.
3. Sort the rotations lexicographically.
4. Construct the BWT string by taking the last character of each rotation.
5. Return the BWT string.
