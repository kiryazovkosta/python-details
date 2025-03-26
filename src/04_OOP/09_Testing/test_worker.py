from idlelib.debugger_r import restart_subprocess_debugger
from multiprocessing.pool import worker


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

from unittest import TestCase, main
class TestWorker(TestCase):

    
    def test_worker_init(self):
        #Arrange and Act
        worker = Worker('test name', 100, 10)

        # Assert
        self.assertEqual('test name', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_has_no_energy_work_raises(self):
        #Arrange
        worker = Worker('test name', 100, 0)

        #Act
        with self.assertRaises(Exception) as ex:
            worker.work()

        #Assert
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(worker.money, 0)
        self.assertEqual(worker.energy, 0)

        worker.energy = -1
        with self.assertRaises(Exception) as ex:
            worker.work()

        #Assert
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(worker.money, 0)
        self.assertEqual(worker.energy, -1)

    def test_worker_work_decrease_energy_and_increase_money(self):
        worker = Worker("Test", 100, 2)
        worker.work()
        self.assertEqual(100, worker.money)
        self.assertEqual(1, worker.energy)
        worker.work()
        self.assertEqual(200, worker.money)
        self.assertEqual(0, worker.energy)

    def test_worker_rest_increase_energy(self):
        # Arrange
        worker = Worker('test name', 100, 0)
        before_energy = worker.energy

        # Act
        worker.rest()

        # Assert
        self.assertEqual(before_energy, 0)
        self.assertEqual(worker.energy, 1)

    def test_worker_get_info(self):
        worker = Worker("Test", 100, 0)
        result = worker.get_info()
        self.assertEqual("Test has saved 0 money.", result)

if __name__ == "__main__":
    main()