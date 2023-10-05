start = 42
end = -12
num_elements = 10

# Calculate the difference between consecutive numbers
diff = (end - start) // (num_elements - 1)

# Generate the sequence
sequence = [start + i * diff for i in range(num_elements)]

print(sequence)
