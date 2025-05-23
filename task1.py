from queue import Queue


# Створити чергу заявок
queue = Queue()
n = 0


def generate_request(num):
    global n
    # Створити нову заявку
    for i in range(num):
        n += 1
        # Додати заявку до черги
        queue.put(f'Заявка №{n}')


def process_request(queue):
    while not queue.empty():
            # Витягти заявку з черги
            request = queue.get()
            # Обробити заявку
            print(f'Обробка {request}')
    # Вивести повідомлення, що черга пуста
    print('Черга пуста')
    global n
    n = 0


# Головний цикл програми:
# Поки користувач не вийде з програми:
while user_input := input("Введіть кількість заявок для генерації: "):
    num = int(user_input)
    # Виконати generate_request() для створення нових заявок
    generate_request(num)
    # Виконати process_request() для обробки заявок
    process_request(queue)
