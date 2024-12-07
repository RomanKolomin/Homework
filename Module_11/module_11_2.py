class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('hello')


def introspection_info(obj):
    dict_ = {}
    type_ = str(type(obj)).replace("<class '", "").replace("'>", "").replace("__main__.", "")
    try:
        module = obj.__module__
    except:
        module = '__main__'
    dict_.update({'type': type_,
                  'attributes': [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))],
                  'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
                  'module': module})
    return dict_


dude = Person('Alex', 25)

print(introspection_info(dude))
print(introspection_info(42))
