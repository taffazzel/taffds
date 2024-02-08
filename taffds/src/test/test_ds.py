import unittest

from taffds.src.main.ds.ds import datastructure
from array import *

class test_topk(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lib=datastructure

    def test_topK(self):
        list1 = [1, 2, 3, 4, 1, 3, 5, 2, 3, 5, 6, 1, 2, 3, 5, 5, 2]
        return_from_test=datastructure().fun_topk(list1,3)
        self.assertAlmostEqual(return_from_test,[(2,4),(3,4),(5,4)])

    def test_high_low(self):
        list1 = [1, 2, 3, 4, 1, 3, 5, 2, 3, 5, 6, 1, 2, 3, 5, 5, 2]
        return_from_test = datastructure().find_highest_lowest(list1)
        self.assertEqual(return_from_test,(6, 1))

    def test_reveres_array(self):
        array_object=array('i',[17,6,20])
        reveresed_array = datastructure().reverse_array(array_object)
        print(reveresed_array)
        self.assertEqual(reveresed_array,[20,6,17])

    def test_kth_hig_low(self):
        list2 = [5, 7, 1, 0, 8, 2, 3, 10, 11]
        return_from_function=datastructure().find_kth_largest_smallest(list2, 3)
        self.assertEqual(return_from_function,(7, 3))

    def test_frequency_calc(self):
        list1 = [1, 2, 3, 4, 1, 3, 5, 2, 3, 5, 6, 1, 2, 3, 5, 5, 2]
        return_from_list_freq = datastructure().freq_counter1(list1)
        self.assertEqual(return_from_list_freq,{1: 3, 2: 4, 3: 4, 4: 1, 5: 4, 6: 1})

    def test_freq_calc2(self):
        list1 = [1, 2, 3, 4, 1, 3, 5, 2, 3, 5, 6, 1, 2, 3, 5, 5, 2]
        self.assertEqual(datastructure().freq_counter2(list1),{1: 3, 2: 4, 3: 4, 4: 1, 5: 4, 6: 1})

    def test_compression(self):
        list_to_send="AABBBCCCDAABB"
        self.assertEqual(datastructure().compression(list_to_send),"A2B3C3D1A2B2")


