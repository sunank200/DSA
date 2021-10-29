"""
Given a list/array of names(String) sort them such that each name is followed
by a name which starts with the last character of the previous name.
# input
[
Luis
Hector
Selena
Emmanuel
Amish
]

# output:
[
Emmanuel
Luis
Selena
Amish
Hector
]



"""


def sort_by_order(names):
    firsts = {}
    lasts = {}

    result = []
    for i in names:
        lasts[i[-1]] = i

    for i in names:
        firsts[i[0].lower()] = i

    start = list(set(firsts.keys()) - set(lasts.keys()))[0]

    i = 0
    while i < len(names):
        if i == 0:
            result.append(firsts[start])
            last = firsts[start][-1]
            i = i + 1
            continue

        result.append(firsts[last])
        last = firsts[last][-1]
        i = i + 1

    return result


if __name__ == "__main__":
    names = ["Luis", "Hector", "Selena", "Emmanuel", "Amish"]
    print(sort_by_order(names))
