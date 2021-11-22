my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']
index_list = []

for b, meaning3 in enumerate(my_list):
    if meaning3[-1].isdigit() == True:
        index_list.append(str(b + 1) + ": " + meaning3)

for i, meaning in enumerate(my_list):
    if meaning[-1].isdigit() == True:
        if meaning.isdigit() == False:
            for k, meaning2 in enumerate(list(my_list[i])):
                if meaning2.isdigit() == True:
                    my_list[i] = my_list[i][:k] + my_list[i][k:].zfill(2)
                    break
        else:
            meaning = meaning.zfill(2)

        my_list[i] = '"' + meaning + '"'

print(" ".join(my_list))
print(" \n".join(index_list))