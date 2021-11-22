my_list = ['инженер-конструктор Игорь',
           'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй',
           'директор аэлита']

for i, meaning in enumerate(my_list):
    meaning = meaning.title()
    print(meaning.replace(meaning[:meaning.rfind(" ")], "Привет"))