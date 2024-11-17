from runner_and_tournament import Tournament, Runner
from unittest import TestCase


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    def testTournament_1(self):
        t1 = Tournament(90, self.r1, self.r3)
        TournamentTest.all_results[1]  = t1.start()
        last_сompetition = list(TournamentTest.all_results.keys())[-1]
        last_runner = list(TournamentTest.all_results[last_сompetition].keys())[-1]
        self.assertTrue(str(TournamentTest.all_results[last_сompetition][last_runner])==self.r3.name)

    def testTournament_2(self):
        t2 = Tournament(90, self.r2, self.r3)
        TournamentTest.all_results[2]  = t2.start()
        last_сompetition = list(TournamentTest.all_results.keys())[-1]
        last_runner = list(TournamentTest.all_results[last_сompetition].keys())[-1]
        self.assertTrue(str(TournamentTest.all_results[last_сompetition][last_runner])==self.r3.name)

    def testTournament_3    (self):
        t3 = Tournament(90, self.r1, self.r2, self.r3)
        TournamentTest.all_results[3]  = t3.start()
        last_сompetition = list(TournamentTest.all_results.keys())[-1]
        last_runner = list(TournamentTest.all_results[last_сompetition].keys())[-1]
        self.assertTrue(str(TournamentTest.all_results[last_сompetition][last_runner])==self.r3.name)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results.keys():
            print(f'competition {key}')
            for k, v in cls.all_results[key].items():
                print(k, str(v))
