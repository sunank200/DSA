def fib_sum(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib_sum(num -1) + fib_sum(num-2) + 1

# fib sum  Fn = Fn+2 -1
# golden ratio (a+b)/ b = a/b = phi

if __name__ == "__main__":
    print(fib_sum(4))