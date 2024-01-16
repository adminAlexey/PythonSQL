# Особенный номер – строка формата [2-4 цифры]\[2-5 цифр]. 
# Хороший номер - строка формата [4 цифры]\[5 цифр]. 
# Хороший номер можно получить из особенного дополнением нулей слева к обоим числам.
# Пример: 17\234 => 0017\00234

import re

def special_number(line):
    specials = []

    while len(line) > 0:
        index = line.find("\\")
        left_line = line[:index]
        right_line = line[index+1:]

        if index == -1:
            break
        
        count_left = 0 #счетчик цифр перед символом '\'
        count_right = 0 #счетчик цифр после символа '\'
        for i in range(1, len(left_line) + 1):
            if line[index - i].isdigit() == True and count_left  < 4:
                count_left += 1
            else: 
                break
        
        for i in range(1,len(right_line) + 1):
            if line[index + i].isdigit() == True and count_right < 5:
                count_right += 1
            else: 
                break

        if count_left > 1 and count_right > 1:
            special = line[index - count_left: index + count_right + 1]
            specials.append(special)
            line = line[index + count_right + 1:]
            print("Найден особенный номер:\t" + special)
        else:
            line = line[index+1:]
       
    return specials

def good_number(specials):
    goods = []
    for i in range(len(specials)):
        index = specials[i].find("\\")
        good = ""
        if index != 4:
            for j in range(4-index):
                good += "0"
        good += specials[i]
        while len(good) < 10:
            good = good[:5] + "0" + good[5:]
        goods.append(good)
    
    print("Получен список хороших номеров:\n")
    for g in goods:
        print(g)    
    

line = input("Введите строку - ")

if line == "":
    line = "Адрес 5467\\456. Номер123\\231aa\\21\\2111111\\444a32a\\201\\1111111\\1"

good_number(special_number(line))

##################################################

print("\n\n\n")
regex = r"\d{2,4}\\\d{2,5}"

line = r'Адрес 5467\456. Номер123\231aa\21\2111111\444a32a\201\1111111\1'

matches = re.findall(regex, line)

good_number(matches)