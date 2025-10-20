class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_val):
        if new_val < self.value:
            if self.left is None:
                self.left = BST(new_val)
            else:
                self.left.insert(new_val)
        else:
            if self.right is None:
                self.right = BST(new_val)
            else:
                self.right.insert(new_val)

    def pre_order(self):
        seq = [self.value]
        if self.left:
            seq.extend(self.left.pre_order())
        if self.right:
            seq.extend(self.right.pre_order())
        return seq

    def post_order(self):
        seq = []
        if self.left:
            seq.extend(self.left.post_order())
        if self.right:
            seq.extend(self.right.post_order())
        seq.append(self.value)
        return seq

    def in_order(self):
        seq = []
        if self.left:
            seq.extend(self.left.in_order())
        seq.append(self.value)
        if self.right:
            seq.extend(self.right.in_order())
        return seq

    def reverse_pre_order(self):
        seq = [self.value]
        if self.right:
            seq.extend(self.right.reverse_pre_order())
        if self.left:
            seq.extend(self.left.reverse_pre_order())
        return seq

    def reverse_post_order(self):
        seq = []
        if self.right:
            seq.extend(self.right.reverse_post_order())
        if self.left:
            seq.extend(self.left.reverse_post_order())
        seq.append(self.value)
        return seq

    def reverse_in_order(self):
        seq = []
        if self.right:
            seq.extend(self.right.reverse_in_order())
        seq.append(self.value)
        if self.left:
            seq.extend(self.left.reverse_in_order())
        return seq


def test_bst():
    # Основное дерево
    tree_a = BST(8)
    tree_a.insert(4)
    tree_a.insert(12)
    tree_a.insert(2)
    tree_a.insert(6)
    tree_a.insert(10)
    tree_a.insert(14)

    assert tree_a.pre_order() == [8, 4, 2, 6, 12, 10, 14]
    assert tree_a.post_order() == [2, 6, 4, 10, 14, 12, 8]
    assert tree_a.in_order() == [2, 4, 6, 8, 10, 12, 14]
    assert tree_a.reverse_pre_order() == [8, 12, 14, 10, 4, 6, 2]
    assert tree_a.reverse_post_order() == [14, 10, 12, 6, 2, 4, 8]
    assert tree_a.reverse_in_order() == [14, 12, 10, 8, 6, 4, 2]

    # Второе дерево
    tree_b = BST(5)
    tree_b.insert(6)
    tree_b.insert(7)
    assert tree_b.pre_order() == [5, 6, 7]
    assert tree_b.post_order() == [7, 6, 5]
    assert tree_b.in_order() == [5, 6, 7]

    # Третье дерево
    tree_c = BST(6)
    tree_c.insert(3)
    tree_c.insert(5)
    assert tree_c.pre_order() == [6, 3, 5]
    assert tree_c.post_order() == [5, 3, 6]
    assert tree_c.in_order() == [3, 5, 6]

    print('Успех')

if __name__ == "__main__":
    test_bst()
