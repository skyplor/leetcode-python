from treenode import TreeNode, drawtree
from typing import List, Optional

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        '''
        we will use a hashmap to store the int as key and its corresponding node
        we will also have a root var. This root node will be updated if a parent doesnt exist as key
        '''
        nodes = {}
        children = set()
        for parent,child,isLeft in descriptions:
            if parent not in nodes:
                parentNode = TreeNode(parent)
                nodes[parent] = parentNode
                root = parentNode
            else:
                parentNode = nodes[parent]
            if child not in nodes:
                childNode = TreeNode(child)
                nodes[child] = childNode
            else:
                childNode = nodes[child]
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            children.add(child)
        for key in nodes.keys():
            if key not in children:
                return nodes[key]
        return None

sol = Solution()
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(f'output: {drawtree(sol.createBinaryTree(descriptions))}')