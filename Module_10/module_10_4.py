import threading
from queue import Queue
from random import randint
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
        self.empty_tables = len(self.tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if not table.guest and self.empty_tables > 0:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    self.empty_tables -= 1
                    break
                elif self.empty_tables == 0:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')
                    break

    def discuss_guests(self):
        while self.empty_tables < len(self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал и ушел')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    self.empty_tables += 1
                    print(self.empty_tables)
                elif not table.guest and not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    self.empty_tables -= 1


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
