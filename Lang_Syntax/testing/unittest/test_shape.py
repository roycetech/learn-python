import unittest

from shape import Shape

class ShapeTest(unittest.TestCase):
    
    def setUp(self):
        self.out = Shape()

    def test_get_shape_by_name(self):        
        self.out.add('square', 'Four equal sides')
        self.assertEqual('Four equal sides', self.out.get('square'))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.out.get('square')



if __name__ == '__main__':
    unittest.main()