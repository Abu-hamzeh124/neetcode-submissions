class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #   an int for storing the first index and another for the second
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            sum1 = numbers[index1] + numbers[index2]
            if sum1 == target:
                return [index1 + 1, index2 + 1]
            if sum1 > target:
                index2 -= 1
            else:
                index1 += 1