# February 11th, 2024
def isValid(self, s: str) -> bool:
    left = ['(', '{', '[']
    right = [')', '}', ']']
    matchkey = {'(': ')', '{': '}', '[': ']'}
    stack = []

    if len(s) % 2 == 1:
        return False
    else:
        for x in s:
            if x in left:
                stack.insert(0, x)
            elif x in right:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop(0)
                    if matchkey[top] != x:
                        return False
            else:
                continue

        if len(stack) > 0:
            return False
        else:
            return True