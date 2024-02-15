# February 15th, 2024
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    if len(temperatures) == 1:
        temperatures[0] = 0
        return temperatures
    else:

        curr = 0
        stack = []  # stores indices

        while curr < len(temperatures) - 1:

            stack.append(curr)
            curr += 1

            # exit condition
            if temperatures[curr] <= temperatures[stack[-1]] and curr == len(temperatures) - 1:
                break
            # end-if

            # push current to stack if value < value at stack top
            elif temperatures[curr] <= temperatures[stack[-1]]:
                continue
            # end-elif

            else:  # found value > stack top, backwards emplace diffs until value < stack top
                while len(stack) > 0:
                    if temperatures[curr] > temperatures[stack[-1]]:
                        change_idx = stack.pop(-1)
                        temperatures[change_idx] = curr - change_idx
                    else:
                        break
                # end-while
            # end-else
        # end-while

    while len(stack) > 0:
        temperatures[stack.pop(-1)] = 0
    temperatures[-1] = 0

    # end-else
    return temperatures
# end-fx