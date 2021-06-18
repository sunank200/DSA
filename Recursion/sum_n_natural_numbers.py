def sum_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_num(n - 1)


if __name__ == "__main__":
    print(sum_num(17))
