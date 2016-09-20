# Created by Andreas Oven Aalsaunet
# This calculator script makes use of Reverse Polish Notation to calculate values.
# Inputted numbers are pushed on a stack and a operators pops the appropriate numbers/operands from the stack and pushes
# the result on the stack. "P" prints the last number on the stack without popping it.

stack = []


def is_number(s):
    try:
        float(s)
        # print(s + " is a number")
        return True
    except ValueError:
        return False


def prompt():
    prompt_count = 1
    while True:
        char = input("[{0}]: ".format(prompt_count))
        prompt_count += 1

        if is_number(char):
            stack.append(char)

        elif char in "+*/" and len(stack) >= 2:
            x = stack.pop()
            y = stack.pop()
            stack.append(eval(y + char + x))

        elif "p" or "P" in char:
            print(stack[len(stack) - 1])


if __name__ == "__main__":
    print("Welcome to the Reverse Polish Notation Calculator!")
    prompt()
