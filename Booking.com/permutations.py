def getPermutations(array):
    permutations = []
    permutation_helper(0, array, permutations)
    return permutations


def permutation_helper(start, array, permutations):
    if start == len(array) - 1:
        permutations.append(array[:])
    else:
        for i in range(start, len(array)):
            swap(array, i, start)
            permutation_helper(start + 1, array, permutations)
            swap(array, i, start)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    print(getPermutations([1, 2, 3, 4, 5, 6, 7, 7]))
