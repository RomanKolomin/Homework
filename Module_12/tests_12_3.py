import runner_and_tournament
import runner
import unittest

is_frozen = True


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        name = runner.Runner("name")
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        name = runner.Runner("name")
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self):
        name_1 = runner.Runner("name_1")
        name_2 = runner.Runner("name_2")
        for i in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner_2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner_3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            for place in result:
                result.update({place: str(result[place])})
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testTournament_1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result)] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testTournament_2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result)] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testTournament_3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result)] == self.runner_3)
