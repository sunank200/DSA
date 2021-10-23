"""
There's a very simple compression algorithm that takes subsequent characters
 and just emits how often they were seen.

Example:
abababaabbbaaaaa

output = a1b1a1b1a1b1a2b3a5
"""


def compress(chars) -> int:
    """
    read pointer and write pointer
    """
    prev = None
    cons = 1
    compressed = ""
    for i in chars:
        if prev:
            if prev == i:
                cons += 1
            else:
                compressed += prev + str(cons)
                cons = 1
        prev = i
    compressed += prev + str(cons)

    return compressed


if __name__ == "__main__":
    print(compress("abababaabbbaaaaa"))
