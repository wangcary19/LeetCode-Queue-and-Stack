# February 8th, 2024
def numSquares(self, n: int) -> int:
    psref = [x ** 2 for x in range(0, 101)]
    q = [n]
    depth = 0
    current_depth_limit = 1
    future_depth_limit = 0

    if n in psref:
        return 1
    else:
        while True:
            for x in range(0, current_depth_limit):
                # print(q)
                # print("q[x] is: " + str(q[x]))
                if q[x] == 0:
                    return depth
                else:
                    for i in range(1, 101):  # add to q all diffs of perfect squares less than q
                        if psref[i] > q[x]:
                            break
                        else:
                            q.append(q[x] - psref[i])
                            future_depth_limit += 1
            # end-for
            q = q[current_depth_limit:]
            current_depth_limit = future_depth_limit
            future_depth_limit = 0
            # print("new c_d_l is: " + str(current_depth_limit))
            depth += 1