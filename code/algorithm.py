# algorithm.py

def burrows_wheeler_transform(s):
    """
    Perform the Burrows-Wheeler Transform on the input string.
    """
    s += '$'  # Add special end-of-string marker
    rotations = [s[i:] + s[:i] for i in range(len(s))]  # Generate all cyclic rotations
    sorted_rotations = sorted(rotations)  # Sort rotations lexicographically
    return ''.join(row[-1] for row in sorted_rotations)  # Take last chars

def inverse_burrows_wheeler_transform(bwt):
    """
    Reverse the Burrows-Wheeler Transform.
    """
    n = len(bwt)
    table = [''] * n
    for _ in range(n):
        table = sorted([bwt[i] + table[i] for i in range(n)])  # Prepend column and sort
    for row in table:
        if row.endswith('$'):
            return row.rstrip('$')  # Remove end marker

# Demo run
if __name__ == "__main__":
    original = "banana"
    bwt_result = burrows_wheeler_transform(original)
    restored = inverse_burrows_wheeler_transform(bwt_result)

    print("Original: ", original)
    print("BWT:      ", bwt_result)
    print("Restored: ", restored)
