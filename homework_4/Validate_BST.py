class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    def check_bst(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        return (
            check_bst(node.left, lower, node.val)
            and check_bst(node.right, node.val, upper)
        )

    return check_bst(root)


def test_is_valid_bst():
    t1 = TreeNode(8, TreeNode(3), TreeNode(10))
    assert is_valid_bst(t1) == True

    t2 = TreeNode(6, TreeNode(2), TreeNode(8, TreeNode(4), TreeNode(9)))
    assert is_valid_bst(t2) == False

    t3 = TreeNode(42)
    assert is_valid_bst(t3) == True

    t4 = TreeNode(7, TreeNode(3), TreeNode(9, TreeNode(5), TreeNode(10)))
    assert is_valid_bst(t4) == False

    t5 = TreeNode(9, TreeNode(4, TreeNode(2), TreeNode(11)), TreeNode(12))
    assert is_valid_bst(t5) == False

    t6 = None
    assert is_valid_bst(t6) == True

    t7 = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)), TreeNode(25, TreeNode(22), TreeNode(30)))
    assert is_valid_bst(t7) == True

    t8 = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)), TreeNode(25, TreeNode(18), TreeNode(30)))
    assert is_valid_bst(t8) == False

    t9 = TreeNode(15, TreeNode(8, TreeNode(3), TreeNode(15)), TreeNode(18))
    assert is_valid_bst(t9) == False

    t10 = TreeNode(12, TreeNode(6, TreeNode(2), TreeNode(8)), TreeNode(18, TreeNode(14), TreeNode(12)))
    assert is_valid_bst(t10) == False

    print('Успех')

if __name__ == "__main__":
    test_is_valid_bst()
