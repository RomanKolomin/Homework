my_dict = {'Roman': 1993 , 'Pavel': 1976, 'Elena': 1969}
print(my_dict)
print(my_dict['Roman'])
print(my_dict.get('Alex', 'Alex не в списке'))
my_dict.update({'Rita': 1992, 'Dasha': 2002})
print(my_dict.pop('Pavel'))
print(my_dict)

my_set = {1, 2, 'Season', (1, 3, 5), 2, 1, (1, 3, 5)}
print(my_set)
my_set.update({0, 4})
my_set.discard(2)
print(my_set)

print('my_set')