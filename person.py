class Person:
    def __init__(self, name, family):
        self.__name = name
        self.__family = family

    def set_name(self, new_name):
        # ...
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_family(self, new_family):
        # ... check the new_family's value
        self.__family = new_family

    def get_family(self):
        return self.__family