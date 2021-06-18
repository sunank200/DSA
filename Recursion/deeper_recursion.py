def sum_recursion(calnum, n):
    calnum = calnum + 1
    print("Enter [{}]: sum_recursion(n={})\n".format(calnum, n))
    total = 0
    if n == 1:
        total = total + 1
        print("--------- End conditon met! total= {} \n".format(total))
    else:
        newnum = n - 1
        print(" before [{}]: sum_recursion[n={}] \n".format(calnum, newnum))
        total = n + sum_recursion(calnum, newnum)
        print("after  [{}]   total: {} \n".format(calnum, total))

    print("return: n={}, total = {} \n".format(n, total))
    return total


if __name__ == "__main__":
    startnum = 3
    print(
        "Sum of first {} integers using recurssion is {}".format(
            startnum, sum_recursion(0, startnum)
        )
    )
