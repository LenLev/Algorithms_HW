class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def _height(self, n):
        return n.height if n else 0

    def _balance(self, n):
        return self._height(n.left) - self._height(n.right) if n else 0

    def _rotate_right(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _rotate_left(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def insert(self, root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        else:
            return root
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        b = self._balance(root)
        if b > 1 and val < root.left.val:
            return self._rotate_right(root)
        if b < -1 and val > root.right.val:
            return self._rotate_left(root)
        if b > 1 and val > root.left.val:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if b < -1 and val < root.right.val:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        return root

    def _min_value(self, n):
        while n.left:
            n = n.left
        return n

    def delete(self, root, val):
        if not root:
            return root
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        b = self._balance(root)
        if b > 1 and self._balance(root.left) >= 0:
            return self._rotate_right(root)
        if b > 1 and self._balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if b < -1 and self._balance(root.right) <= 0:
            return self._rotate_left(root)
        if b < -1 and self._balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        return root

    def search(self, root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.search(root.left, val)
        return self.search(root.right, val)


def test_avl():
    avl = AVL()
    root = None

    # вставка
    for v in [10, 20, 30, 40, 50, 25]:
        root = avl.insert(root, v)
    assert avl.search(root, 25).val == 25

    # удаление
    root = avl.delete(root, 40)
    assert not avl.search(root, 40)

    # поиск
    assert avl.search(root, 10).val == 10
    assert avl.search(root, 100) is None

    # проверка сбалансированности
    def check_balance(node):
        if not node:
            return True
        lh = avl._height(node.left)
        rh = avl._height(node.right)
        if abs(lh - rh) > 1:
            return False
        return check_balance(node.left) and check_balance(node.right)

    assert check_balance(root)

    print("Успех")

if __name__ == "__main__":
    test_avl()