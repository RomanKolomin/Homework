calls = 0


def string_info(string):
    global calls
    tuple_ = (len(string), string.upper(), string.lower())
    calls += 1
    return tuple_


def is_contains(string, list_to_search):
    global calls
    calls += 1
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
