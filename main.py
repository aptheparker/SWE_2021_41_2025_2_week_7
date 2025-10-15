from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []

if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(twoSum([3, 3], 6))          # Output: [0, 1]