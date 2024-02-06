# February 5th, 2024
def numIslands(self, grid: List[List[str]]) -> int:
    h = len(grid)
    w = len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    islands = 0

    for i in range(0, h):
        for j in range(0, w):
            if grid[i][j] == "0" or grid[i][j] == "-1":  # not land or already reached
                continue
            else:  # BFS
                q = [(i, j)]

                while len(q) > 0:
                    base = q.pop()
                    oi = base[0]
                    oj = base[1]

                    grid[oi][oj] = "-1"

                    for x in dirs:
                        si = oi + x[0]
                        sj = oj + x[1]
                        if si < 0 or si >= h or sj < 0 or sj >= w or grid[si][sj] == "0" or grid[si][sj] == "-1":
                            continue
                        else:
                            q.append((si, sj))
                    # end-for
                # end-while
                islands += 1
                # end-else
            # end-for-j
        # end-for-i

    return islands