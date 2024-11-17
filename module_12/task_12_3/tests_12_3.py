import sys
import os

# Добавляем корневую директорию в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), r'..\task_12_1'))
sys.path.insert(0, project_root)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), r'..\task_12_2'))
sys.path.insert(0, project_root)

import unittest
from module_12_1 import RunnerTest  # Импортируем RunnerTest из соответствующего модуля
from module_12_2 import TournamentTest  # Импортируем TournamentTest из соответствующего модуля

# Создаем объект TestSuite
suite = unittest.TestSuite()

# Добавляем тесты из RunnerTest и TournamentTest в TestSuite
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем объект TextTestRunner с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тестовый набор
runner.run(suite)
