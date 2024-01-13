class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        print(key_hash)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def delete(self, key):
        key_hash = self.hash_function(key)

        if self.table[key_hash] is None:
            return False
        else:
            for i in range(0, len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


if __name__ == "__main__":
    # Тестуємо нашу хеш-таблицю:
    H = HashTable(5)
    print("Додавання елементів:")
    print(H.insert("apple", 10))
    print(H.insert("apple", 20))
    print(H.insert("orange", 20))
    print(H.insert("banana", 30))

    print("Виведемо всі елементи:")
    print(H.table)

    print("Видалення елементів:")
    print(H.delete("banana"))

    print("Виведемо всі елементи:")
    print(H.table)
