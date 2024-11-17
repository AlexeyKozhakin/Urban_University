import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r1 = Runner('John')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50)

    def test_run(self):
        r2 = Runner('Sam')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challange(self):
        r3 = Runner('Joanna')
        r4 = Runner('Lisa')
        for _ in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)


