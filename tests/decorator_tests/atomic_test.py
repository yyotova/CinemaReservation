import unittest
import sys
sys.path.append('.')

from CinemaReservationSystem.decorators.atomic import atomic


class TestAtomic(unittest.TestCase):
    def test_atomic_create_table(self):
        @atomic
        def create_test(con):
            con.cursor.execute('CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name VARCHAR(50));')

        @atomic
        def select_test(con):
            return con.cursor.execute('SELECT * FROM test').fetchone()

        self.assertEqual((1, 'test',), select_test)


if __name__ == '__main__':
    unittest.main()
