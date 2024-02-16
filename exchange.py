class DataExchangeQueue:
    def __init__(self):
        self.queue = []

    def get_data(self):
        # Отримання даних з черги
        return self.queue.pop(0)

    def add_data(self, data):
        # Додавання даних до черги
        self.queue.append(data)

class DataExchangeHandler:
    def process_data(self, data):
        # Обробка отриманих даних перед навчанням моделей
        return data