"""
Implement iota

"""


def convert_to_string(num, base=10):
    if num // base == 0:
        return chr(num + ord("0"))
    # print(num, num//base, chr(num % base + ord('0')))
    return convert_to_string(num // base, base) + chr(num % base + ord("0"))


if __name__ == "__main__":

    # add check for negative if required
    num = 0
    if num >= 0:
        print(convert_to_string(num, 10))
    else:
        num = -1 * num
        ans = convert_to_string(num, 10)
        print(-1 * int(ans))
