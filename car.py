import os
import csv
from typing import List, Union, Tuple


class CarBase:
    def __init__(self, brand: str, photo_file_name: str, carrying: float):
        """
        Базовый класс для всех типов автомобилей.

        :param brand: Марка автомобиля.
        :param photo_file_name: Имя файла с фотографией автомобиля.
        :param carrying: Грузоподъемность автомобиля.
        """
        self.car_type: str = None  # должен быть установлен в подклассе
        self.brand: str = brand
        self.photo_file_name: str = photo_file_name
        self.carrying: float = float(carrying)

    def get_photo_file_ext(self) -> str:
        """
        Возвращает расширение файла с фотографией.

        :return: Расширение файла с фотографией (например, '.png', '.jpg').
        """
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    def __init__(self, brand: str, photo_file_name: str, carrying: float, passenger_seats_count: int):
        """
        Класс для легкового автомобиля.

        :param brand: Марка автомобиля.
        :param photo_file_name: Имя файла с фотографией автомобиля.
        :param carrying: Грузоподъемность автомобиля.
        :param passenger_seats_count: Количество пассажирских мест.
        """
        super().__init__(brand, photo_file_name, carrying)
        self.car_type: str = 'car'
        self.passenger_seats_count: int = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand: str, photo_file_name: str, carrying: float, body_whl: str):
        """
        Класс для грузового автомобиля.

        :param brand: Марка автомобиля.
        :param photo_file_name: Имя файла с фотографией автомобиля.
        :param carrying: Грузоподъемность автомобиля.
        :param body_whl: Размеры кузова в формате 'длина x ширина x высота'.
        """
        super().__init__(brand, photo_file_name, carrying)
        self.car_type: str = 'truck'
        self.body_length, self.body_width, self.body_height = self.parse_body_whl(body_whl)

    def parse_body_whl(self, body_whl: str) -> Tuple[float, float, float]:
        """
        Разбирает строку с размерами кузова и возвращает их в виде кортежа чисел.

        :param body_whl: Строка с размерами кузова.
        :return: Кортеж из длины, ширины и высоты кузова.
        """
        if body_whl:
            return tuple(map(float, body_whl.split('x')))
        return 0.0, 0.0, 0.0

    def get_body_volume(self) -> float:
        """
        Возвращает объем кузова грузового автомобиля.

        :return: Объем кузова в метрах кубических.
        """
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand: str, photo_file_name: str, carrying: float, extra: str):
        """
        Класс для специальной техники.

        :param brand: Марка техники.
        :param photo_file_name: Имя файла с фотографией техники.
        :param carrying: Грузоподъемность техники.
        :param extra: Дополнительная информация о технике.
        """
        super().__init__(brand, photo_file_name, carrying)
        self.car_type: str = 'spec_machine'
        self.extra: str = extra


def get_car_list(csv_filename: str) -> List[Union[Car, Truck, SpecMachine]]:
    """
    Функция для создания списка объектов автомобилей из CSV файла.

    :param csv_filename: Имя CSV файла с данными об автомобилях.
    :return: Список объектов автомобилей.
    """
    car_list: List[Union[Car, Truck, SpecMachine]] = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if car_type == 'car':
                    car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                elif car_type == 'truck':
                    car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                elif car_type == 'spec_machine':
                    car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
            except (ValueError, IndexError):
                # Пропускаем строки с некорректными данными
                pass
    return car_list
