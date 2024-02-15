temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
# temperatures = [55,38,53,81,61,93,97,32,43,78]

if len(temperatures) == 1:
    temperatures[0] = 0
    # return temperatures
else:
    curr = 0
    stack = []  # stores indices
    # TODO add correct exit condition
    while curr < len(temperatures) - 1:

        stack.append(curr)
        curr += 1

        # reached end of set without finding a temp greater than top of stack, then empty stack and emplace 0
        if temperatures[curr] <= temperatures[stack[-1]] and curr == len(temperatures) - 1:
            print("Exit cond")
            """
            while len(stack) > 0:
                temperatures[stack.pop(-1)] = 0
                """
            break

            # return temperatures

        # push current index to stack if value at current is less than value at prev (i.e. top of stack)
        elif temperatures[curr] <= temperatures[stack[-1]]:
            print("Cond A, curr is: " + str(curr) + "; top of stack is: " + str(stack[-1]) + ".  Stack is: ", end="")
            print(stack, end="")
            print("  Temperatures is: ", end="")
            print(temperatures)

            continue

        # found a value greater than top of stack, walk back on stack while emplacing difference in indices until condition no longer holds, then continue forward
        else:
            print("Cond B, curr is: " + str(curr) + "; top of stack is: " + str(stack[-1]) + ".  Stack is: ", end="")
            print(stack, end="")
            print("  Temperatures is: ", end="")


            while len(stack) > 0:
                if temperatures[curr] > temperatures[stack[-1]]:
                    change_idx = stack.pop(-1)
                    temperatures[change_idx] = curr - change_idx
                else:
                    break

            print(temperatures)
    while len(stack) > 0:
        temperatures[stack.pop(-1)] = 0
    temperatures[-1] = 0

    print(temperatures)
    # return temperatures
