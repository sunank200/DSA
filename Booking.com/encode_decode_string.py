"""

"""

"""
Approach 1: is to use chr(257) to join the string and split by chr(257)
Approach 2: 
Encoding Algorithm
    Iterate over the array of chunks, i.e. strings.

    For each chunk compute its length, and convert that length into 4-bytes string.

    Append to encoded string :

    4-bytes string with information about chunk size in bytes.

    Chunk itself.

    Return encoded string.
    
Decoding Algorithm
    Iterate over the encoded string with a pointer i initiated as 0. While i < n:

    Read 4 bytes s[i: i + 4]. It's chunk size in bytes. Convert this 4-bytes string to integer length.

    Move the pointer by 4 bytes i += 4.

    Append to the decoded array string s[i: i + length].

    Move the pointer by length bytes i += length.

    Return decoded array of strings.
"""
#     def len_to_str(self, x):
#         x = len(x)

#         bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
#         bytes.reverse()
#         bytes_str = ''.join(bytes)
#         return bytes_str

#     def str_to_int(self, bytes_str):
#         """
#         Decodes bytes string to integer.
#         """
#         result = 0
#         for ch in bytes_str:
#             result = result * 256 + ord(ch)
#         return result


def encode(strs: [str]) -> str:
    """Encodes a list of strings to a single string."""
    if len(strs) == 0:
        return chr(258)

    return chr(257).join(strs)
    # return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)


def decode(s: str) -> [str]:
    """Decodes a single string to a list of strings."""
    if s == chr(258):
        return []

    return s.split(chr(257))
    # i, n = 0, len(s)
    # output = []
    # while i < n:
    #     length = self.str_to_int(s[i: i + 4])
    #     i += 4
    #     output.append(s[i: i + length])
    #     i += length
    # return output


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
