class MyHashTable:
    def __init__(self, initial_capacity=8, load_factor_threshold=0.75):
        self._capacity = initial_capacity
        self._size = 0
        self._load_factor_threshold = load_factor_threshold

        self._buckets = [[] for _ in range(self._capacity)]

    def _hash(self, key):
        return hash(key) % self._capacity

    def _get_load_factor(self):
        return self._size / self._capacity
        

    def _resize(self, new_capacity):
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

        print(f"новый размер {new_capacity}")

        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)
        
    def insert(self, key, value):
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

        if self._get_load_factor() > self._load_factor_threshold:
            self._resize(self._capacity * 2)


    def get(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        raise KeyError(f"Ключ '{key}' не найден")

    
    def delete(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                self._size -= 1
                return
        
        raise KeyError(f"Ключ '{key}' не найден")


    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __len__(self):
        return self._size

    def __str__(self):
        elements = []
        for bucket in self._buckets:
            for key, value in bucket:
                elements.append(f"'{key}': '{value}'")
        return "{" + ", ".join(elements) + "}"
    
    def __repr__(self):
        return str(self)
    
def test_hash_table():
    ht = MyHashTable(initial_capacity=4)
    
    # Вставка и поиск
    ht.insert("a", 5)
    ht.insert("b", 10)
    ht.insert("c", 15)
    
    assert ht.get("a") == 5
    assert ht.get("b") == 10
    assert ht.get("c") == 15
    
    # Обновление значения
    ht.insert("a", 8)
    assert ht.get("a") == 8
    
    # Удаление
    ht.delete("b")
    try:
        ht.get("b")
        assert False, "Ожидался KeyError для удалённого ключа"
    except KeyError:
        pass

    # Проверка удаления несуществующего ключа
    try:
        ht.delete("n")
        assert False, "Ожидался KeyError при удалении несуществующего ключа"
    except KeyError:
        pass
    
    # Коллизии 
    small_ht = MyHashTable(initial_capacity=2)
    small_ht.insert("a", 1)
    small_ht.insert("b", 2)
    small_ht.insert("c", 3)
    
    assert small_ht.get("a") == 1
    assert small_ht.get("b") == 2
    assert small_ht.get("c") == 3
    
    # Автоматическое увеличение размера
    auto_ht = MyHashTable(initial_capacity=4, load_factor_threshold=0.75)
    for i in range(10):
        auto_ht.insert(f"key_{i}", i)
    
    # Все значения на месте после ресайза
    for i in range(10):
        assert auto_ht.get(f"key_{i}") == i
            
    print("успех")

if __name__ == "__main__":
    test_hash_table()
