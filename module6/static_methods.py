class my_class:
    atribut_class = True

    def __init__(self,name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    @classmethod
    def change_class_atribut(cls, new_value):
        cls.atribut_class = new_value


a1 = my_class('a1')
a2 = my_class('a2')
a3 = my_class('a3')

print(a2.name)
print(a1.atribut_class)
print(a2.atribut_class)
print(a3.atribut_class)
a2.change_name('aaaaaaa2')
print(a2.name)

my_class.change_class_atribut(False)
print(a1.atribut_class)
print(a2.atribut_class)
print(a3.atribut_class)