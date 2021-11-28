from Lessen_4_Home_4_utils import currency_rates


name_value = input('Название валюты: ')
print(f"Цена EUR: {currency_rates('EUR', 0)}\n"
      f"Цена USD: {currency_rates('USD', 0)}\n"
      f"Цена {name_value.upper()}: {currency_rates(name_value, 1)}")
