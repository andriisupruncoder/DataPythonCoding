import huffman

def generate_huffman_code(symbols, frequencies):
  # Create a Huffman tree.
  tree = huffman.HuffmanTree(symbols, frequencies)

  # Generate a Huffman code for each symbol.
  codes = tree.generate_codes()

  # Print the Huffman code.
  for symbol, code in codes.items():
    print("{}: {}".format(symbol, code))

# Generate a Huffman code for 8 symbols.
symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
frequencies = [0.25, 0.25, 0.25, 0.125, 0.0625, 0.0625, 0.0625, 0.0625]

generate_huffman_code(symbols, frequencies)