# Created by Andreas Oven Aalsaunet
# This calculator script makes use of Reverse Polish Notation to calculate values.
# Inputted numbers are pushed on a stack and a operators pops the appropriate numbers/operands from the stack and pushes
# the result on the stack. "P" prints the last number on the stack without popping it.

import math
stack = []


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def prompt():
    prompt_count = 1
    while True:
        input_string = input("[{0}]: ".format(prompt_count))
        prompt_count += 1

        char_list = input_string.split()
        for char in char_list:
            if is_number(char):
                stack.append(float(char))

            elif char in "+*/" and len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(eval(str(y) + char + str(x)))

            elif char in "Vv" and len(stack) >= 1:
                # Replaces the last number of the stack with its square root
                stack.append(math.sqrt(stack.pop()))

            elif (char == "sin" or char == "cos") and len(stack) >= 1:
                x = stack.pop()
                stack.append(eval("math." + char + "(x)"))

            elif char in "Pp" and len(stack) >= 1:
                print("--> " + str(stack[len(stack) - 1]))

            elif char == "reset":
                stack.clear()

            elif char == "stack":
                print("--> " + str(stack))

            else:
                print("--> Not a valid command (right now)")


if __name__ == "__main__":
    print("Welcome to the Reverse Polish Notation Calculator!")
    prompt()
