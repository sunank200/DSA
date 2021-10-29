"""
 System configuration/ config files

 connection string = {variables}

 Key value


 Input String = "I am working with {workers} {day}"
 Dictionary = {"workers": "farmers",
 "day":2}

 Return = "I am working with farmers"

 Input str2 = "I am working with {{country}workers}}"
 Dictionary = {"country" : "India", "Indiaworkers" :"farmers"}
 Result = "I am working with farmers"

"""
# a = list("I am working with {{Indiaworkers}}")
# a.pop(0)
# a.pop(0)
# print(a)
# a.insert(0,"A")
# a.insert(1, "B")
# print(a)


def replace_word(word, end, start, input_str, config):

    word = word.replace("{", "")
    word = word.replace("}", "")
    print(word)
    replacement_word = config.get(word)
    input_str = list(input_str)
    for _ in range(start, end):
        input_str.pop(start)

    i = start
    for ch in replacement_word:
        input_str.insert(i, ch)
        i += 1
    return "".join(input_str)


def replace_config(input_str, config):
    if len(input_str) == 0:
        return input_str

    start = 0
    end = 0
    while start < len(input_str):
        if input_str[start] == "{":
            stack = []
            temp = ""
            while input_str[start] != "}" and start < len(input_str):
                if input_str[start] == "{":
                    stack.append(input_str[start])
                else:
                    temp += input_str[start]
                start += 1
            # temp += input_str[start + 1]
            stack.append(temp)
            print(stack)
            input_str = replace_word(stack.pop(-1), start, end, input_str, config)
            print(input_str)
            print(stack)
            start = end - 1
        else:
            start += 1
            end += 1

    return input_str


if __name__ == "__main__":
    key_val = {"country": "India", "Indiaworkers": "farmers"}
    print(replace_config("In am working with {{country}workers}", key_val))
