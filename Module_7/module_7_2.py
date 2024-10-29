def custom_write(file_name, strings):
    dict_ = {}
    file = open(file_name, 'w', encoding="utf-8")
    for string in strings:
        index = strings.index(string)
        position = (file.tell())
        file.write(str(string))
        file.write('\n')
        dict_.update({(index + 1, position): string})
    file.close()
    return dict_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
