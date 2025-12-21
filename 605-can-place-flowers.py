from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        Loop through the flowerbed, each time we check if we can place the flower or not by checking if left and right is 0
        return True if n == 0
        return False at the end
        '''
        def in_range(index: int, start: int, end: int):
            if index < start or index > end:
                return False

            return True

        start = 0
        flowerbed_length = len(flowerbed)
        end = flowerbed_length - 1
        temp_flowerbed = [0]*flowerbed_length
        for i, flower_value in enumerate(flowerbed):
            temp_flowerbed[i] = flower_value

        for i in range(flowerbed_length):
            if temp_flowerbed[i] == 1:
                continue
            left_i = i - 1
            right_i = i + 1
            has_left_flower, has_right_flower = 0, 0
            if in_range(left_i, start, end):
                has_left_flower = temp_flowerbed[left_i]
            if in_range(right_i, start, end):
                has_right_flower = temp_flowerbed[right_i]

            if not has_left_flower and not has_right_flower:
                if n == 1:
                    return True
                temp_flowerbed[i] = 1
                n -= 1

        return False


sol = Solution()
flowerbed = [1, 0, 0, 0, 1]
n = 1
output = sol.canPlaceFlowers(flowerbed, n)
print(f'output: {output}')
