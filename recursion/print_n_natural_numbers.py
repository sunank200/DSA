# Print numbers from 1 to N
def print_num_asc(n):
    if n > 0:
        print_num_asc(n - 1)
        print(n)


def print_num_desc(n):
    if n == 1:
        return 1
    print(n)
    print_num_desc(n - 1)


if __name__ == "__main__":
    print(print_num_asc(12))
    print(print_num_desc(15))
