import runner_and_tournament
import unittest


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

    def testTournament_1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result)] == self.runner_3)

    def testTournament_2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result)] == self.runner_3)

    def testTournament_3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result)] == self.runner_3)

# Последнее место занимает самый медлительный участник
    def testTournament_4(self):
        tournament = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        speed_list = {}
        for participant in tournament.participants:
            speed_list.update({participant.speed: participant})
        turtle = speed_list[min(speed_list)]
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result)] == turtle)
