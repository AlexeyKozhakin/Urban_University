class Horse:
    sound = 'Frrr'
    color = 'Black'
    def __init__(self, name):
        self.name = name

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color




def fun(a,b):
    return a*b


a1 = Horse('a1')
a2 = Horse('a2')
a3 = Horse('a3')

print(a1.name)
print(a1.color)
print(a2.color)
print(a3.color)
Horse.change_color('White')

print(a1.color)
print(a2.color)
print(a3.color)