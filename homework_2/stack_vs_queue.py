class Node:
    # Узел односвязного списка
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack:
    # LIFO
    def __init__(self):
        self.top = None
        self._size = 0

    # Положить значение на вершину стека
    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node
        self._size += 1

    # Взять и вернуть значение с обработкой пустого стека
    def pop(self):
        if self.top is None:
            raise IndexError('empty stack')
        value = self.top.value
        self.top = self.top.next_node
        self._size -= 1
        return value

    # Посмотреть значение на вершине без удаления
    def peek(self):
        if self.top is None:
            raise IndexError('peek from empty stack')
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size
    
class Queue:
    # FIFO
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Добавить значение в конец очереди
    def enqueue(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self._size += 1
       
    # Взять и вернуть значение с обработкой пустой очереди
    def dequeue(self):
        if self.head is None:
            raise IndexError('empty queue')
        node = self.head
        self.head = node.next_node
        if self.head is None:
            self.tail = None
        self._size -= 1
        return node.value

    # Посмотреть первый элемент без удаления с обработкой пустой очереди
    def peek(self):
        if self.head is None:
            raise IndexError('peek from empty queue')
        return self.head.value
    
    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

def run_tests():
    # Тестирование стека (LIFO)
    s = Stack()
    assert s.is_empty()
    assert s.size() == 0

    s.push(1)
    s.push(2)
    s.push(3)

    assert s.size() == 3
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    assert s.size() == 0

    try:
        s.pop()
        assert False, "Expected IndexError for pop from empty stack"
    except IndexError:
        pass

    try:
        s.peek()
        assert False, "Expected IndexError for peek from empty stack"
    except IndexError:
        pass

    # Дополнительные тесты для стека
    s2 = Stack()
    for i in range(5):
        s2.push(i)
    
    assert s2.size() == 5
    assert s2.peek() == 4
    
    for i in range(4, -1, -1):
        assert s2.pop() == i
    
    assert s2.is_empty()

    # Тестирование очереди (FIFO)
    q = Queue()
    assert q.is_empty()
    assert q.size() == 0

    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')

    assert q.size() == 3
    assert q.peek() == 'a'
    assert q.dequeue() == 'a'
    assert q.dequeue() == 'b'
    assert q.dequeue() == 'c'
    assert q.is_empty()
    assert q.size() == 0

    try:
        q.dequeue()
        assert False, "Expected IndexError for dequeue from empty queue"
    except IndexError:
        pass
    
    try:
        q.peek()
        assert False, "Expected IndexError for peek from empty queue"
    except IndexError:
        pass

    # Проверка поведения хвоста после опустошения
    q2 = Queue()
    q2.enqueue(10)
    assert q2.dequeue() == 10
    q2.enqueue(20)
    q2.enqueue(30)
    assert q2.dequeue() == 20
    assert q2.dequeue() == 30
    assert q2.is_empty()

    # Дополнительные тесты для очереди
    q3 = Queue()
    for i in range(5):
        q3.enqueue(i)
    
    assert q3.size() == 5
    assert q3.peek() == 0
    
    for i in range(5):
        assert q3.dequeue() == i
    
    assert q3.is_empty()

    print("Тесты пройдены")


if __name__ == "__main__":
    run_tests()