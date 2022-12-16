import requests


EXCHANGE_RATES = {
    'USD': 1,
    'EUR': 1.3,
    'RUB': 0.01425,
    'BTC': 1000,
    'GBP': 1.5,
}


def get_exchange_rates():  # Реализовать получение курсов по API
    return EXCHANGE_RATES


def main():
    exchange_rates = get_exchange_rates()
    base_currency = input(f'Введите валюту, которую хотите обменять {list(exchange_rates)}\n')
    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода
    target_currency = input(f'Введите валюту, на которую хотите обменять {list(exchange_rates)}\n')
    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода
    currency_amount = float(input('Введите количество валюты\n'))

    cross_course = exchange_rates[base_currency] / exchange_rates[target_currency]
    result = round(cross_course * currency_amount, 2)
    print(result)  # добавить валюту в вывод


main()

