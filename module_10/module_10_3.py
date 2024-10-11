import time
from threading import Lock
import threading
import random


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.trans_dep = 100
        self.trans_take = 100

    def deposit(self):
        for trans in range(self.trans_dep):
            dep = random.randint(50, 500)
            # Блокировка перед изменением баланса
            if self.balance >= 500 and not self.lock.acquire(blocking=False):
                self.lock.release()
            self.balance += dep

            print(f"Пополнение: {dep}. Баланс: {self.balance}")
            time.sleep(0.001)  # Задержка для имитации работы

    def take(self):
        for trans in range(self.trans_take):
            take = random.randint(50, 500)
            # Блокировка перед изменением баланса
            if take > self.balance:
                print(f'Запрос отклонён, недостаточно средств. Запрашиваемая сумма: {take}, Доступный баланс: {self.balance}')
                self.lock.acquire()
            else:
                self.balance -= take
                print(f"Снятие: {take}. Баланс: {self.balance}")
            time.sleep(0.001)  # Задержка для имитации работы


bk = Bank()

# Создание потоков
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
