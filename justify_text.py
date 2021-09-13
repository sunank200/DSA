"""
We are building a word processor and we would like to implement a "reflow"
functionality that also applies full justification to the text.
Given an array containing lines of text and a new maximum width, re-flow the
text to fit the new width. Each line should have the exact specified width.
If any line is too short, insert '-' (as stand-ins for spaces) between words
as equally as possible until it fits.
Note: we are using '-' instead of spaces between words to make testing and
visual verification of the results easier.


lines = [ "The day began as still asJu the",
          "night abruptly lighted with",
          "brilliant flame" ]

reflowAndJustify(lines, 24) "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces

reflowAndJustify(lines, 25) "reflow lines and justify to length 25" =>

        [ "The-day-began-as-still-as"
          "the-----night----abruptly"
          "lighted---with--brilliant"
          "flame" ]

reflowAndJustify(lines, 26) "reflow lines and justify to length 26" =>

        [ "The--day-began-as-still-as",
          "the-night-abruptly-lighted",
          "with----brilliant----flame" ]

reflowAndJustify(lines, 40) "reflow lines and justify to length 40" =>

        [ "The--day--began--as--still--as-the-night",
          "abruptly--lighted--with--brilliant-flame" ]

reflowAndJustify(lines, 14) "reflow lines and justify to length 14" =>

        ['The--day-began',
         'as---still--as',
         'the------night',
         'abruptly',
         'lighted---with',
         'brilliant',
         'flame']

n = number of words OR total characters

"""

lines = [
    "The day began as still as the",
    "night abruptly lighted with",
    "brilliant flame",
]
test_reflow_width1 = 24
test_reflow_width2 = 25
test_reflow_width3 = 26
test_reflow_width4 = 40
test_reflow_width5 = 14


def justify_text(lines, maxWidth):
    """
    1. Get all the words which fit in a line.
    2. check if line has one word or more than one.
     nspaces = len(current_line) -1 if len(current_line) - 1 else 1

            for i in range(maxWidth - current_line_width):
                current_line[i % nspaces] += " "
    3. reset counters for next line
    4. create last line
    """
    words = []
    for line in lines:
        words.extend(line.split())

    current_line = []
    current_line_width = 0

    lines = []

    for word in words:
        # here length of next word + length if previous words + len of spaces (repersentted by len(current_line))
        if len(word) + current_line_width + len(current_line) > maxWidth:
            # check one word or multiple word. Need to add justified line
            nspaces = len(current_line) - 1 if len(current_line) - 1 else 1

            for i in range(maxWidth - current_line_width):
                current_line[i % nspaces] += " "

            lines.append("".join(current_line))
            current_line = []
            current_line_width = 0

        current_line.append(word)
        current_line_width += len(word)

    last_line = " ".join(current_line)
    last_line = last_line.strip()
    last_line = last_line + " " * (maxWidth - len(last_line))
    lines.append(last_line)
    return lines


if __name__ == "__main__":
    test_arr = [24, 25, 26, 40, 14]
    for i in test_arr:
        print(justify_text(lines, i))
