# Complexity Analysis – Burrows-Wheeler Transform

## Time Complexity

### Burrows-Wheeler Transform:
- Generating rotations: O(n)
- Sorting rotations: O(n log n)
- Constructing result: O(n)

**Overall Time Complexity**: O(n log n)

### Inverse BWT (Naive):
- n iterations of sorting: O(n × n log n)

**Overall Time Complexity**: O(n² log n)

## Space Complexity

- For BWT: O(n²) for storing all cyclic rotations
- For inverse BWT: O(n²) for reconstructing rows

**Note**: Optimized implementations using suffix arrays and LF-mapping can reduce time and space complexity to O(n).
