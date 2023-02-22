# Pavlo Yatluk
# dz_30_1

# Написати клас для створення і роботи з хеш - таблицями. Клас повинен містити наступні функції:#
# створення хеш талиці заданої довжини, пошук , додавання і видалення нових елементів, друкування хеш - таблиці,
# виправлення колізій.

class HashTable:

    def __init__(self, length: int):
        self.length = length
        self.hash_table = [[]] * length

    def __str__(self):
       return ''.join(map(str, self.hash_table))

    def hash_func(self, key):
        return key % self.length

    def add(self, key, value):
        index = self.hash_func(key)
        if not self.hash_table[index]:
            self.hash_table[index] = [key, value]
        else:
            self.hash_table[index].extend([key, value])

    def search(self, key):
        index = self.hash_func(key)
        if self.hash_table[index]:
            return self.hash_table[index][self.hash_table[index].index(key) + 1]
        else:
            return None

    def remove(self, key: int, data):
        index = self.hash_func(key)
        result = self.search(key)
        if result:
            if data in self.hash_table[index]:
                self.hash_table[index].remove(key)
                self.hash_table[index].remove(data)
            else:
                error = ValueError(f'Відсутнє значення \'{data}\' з ключем ({key}).')
                raise error
        else:
            error = KeyError(f'Відсутній ключ ({key}) у хеш-таблиці.')
            raise error

ht = HashTable(5)
print(ht)

