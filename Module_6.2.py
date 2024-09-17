class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'black', 'white', 'green']  # Список допустимых цветов окрашивания

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner  # Владелец транспорта(изменяемый)
        self.__model = __model  # Модель транспорта(не можем менять название)
        self.__engine_power = __engine_power  # Мощность(не можем менять мощность самостоятельно)
        self.__color = __color  # Название цвета(не можем менять название сами)

    def get_model(self):
        return f'Модель: {self.__model}.'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}.'

    def get_color(self):
        return f'Цвет: {self.__color}.'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}.')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}.')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Marc II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()