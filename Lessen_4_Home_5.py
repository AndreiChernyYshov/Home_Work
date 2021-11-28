from sys import argv
from Lessen_4_Home_5_utils import currency_rates

name, s_1 = argv
print(f"Цена {s_1.upper()}: {currency_rates(s_1)}")
