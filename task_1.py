import random

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
            if 0 >= len(name) or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if not name in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__name_items.append(name)
                self.__number_items += 1

    def delete_item_from_check(self, name):
        if not name in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):

        total = []

        for item in self.__name_items:
            if item in self.__item_price:
                total.append(self.__item_price[item])

        if self.__number_items > 10:
            return sum(total) * 0.9
        return sum(total)

    def twenty_percent_tax_calculation(self):
        tax_rate = 20
        twenty_percent_tax = list(filter(lambda x: self.__tax_rate[x] == tax_rate, self.__name_items))
        total = list(map(lambda x: self.__item_price[x], twenty_percent_tax))
        if self.__number_items > 10:
            return sum(total) * 0.9 * (tax_rate / 100)
        return sum(total) * (tax_rate / 100)

    def ten_percent_tax_calculation(self):
        tax_rate = 10
        ten_percent_tax = list(filter(lambda x: self.__tax_rate[x] == tax_rate, self.__name_items))
        total = list(map(lambda x: self.__item_price[x], ten_percent_tax))
        if self.__number_items > 10:
            return sum(total) * 0.9 * (tax_rate / 100)
        return sum(total) * (tax_rate / 100)

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if not type(telephone_number).__name__ == 'int':
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'


#вызовы
osrc = OnlineSalesRegisterCollector()

osrc.add_item_to_cheque('чипсы')
osrc.add_item_to_cheque('кола')
osrc.add_item_to_cheque('печенье')
osrc.add_item_to_cheque('молоко')
osrc.add_item_to_cheque('кефир')
osrc.add_item_to_cheque('чипсы')
osrc.add_item_to_cheque('кола')
osrc.add_item_to_cheque('печенье')
osrc.add_item_to_cheque('молоко')
osrc.add_item_to_cheque('кефир')
osrc.add_item_to_cheque('чипсы')
osrc.add_item_to_cheque('кола')
osrc.add_item_to_cheque('печенье')
osrc.add_item_to_cheque('молоко')
osrc.add_item_to_cheque('кефир')

print(f'Сумма: {osrc.check_amount()}')
print(f'20% НДС: {osrc.twenty_percent_tax_calculation()}')
print(f'10% НДС: {osrc.ten_percent_tax_calculation()}')
print(f'Сумма НДС: {osrc.total_tax()}')
print(f'Номер: {osrc.get_telephone_number(int(''.join(str(random.randint(0, 9)) for _ in range(10))))}')