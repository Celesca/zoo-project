import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_b1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Error")

    def test_b2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_b3(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
if __name__ == '__main__':
    unittest.main()