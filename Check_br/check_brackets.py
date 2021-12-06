open_br = ["[", "{", "("]
close_br = ["]", "}", ")"]

# Function to check brackets
def check(myString):
    stack = []
    for i in myString:
        if i in open_br:
            stack.append(i)
        elif i in close_br:
            pos = close_br.index(i)
            if ((len(stack) > 0) and
                    (open_br[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unmatched"
    if len(stack) == 0:
        return "Matched"
    else:
        return "Unmatched"


