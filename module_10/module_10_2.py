from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name_knight: str, power: int):
        self.name_knight = name_knight
        self.power = power
        self.enemies = 100
        self.days = 0
        super().__init__()

    def run(self):
        print(f"{self.name_knight}, на нас напали!")
        self.days = 0
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            print(f"{self.name_knight} сражается {self.days}..., осталось {self.enemies} воинов.")
        print(f"{self.name_knight} одержал победу спустя {self.days} дней(дня)!")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()