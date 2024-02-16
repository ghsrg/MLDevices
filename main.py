# Файл main.py

from models import DeviceModelFactory
from training import Trainer
from exchange import DataExchangeQueue, DataExchangeHandler
from config import load_config

def main():
    # Завантаження конфігурації
    config = load_config()

    # Ініціалізація фабрики моделей
    model_factory = DeviceModelFactory()

    # Ініціалізація тренера
    trainer = Trainer()

    # Ініціалізація черги для обміну даними
    data_exchange_queue = DataExchangeQueue()

    # Ініціалізація обробника обміну даними
    data_exchange_handler = DataExchangeHandler()

    # Запуск основної логіки програми
    while True:
        # Отримання даних від портативних пристроїв
        data = data_exchange_queue.get_data()

        # Обробка отриманих даних
        processed_data = data_exchange_handler.process_data(data)

        # Навчання моделей на основному сервері
        trainer.train_models(processed_data)

        # Оновлення ваг моделей на портативних пристроях
        for device_id, model in processed_data.items():
            device = model_factory.get_device_model(device_id)
            device.update_model_weights(model)

if __name__ == "__main__":
    main()