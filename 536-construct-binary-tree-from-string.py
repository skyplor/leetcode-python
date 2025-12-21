from typing import Optional
from treenode import TreeNode, drawtree


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        '''
        we can use stack for this. while going through the string char by char, we will have a i pointer
        if we encounter a ')', pop from stack and proceed
        if we encounter a '(', proceed
        otherwise, we will parse the digits and '-'
            We can expect to have multiple digits, so we have a start pointer, then we need to use a while loop to loop through the next character to see if it's a digit. if yes, continue until we don't have a digit
            After that, we create a node with the value based on the start pointer to i.
            We then check if top most node on the stack has a left child node. if no, assign this new node as the left child node. Otherwise, assign the next value as the right child node.
            Then push this node onto the stack

        at the end, we just get the first node from the stack since that will be the root node.
        We also need to account for case if s is empty, then we will return a None
        '''

        stack = []
        is_negated = False
        i = 0

        while i < len(s):
            c = s[i]
            if c == ')':
                stack.pop()
                i += 1
            elif c == '(':
                i += 1
            else:
                if c == '-':
                    is_negated = True
                    i += 1
                else:
                    start = i
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    val = int(s[start:i])
                    if is_negated:
                        val = -val
                    is_negated = False

                    node = TreeNode(val)
                    if stack:
                        parent = stack[-1]
                        if not parent.left:
                            parent.left = node
                        elif not parent.right:
                            parent.right = node

                    stack.append(node)

        return stack[0] if stack else None


sol = Solution()
# s = "-4(2(3)(1))(6(5)(7))"
s = ""
output = sol.str2tree(s)
drawtree(output)
