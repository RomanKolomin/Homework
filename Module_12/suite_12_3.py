import tests_12_3
import unittest


tournament_test = unittest.TestSuite()
tournament_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tournament_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournament_test)
