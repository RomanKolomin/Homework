immutable_var = (1, 3.5, True, [1,2,3], (1, 3, 5))
print(immutable_var)
# immutable_var[0] = 2.43 # Нельзя, т.к. кортеж не позволяет изменять значения элементов
mutable_list = [1, 2.5, "hi", (1,2)]
mutable_list[3] = True
print(mutable_list)