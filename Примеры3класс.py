import random

set_tab = set()

def Tablica_umn(): # функция умножения
    num1 = str(random.randint(3,9))
    num2 = str(random.randint(3,9))
    stroka = num1 + " x " + num2 + " = \n"
    return(stroka)


def Tablica_del(): # фукция деления
    num3 = random.randint(3,9)
    num4 = random.randint(3,9)
    num5 = str(num3 * num4)
    stroka = num5 + " : " + str(num3) + " = \n"
    return(stroka)


while len(set_tab) < 40: # создание таблицы примеров
    word1 = Tablica_umn()
    set_tab.add(word1)
    word2 = Tablica_del()
    set_tab.add(word2)


with open ('Примеры.txt' , 'w') as word: # создание файла
    for i in set_tab:
        word.write(i)
        word.write('\n')


