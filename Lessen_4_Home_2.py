from requests import get, utils


def currency_rates(char_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    i = content.find(char_code.upper())
    if i == -1:
        num = 'None'
    else:
        num = content[content.find('Value', i) + 6: content.find('<', content.find('Value', i))]

    return num


name_value = input('Название валюты: ')
print(f"Цена EUR: {currency_rates('EUR')};\n"
      f"Цена USD: {currency_rates('USD')};\n"
      f"Цена {name_value.upper()}: {currency_rates(name_value)}.")
