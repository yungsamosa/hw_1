import sys
import random
#this is a comment I fixed after messing with git lmao
def random_lines(filename):
    output = ""
    with open(filename, encoding="utf-8") as f:
        for x in f:
            if random.random() < 0.01:
                output += x
    return output

filename = sys.argv[1]
print(random_lines(filename))
