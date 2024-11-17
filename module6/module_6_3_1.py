class Horse:
    sound = 'Frrr'

    def __init__(self):
        self.x_distance = 0

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.y_distance = 0

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    sound = Eagle.sound

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

# Создаем объект класса Pegasus и вызываем методы
p1 = Pegasus()

print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

p1.voice()  # I train, eat, sleep, and repeat