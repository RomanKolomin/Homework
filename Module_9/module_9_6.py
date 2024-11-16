def all_variants(text):
    for size in range(len(text)):
        for position in range(len(text)-size):
            yield text[position:(position + 1 + size)]


a = all_variants("abc")
for i in a:
    print(i)
