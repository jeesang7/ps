# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        print(left_depth, right_depth)
        return max(left_depth, right_depth) + 1


def test_depth(tree):
    # root = TreeNode(10, TreeNode(20), TreeNode(4))
    print(tree.depth())


def insert(temp, data):
    que = []
    que.append(temp)
    while len(que):
        temp = que[0]
        que.pop(0)
        if temp.left is None:
            if data is not None:
                temp.left = TreeNode(data)
            else:
                temp.left = TreeNode(0)
            break
        else:
            que.append(temp.left)

        if temp.right is None:
            if data is not None:
                temp.right = TreeNode(data)
            else:
                temp.right = TreeNode(0)
            break
        else:
            que.append(temp.right)
    print(que)


def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    return Tree


if __name__ == "__main__":
    # test_depth()
    tree = make_tree([2, 10, 3, 7, 22, 102])
    test_depth(tree)
