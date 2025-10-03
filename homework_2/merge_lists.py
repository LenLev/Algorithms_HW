# реализация односвязного списка
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # Преобразование списка в Python список для проверок
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

# Вспомогательная функция для создания списка из массива
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 1. С фиктивным элементом
def merge_with_dummy(list1, list2):
    dummy = ListNode(-1)  # фиктивный узел
    current = dummy

    # Проход по спискам
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Присоединение оставшихчя узлов
    current.next = list1 if list1 else list2

    # Возвращаем следующий узел после фиктивного
    return dummy.next


# 2. Без фиктивного элемента
def merge_without_dummy(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    # Определяем голову нового списка
    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    # Проход по спискам
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Присоединение оставшихчя узлов
    current.next = list1 if list1 else list2

    # Возвращаем следующий узел после фиктивного
    return head


def merge_tests():
    # Данные для тестов
    l1 = create_linked_list([1,2,4])
    l2 = create_linked_list([1,3,4])

    # С фиктивным элементом
    merged1 = merge_with_dummy(l1, l2)
    assert merged1.to_list() == [1,1,2,3,4,4]

    # Обновляем данные для тестов
    l1 = create_linked_list([1,2,4])
    l2 = create_linked_list([1,3,4])

    # Без фиктивного элемента
    merged2 = merge_without_dummy(l1, l2)
    assert merged2.to_list() == [1,1,2,3,4,4]

    # Проверка пустых списков
    assert merge_with_dummy(None, None) == None
    assert merge_without_dummy(None, None) == None

    # Проверка для одного пустого списка
    l3 = create_linked_list([0,5])
    assert merge_with_dummy(l3, None).to_list() == [0,5]

    l3 = create_linked_list([0,5])
    assert merge_without_dummy(None, l3).to_list() == [0,5]

    # Разные длины списков
    l4 = create_linked_list([10, 12, 14, 16])
    l5 = create_linked_list([11, 13, 15])
    
    merged3 = merge_without_dummy(l4, l5)
    assert merged3.to_list() == [10, 11, 12, 13, 14, 15, 16]

    l4 = create_linked_list([10, 12, 14, 16])
    l5 = create_linked_list([11, 13, 15])
    
    merged4 = merge_with_dummy(l4, l5)
    assert merged4.to_list() == [10, 11, 12, 13, 14, 15, 16]

    print('Тесты пройдены')

if __name__ == "__main__":
    merge_tests()