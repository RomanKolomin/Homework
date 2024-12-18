import logging
import rt_with_exceptions
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            name = rt_with_exceptions.Runner("name", -5)
            for i in range(10):
                name.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(name.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            name = rt_with_exceptions.Runner(123)
            for i in range(10):
                name.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(name.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        name_1 = rt_with_exceptions.Runner("name_1")
        name_2 = rt_with_exceptions.Runner("name_2")
        for i in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")
