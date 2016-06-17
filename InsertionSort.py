import unittest

def sort(arr):
    for idx, val in enumerate(arr):
        pos = idx
        while pos > 0 and arr[pos-1] > val:
            arr[pos] = arr[pos-1]
            pos = pos -1
        arr[pos] = val
            
class TestSorting(unittest.TestCase):
        
    def testSorting(self):
        arr = [4, 81, 3, 5, 2]
        sort(arr)
        self.assertEqual(arr, [2, 3, 4, 5, 81])
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSorting)
    unittest.TextTestRunner(verbosity=2, buffer=False).run(suite)