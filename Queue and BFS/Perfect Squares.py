# February 11th, 2024
def numSquares(self, n: int) -> int:
    psref = [x ** 2 for x in range(1, 101)]
    q = [n]
    depth = 0

    while len(q) > 0:

        next_depth = set()

        for x in range(0, len(q)):  # adds next depth of tree
            if q[x] in psref:
                return depth + 1
            else:
                for y in psref:
                    if y > q[x]:
                        break
                    else:
                        next_depth.add(q[x] - y)

        q.clear()
        q = list(next_depth)
        depth += 1