# March 5th, 2024

total = 0  # used to hash the depth value


def findTargetSumWays(self, nums: List[int], target: int) -> int:
    total = sum(nums)
    runtime_memory = [[None] * 2000 for i in
                      range(1000)]  # query via [depth][self.total + target]; hash stores number of repeated subroutines
    return self.remember_subroutines(nums, 0, target, 0, runtime_memory)


def remember_subroutines(self, nums: List[int], cumulative: int, target: int, depth: int, memory: List[[int]]) -> int:
    if depth == len(nums):  # exit condition
        if cumulative == target:  # valid leaf has been reached, increment subroutine count
            return 1
        else:  # invalid leaf, do not increment master count
            return 0
    else:
        if memory[depth][self.total + cumulative] != None:
            return memory[depth][self.total + cumulative]

        # get the number of valid leaves under the current node
        leaves_to_left = self.remember_subroutines(nums, cumulative - nums[depth], target, depth + 1, memory)
        leaves_to_right = self.remember_subroutines(nums, cumulative + nums[depth], target, depth + 1, memory)
        memory[depth][self.total + cumulative] = leaves_to_left + leaves_to_right
        return memory[depth][self.total + cumulative]