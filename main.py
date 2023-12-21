from car import get_car_list

if __name__ == "__main__":
    cars = get_car_list('cars.csv')
    for car in cars:
        print(f'Type: {car.car_type}, Brand: {car.brand}, Photo Ext: {car.get_photo_file_ext()}')
        if hasattr(car, 'get_body_volume'):
            print(f'Body Volume: {car.get_body_volume()}')
        print('-' * 30)
