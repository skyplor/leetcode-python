from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        '''
        We can use this advance data structure Segment Tree
        The idea is to get the max value between 2 segments.
        If the max value allows us to place the fruit, then we can proceed down the tree by first checking the left segment's max value.
            If it can be placed, then we move further down the tree. Otherwise, we move to the right
            If it cannot be placed, then we just increment a counter (which we will return at the end)
        We continue moving down the segment tree under we hit the leaf node.
        Once we can place the fruit, we update the current node's max value to `-1` and return True to parent
        If True is returned, that means the max of this parent node will need to be updated.
        The parent node will then get the max value of the 2 child segments and update itself, and continue to return the same result back to its parent until we hit the root node

        To build a segment tree, we will use a list to represent it. For the size, the usual convention is to just 4*n to ensure enough space
        We will do it recursively, each time we cut the baskets array by half and build the left and right
            - left subtree will have the index (2*i)
            - right subtree will have the index (2*i + 1)

                   1
                /     \\
               2        3
             /  \\    /  \\
            4    5   6     7 
        '''

        def build_segment_tree(left: int, right: int, index: int):
            if left == right:
                segment_tree[index] = baskets[left]
                return

            mid = left + (right - left) // 2
            left_child_index = 2*index
            right_child_index = 2*index + 1
            build_segment_tree(left, mid, left_child_index)
            build_segment_tree(mid+1, right, right_child_index)
            segment_tree[index] = max(
                segment_tree[left_child_index], segment_tree[right_child_index])

        def place_fruit(fruit: int, left: int, right: int, index: int) -> bool:
            if fruit > segment_tree[index]:
                return False

            # leaf node
            if left == right:
                segment_tree[index] = -1
                return True

            # middle node
            mid = left + (right - left) // 2
            left_child_index = 2 * index
            right_child_index = 2 * index + 1

            res = False
            if fruit <= segment_tree[left_child_index]:
                res = place_fruit(fruit, left, mid, left_child_index)
            else:
                res = place_fruit(fruit, mid+1, right, right_child_index)

            segment_tree[index] = max(
                segment_tree[left_child_index], segment_tree[right_child_index])
            return res

        n = len(fruits)
        # usual convention is to just 4 times the array size
        segment_tree_size = 4 * n
        segment_tree = [0] * segment_tree_size
        build_segment_tree(0, n-1, 1)
        res = 0
        for fruit in fruits:
            if not place_fruit(fruit, 0, n-1, 1):
                res += 1

        return res


sol = Solution()
fruits = [4, 2, 5]
baskets = [3, 5, 4]
output = sol.numOfUnplacedFruits(fruits, baskets)
print(f'output: {output}')
