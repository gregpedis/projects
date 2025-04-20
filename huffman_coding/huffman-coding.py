from queue import PriorityQueue
from sys import argv


# This class represents a node necessary for the tree structure
# of the Huffman coding lossless compression algorithm.
class HuffmanNode:
    def __init__(self, left, right, symbol, weight):
        self._left = left
        self._right = right
        self._symbol = symbol
        self._weight = weight

    @property
    def symbol(self):
        return self._symbol

    @property
    def right(self):
        return self._right

    @property
    def left(self):
        return self._left

    @property
    def weight(self):
        return self._weight

    # Python's priority queue compares both the priority and the item,
    # so an operator overload for greater-than is needed, since HuffmanNode is not a primitive type.
    # The result of the comparison is not relevant, only the existence of the operator is.
    def __gt__(self, other):
        return self.symbol > other.symbol


# This class represents all the functionality necessary to encode a value
# via the Huffman encoding compression method.
class HuffmanEncoder:

    def __init__(self, text):
        self.text = text

    # This method creates and returns a dictionary of symbol-frequency key-value pairs.
    def create_frequency_table(self):
        self.frequencies = {}
        for character in self.text:
            if not character in self.frequencies:
                self.frequencies[character] = 1
            else:
                self.frequencies[character] = self.frequencies[character] + 1
        return self.frequencies

    # This method creates a priority queue and restructures it to a Huffman Tree.
    def create_encoding_tree(self, frequency_table):
        self.priority_queue = PriorityQueue()
        # Inserts all the symbols in the priority queue based on their frequency.
        for symbol, frequency in frequency_table.items():
            leaf_node = HuffmanNode(None, None, symbol, frequency)
            item = (frequency, leaf_node)
            self.priority_queue.put(item)
        # Restructures the priority queue in order to contain only one, tree-structured node.
        while len(self.priority_queue.queue) > 1:
            _, left_node = self.priority_queue.get()
            _, right_node = self.priority_queue.get()
            combined_weight = left_node.weight + right_node.weight
            internal_node = HuffmanNode(
                left_node, right_node, left_node.symbol + right_node.symbol, combined_weight)
            self.priority_queue.put((combined_weight, internal_node))
        # Returns the Huffman Tree Root.
        return self.priority_queue.get()[1]

    # This method recursively creates a Huffman Encoding table.
    def create_encoding_table(self, huffman_node, encoding_table, encoding_value):
        # If a leaf node is not reached, add a suffix bit and pass the method to children.
        if huffman_node.left != None:
            # Left nodes get 0 as bit
            encoding_value_left = encoding_value + "0"
            self.create_encoding_table(
                huffman_node.left, encoding_table, encoding_value_left)
            # Right nodes get 1 as bit
            encoding_value_right = encoding_value + "1"
            self.create_encoding_table(
                huffman_node.right, encoding_table, encoding_value_right)
        else:
            # Leaf node is reached, add the symbol-encoding value pair to the table.
            encoding_table[huffman_node.symbol] = encoding_value


# This methods prints a list in the form of (character, frequency, Huffman code).
def print_frequencies_codes(frequency_table, encoding_table):
    print("Char     Freq        Code")
    print("-------------------------")
    # Use the __getitem__ method as the key function, in order to sort them based on frequency.
    # Enable the reverse to set the sorting in descending order.
    sorted_chars = sorted(
        frequency_table, key=frequency_table.__getitem__, reverse=True)
    # Prints a line for each character.
    for symbol in sorted_chars:
        frequency = frequency_table[symbol]
        encoding_value = encoding_table[symbol]
        print(f"{symbol}        {frequency}           {encoding_value}")
    print("\n")


# Python's script entry point.
if __name__ == '__main__':
    # Checks if the script is executed with no input supplied.
    if len(argv) < 2:
        print("A string input was not provided.")
    else:
        # Joining the input starting from 1, 
        # since the first argument is the script's name.
#        f = open("input.txt", "rt")
#        text_input = " ".join(f.readlines()).replace("\n", "")

        text_input = " ".join(argv[1:])
        print("\nStarting Huffman coding for input:")
        print(f"{text_input}\n")

        encoder = HuffmanEncoder(text_input)
        frequency_table = encoder.create_frequency_table()
        encoding_tree = encoder.create_encoding_tree(frequency_table)
        encoding_table = dict()
        encoder.create_encoding_table(encoding_tree, encoding_table, "")

        print_frequencies_codes(frequency_table, encoding_table)
        # Encode each character in given input via the encoding table.
        binary_output = ""
        for ch in text_input:
            binary_output += encoding_table[ch] + " "
        # Finally, print the Huffman-encoded bit output.
        print("Binary Output generated by Huffman coding:")
        print(binary_output)
