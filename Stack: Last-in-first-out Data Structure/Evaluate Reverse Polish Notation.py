# February 18th, 2024

def evalRPN(self, tokens: List[str]) -> int:
    numstack = []

    # fx for performing arithmetic
    def parse(a: int, b: int, op: str) -> int:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:
            return int(a / b)

    # end-parse-fx

    for i in range(0, len(tokens)):
        if tokens[i] in ["+", "-", "*", "/"]:
            b = numstack.pop(0)
            a = numstack.pop(0)
            op = tokens[i]

            numstack.insert(0, parse(a, b, op))

            continue
        else:
            numstack.insert(0, int(tokens[i]))

    return numstack[0]