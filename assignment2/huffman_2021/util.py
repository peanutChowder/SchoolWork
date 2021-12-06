import bitio
import huffman
import pickle

def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    treeNode = pickle.load(tree_stream)


    return treeNode

def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    if isinstance(tree, huffman.TreeLeaf):
      return tree.getValue()

    bit = bitreader.readbit()

    if bit == 0:
      return decode_byte(tree.getLeft(), bitreader)

    else:
      return decode_byte(tree.getRight(), bitreader)



def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    treeRoot = read_tree(compressed)

    bitreader = bitio.BitReader(compressed)
    bitwriter = bitio.BitWriter(uncompressed)
    EOF = False

    while not EOF:
      try:
        decoded_byte = decode_byte(treeRoot, bitreader)
        if decoded_byte:
          bitwriter.writebits(decoded_byte, 8)
        else:
          EOF = True

      except EOFError:
        EOF = True

    bitwriter.flush()

def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pickle.dump(tree, tree_stream)

def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''
    write_tree(tree, compressed)
    encoding_table = huffman.make_encoding_table(tree)
    bitreader = bitio.BitReader(uncompressed)
    bitwriter = bitio.BitWriter(compressed)

    EOF = False
    while not EOF:
      try:
        uncompressed_byte = bitreader.readbits(8)
        encoded_byte_tuple = encoding_table[uncompressed_byte]

      except EOFError:
        encoded_byte_tuple = encoding_table[None]
        EOF = True

      finally:
        for bit in encoded_byte_tuple:
          bitwriter.writebit(bit)
    bitwriter.flush()

if __name__ == "__main__":
  filename = "arrow.png"
  # with open(filename, 'rb') as compressed:
  #       with open(filename+'.decomp', 'wb') as uncompressed:
  #               decompress(compressed, uncompressed)

  with open(filename, 'rb') as uncompressed:
        freqs = huffman.make_freq_table(uncompressed)

        tree = huffman.make_tree(freqs)
        uncompressed.seek(0)
        with open(filename+'.huf', 'wb') as compressed:
                compress(tree, uncompressed, compressed)


      