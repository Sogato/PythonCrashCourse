filename_1 = 'examples/war-and-peace.txt'
filename_2 = 'examples/letters_from_a_cat.txt'
filename_3 = 'examples/the-call-of-the-wild.txt'

file_list = [filename_1, filename_2, filename_3]

for file in file_list:
    try:
        try:
            with open(file, encoding='utf-8') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            print(f'Файл "{file}" не поодерживает кодировку UTF-8.')
            continue

    except FileNotFoundError:
        print(f'Файл "{file}" не найден.')
    else:
        sum_count1 = 0
        sum_count2 = 0
        for line in lines:
            sum_count1 += line.lower().count('the')
            sum_count2 += line.lower().count('the ')

        print(f'Колличество вхождений слова "the" в файл "{file}": ', sum_count1)
        print(f'Колличество вхождений слова "the " в файл "{file}": ', sum_count2)
