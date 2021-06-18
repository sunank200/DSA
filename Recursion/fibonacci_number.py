def fib_num(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib_num(num - 1) + fib_num(num - 2)


if __name__ == "__main__":
    print(fib_num(45))
