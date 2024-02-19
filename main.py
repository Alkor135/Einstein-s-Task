import pandas as pd
from random import sample


table = {1: ['желтый', 'Норвежец', 'вода', 'Тойота', 'лиса'],
         2: ['синий', 'Датчанин', 'чай', 'Порше', 'лошадь'],
         3: ['красный', 'Англичанин', 'молоко', 'Рено', 'улитки'],
         4: ['белый', 'Испанец', 'сок', 'Ауди', 'собака'],
         5: ['зеленый', 'Японец', 'кофе', 'БМВ', 'зебра']}

df_orig = pd.DataFrame(table, index=['Цвет', 'Национальность', 'Напиток', 'Авто', 'Животное'])
# print(df_orig, '\n')
df = pd.DataFrame(columns=[1, 2, 3, 4, 5])  # Создание DF c нумерованными колонками

for row in df_orig.itertuples(index=True):  # Перебираем строки DF
    elem_lst = [row[1], row[2], row[3], row[4], row[5]]  # Создание списка из элементов строки
    elem_lst = sample(elem_lst, len(elem_lst))  # Перемешивание словаря
    df.loc[row[0]] = elem_lst  # Добавление новой строки в DF

# print(df, '\n')

task = (f'1. На улице стоят пять домов.\n'
        # f'2. Англичанин живёт в красном доме.\n'
        f'2. {df.loc["Национальность", 3]} живёт в {df.loc["Цвет", 3]} дом.\n'
        f'3. У {df.loc["Национальность", 4]} есть {df.loc["Животное", 4]}.\n'
        f'4. В {df.loc["Цвет", 5]} дом пьют {df.loc["Напиток", 5]}.\n'
        f'5. {df.loc["Национальность", 2]} пьёт {df.loc["Напиток", 2]}.\n'
        f'6. {df.loc["Цвет", 5]} дом стоит сразу справа от {df.loc["Цвет", 4]} дом.\n'
        f'7. Тот, кто ездит на {df.loc["Авто", 3]}, разводит {df.loc["Животное", 3]}.\n'
        f'8. В {df.loc["Цвет", 1]} дом, ездят на {df.loc["Авто", 1]}.\n'
        f'9. В центральном доме пьют {df.loc["Напиток", 3]}.\n'
        f'10. {df.loc["Национальность", 1]} живёт в первом доме.\n'
        f'11. Сосед того, кто ездит на {df.loc["Авто", 2]}, держит {df.loc["Животное", 1]}.\n'
        f'12. В доме по соседству с тем, в котором держат {df.loc["Животное", 2]}, ездят на {df.loc["Авто", 1]}.\n'
        f'13. Тот, кто ездит на {df.loc["Авто", 4]}, пьёт {df.loc["Напиток", 4]}.\n'
        f'14. {df.loc["Национальность", 5]} ездит на {df.loc["Авто", 5]}.\n'
        f'15. {df.loc["Национальность", 1]} живёт рядом с {df.loc["Цвет", 2]} дом.\n'
        f'Кто пьёт {df.loc["Напиток", 1]}? Кто держит {df.loc["Животное", 5]}?')

print(task)
