import unittest
from unittest import mock
import ATM


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.user = []

    def tearDown(self):
        self.user = None    
    
    # mock = mock.Mock()
    # mock.side_effect = ['drageon', 1234]
    # @mock.patch('ATM.input', side_effect = ['drageon', 1234])
    @mock.patch('builtins.input', return_value = 'drageon')
    def set_user(self, mock_input):
        # self.user = self.user
        # mock_input.side_effect = ['drageon', 1234]
        # mock_input.return_value = 'drageon'
        test = ATM.Account()
        self.assertEqual(test, 1)
    
    # def test(self):
    #     self.test = 1
    #     self.assertEqual(self.test, 1)

# mock = mock.Mock()
# mock.side_effect = ['drageon', 1234]

if __name__ == '__main__':
    unittest.main()