EXCHANGE_RATES = {
    'USD': 1,
    'EUR': 1.3,
    'RUB': 0.01425,
    'BTC': 1000,
}


def get_exchange_rates():  # TODO: получать данные по API
    return EXCHANGE_RATES


def main():
    exchange_rates = get_exchange_rates()
    base_currency = input(f'Введите валюту, которую хотите менять {list(exchange_rates)}\n')  # TODO: сделать красивый вывод списка
    target_currency = input(f'Введите валюту, на которую хотите менять {list(exchange_rates)}\n')  # TODO: сделать красивый вывод списка
    # TODO: проверить ввод пользователя на то, что валюта существует
    currency_amount = int(input('Введите количество валюты\n'))  # TODO: добавить возможность использования нецелых чисел

    cross_course = exchange_rates[base_currency] / exchange_rates[target_currency]

    print(round(currency_amount * cross_course, 2))


main()
