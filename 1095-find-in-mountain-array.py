class MountainArray:
    def __init__(self, arr: list[int]) -> None:
        self.counter = 0
        self.arr = arr

    def get(self, index: int) -> int:
        self.counter += 1
        if self.counter > 100:
            raise Exception
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountainArr: MountainArray) -> int:
        arr_length = mountainArr.length()

        def find_peak() -> int:
            left, right = 0, arr_length - 1
            while left < right:
                mid = left + (right - left) // 2
                mid_value = mountainArr.get(mid)
                next_value = mountainArr.get(mid + 1)
                if mid_value > next_value:
                    right = mid
                else:
                    left = mid + 1

            return left

        def binary_search(left: int, right: int, search_ascending: bool) -> int:

            while left < right:
                mid = left + (right - left) // 2
                mid_value = mountainArr.get(mid)

                if mid_value == target:
                    return mid
                elif target < mid_value:
                    if search_ascending:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    if search_ascending:
                        left = mid + 1
                    else:
                        right = mid

            return -1

        peak_index = find_peak()
        res = binary_search(0, peak_index, True)
        if res == -1:
            res = binary_search(peak_index, arr_length, False)

        return res


sol = Solution()
target = 3
arr = [1, 2, 3, 4, 5, 3, 1]
mountainArray = MountainArray(arr)
output = sol.findInMountainArray(target, mountainArray)
print(f'arr: {arr}, target: {target}, output: {output}')

target = 2
arr = [1, 5, 2]
mountainArray = MountainArray(arr)
output = sol.findInMountainArray(target, mountainArray)
print(f'arr: {arr}, target: {target}, output: {output}')

target = 3
arr = [3, 5, 3, 2, 0]
mountainArray = MountainArray(arr)
output = sol.findInMountainArray(target, mountainArray)
print(f'arr: {arr}, target: {target}, output: {output}')

target = 5
arr = [1, 2, 3, 5, 3]
mountainArray = MountainArray(arr)
output = sol.findInMountainArray(target, mountainArray)
print(f'arr: {arr}, target: {target}, output: {output}')
