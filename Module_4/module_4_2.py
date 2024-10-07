def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


# inner_function() - функция определена только в функции test_function
