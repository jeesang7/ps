# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        # print(left_depth, right_depth)
        return max(left_depth, right_depth) + 1

    def preorder_traverse(self):
        if self.left is None and self.right is None:
            print(self.val)
            return
        print(self.val)
        if self.left is not None:
            self.left.preorder_traverse()
            print(self.val)
        if self.right is not None:
            self.right.preorder_traverse()
            print(self.val)


def make_tree_by_elements(elements):
    def _insert_left_first(tmp_tree, data):
        que = []
        que.append(tmp_tree)
        que_val = []
        que_val.append(tmp_tree.val)

        while len(que):
            tmp_tree = que[0]
            que.pop(0)
            que_val.pop(0)
            if tmp_tree.left is None:
                if data is not None:
                    tmp_tree.left = TreeNode(data)
                else:
                    tmp_tree.left = TreeNode(0)
                break
            else:
                que.append(tmp_tree.left)
                que_val.append(tmp_tree.val)

            if tmp_tree.right is None:
                if data is not None:
                    tmp_tree.right = TreeNode(data)
                else:
                    tmp_tree.right = TreeNode(0)
                break
            else:
                que.append(tmp_tree.right)
                que_val.append(tmp_tree.val)
        print(que_val)

    tree = TreeNode(elements[0])
    for element in elements[1:]:
        _insert_left_first(tree, element)

    return tree


if __name__ == "__main__":
    tree = make_tree_by_elements([2, 10, 3, 7, 22, 102])
    print("depth:", tree.depth())
    tree.preorder_traverse()
