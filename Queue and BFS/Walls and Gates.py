# February 4th, 2024
def wallsAndGates(self, rooms: List[List[int]]) -> None:
    i = 0
    j = 0
    height = len(rooms)
    width = len(rooms[0])
    gate = 0
    queue = []
    INF = 2147483647
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(0, height):  # find coords of gates
        for j in range(0, width):
            if rooms[i][j] == gate:
                queue.append((i, j))
            else:
                continue

    while len(queue) > 0:  # BFS from gates
        gi, gj = queue.pop(0)  # read last node coords
        for x in dirs:
            si = gi + x[0]
            sj = gj + x[1]
            if si < 0 or si >= height or sj < 0 or sj >= width or rooms[si][sj] != INF:
                continue
            else:
                rooms[si][sj] = rooms[gi][gj] + 1
                queue.append((si, sj))