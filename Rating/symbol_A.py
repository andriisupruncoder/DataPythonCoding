import heapq

def generate_huffman_codes(symbols, frequencies):
  """
  Generates Huffman codes for the given symbols and frequencies.

  Args:
    symbols: A list of symbols.
    frequencies: A list of frequencies for the corresponding symbols.

  Returns:
    A dictionary of Huffman codes, with the symbols as keys and the codes as values.
  """

  # Create a priority queue of nodes, with the frequencies as the keys.

  queue = [(-frequency, symbol) for symbol, frequency in frequencies.items()]
  heapq.heapify(queue)

  # Build the Huffman tree by repeatedly merging the two nodes with the lowest frequencies.

  while len(queue) > 1:
    # Pop the two nodes with the lowest frequencies.
    node1 = heapq.heappop(queue)
    node2 = heapq.heappop(queue)

    # Create a new node with the combined frequency.
    node = (node1[0] + node2[0], None, node1[1], node2[1])

    # Add the new node to the queue.
    heapq.heappush(queue, node)

  # The root of the Huffman tree is the code for all symbols.

  root = heapq.heappop(queue)[1]

  # Generate the Huffman codes by traversing the tree.

  codes = {}
  generate_codes(root, codes)
  return codes

def generate_codes(node, codes):
  """
  Recursively generates Huffman codes for the given node.

  Args:
    node: The current node in the Huffman tree.
    codes: A dictionary of Huffman codes, with the symbols as keys and the codes as values.
  """

  if node.symbol is not None:
    codes[node.symbol] = ""
  else:
    generate_codes(node.left, codes)
    generate_codes(node.right, codes)