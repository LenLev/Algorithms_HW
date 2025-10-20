class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    def verify(node):
        if not node:
            return 0, True

        l_height, l_bal = verify(node.left)
        r_height, r_bal = verify(node.right)

        node_balanced = l_bal and r_bal and abs(l_height - r_height) <= 1
        total_height = max(l_height, r_height) + 1

        return total_height, node_balanced

    return verify(root)[1]


def test_is_balanced():
    t1 = TreeNode(10, TreeNode(5), TreeNode(15))
    assert is_balanced(t1) == True

    t2 = TreeNode(10, TreeNode(8, TreeNode(6)), None)
    assert is_balanced(t2) == False

    t3 = TreeNode(42)
    assert is_balanced(t3) == True

    t4 = None
    assert is_balanced(t4) == True

    t5 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(9)), TreeNode(5, None, TreeNode(7)))
    assert is_balanced(t5) == True

    t6 = TreeNode(7, TreeNode(5, TreeNode(4, TreeNode(3))), None)
    assert is_balanced(t6) == False

    t7 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, None, TreeNode(6, None, TreeNode(8))))
    assert is_balanced(t7) == False

    t8 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(8)))
    assert is_balanced(t8) == True

    t9 = TreeNode(10, TreeNode(9, TreeNode(8, TreeNode(7))), TreeNode(15))
    assert is_balanced(t9) == False
    
    print('Успех')

if __name__ == "__main__":
    test_is_balanced()
