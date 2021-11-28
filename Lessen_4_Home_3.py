import datetime
from requests import get, utils


def currency_rates(char_code, t):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    i = content.find(char_code.upper())
    if i == -1:
        num = 'None'
    else:
        num = content[content.find('Value', i) + 6: content.find('<', content.find('Value', i))]

    if t == 1:
        date_per = content.find('Date')
        date = content[content.find('"', date_per) + 1: content.find('"', content.find('"', date_per) + 1)].split('.')
        
        return f'{num}\n{datetime.date(int(date[2]), int(date[1]), int(date[0]))}'

    return num


name_value = input('Название валюты: ')
print(f"Цена EUR: {currency_rates('EUR', 0)}\n"
      f"Цена USD: {currency_rates('USD', 0)}\n"
      f"Цена {name_value.upper()}: {currency_rates(name_value, 1)}")
