import runner
from unittest import TestCase


class RunnerTest(TestCase):
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
