"""
You decide to create a substitution cipher. The cipher alphabet is based on a
 key shared amongst those of your friends who don't mind spoilers.

Suppose the key is:
"The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy
dwarf!".

We use only the unique letters in this key to set the order of the characters
in the substitution table.

T H E Q U I C K O N Y X G B L R A S W D J M P V Z F

(spaces added for readability)

We then align it with the regular alphabet:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T H E Q U I C K O N Y X G B L R A S W D J M P V Z F

Which gives us the substitution mapping: A becomes T, B becomes H, C becomes
E, etc.

Write a function that takes a key and a string and encrypts the string with
the key.

Example:
key = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the
1st lazy dwarf!"
encrypt("It was all a dream.", key) -> "Od ptw txx t qsutg."
encrypt("Would you kindly?", key) -> "Pljxq zlj yobqxz?"

Complexity analysis:

m: The length of the message
k: The length of the key


"""
key = (
    "The quick onyx goblin, Grabbing his sword ==}-------- jumps over "
    "the 1st lazy dwarf!"
)
message = "It was all a dream."
message2 = "Would you kindly?"

ch = "A"


# print(ch.isalpha())
# print(ch.lower())
# print(ord('b') % 97)
def encrypt_based_on_key(key, message):
    order_key = [None] * 26

    seen_dict = {}
    current_index = 0
    for ch in key:
        if ch.isalpha() and ch.lower() not in seen_dict:
            order_key[current_index] = ch.lower()
            current_index += 1
            seen_dict[ch.lower()] = True

    result = ""
    for ch in message:
        letter_index = ord(ch.lower()) % 97
        if ch.isalpha() and ch.isupper():
            result += str(order_key[letter_index]).upper()
        elif ch.isalpha() and ch.islower():
            result += order_key[letter_index]
        else:
            result += ch

    return result


if __name__ == "__main__":
    print(encrypt_based_on_key(key, message2))

# message1 = "One does not simply walk into Mordor"
# rows1, cols1 = 6, 6

# message2 = "1.21 gigawatts!"
# rows2, cols2 = 5, 3
# rows3, cols3 = 3, 5


# def encrypt(message, rows, cols):
#     if len(message) > (rows*cols):
#         return None

#     encryption_matrix = [[None for _ in range(cols)]  for _ in range(rows)]

#     i, j = 0, 0

#     current_index = 0
#     while current_index < len(message):
#         ch = message[current_index]

#         if j <= cols-1:
#             encryption_matrix[i][j] = ch
#         else:
#             j = 0
#             i += 1
#             encryption_matrix[i][j] = ch


#         j += 1
#         current_index += 1

#     result = ""

#     for i in range(cols):
#         for j in range(rows):
#             result += encryption_matrix[j][i]

#     return result


# if __name__ == "__main__":
# #     print(encrypt(message2, rows3, cols3))
# """
# n = length of message
# Time Complexity : O(n)
# Space Complexity: O(n)
# """
