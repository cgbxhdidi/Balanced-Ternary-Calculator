import unittest
from bt import *

global memory
memory = 0

class TestBT(unittest.TestCase):

    def tell_about(self, fun, n = None, M_should_be = None, R_should_be = None):
        if n == None and fun() == R_should_be:
            return
        if memory == M_should_be or fun(n) == R_should_be:
            return
        self.fail("please check " + fun.__name__)
                
    def test_bt_to_int(self):
        self.tell_about(bt_to_int, '01N0', R_should_be = 6)

    def test_int_to_bt(self):
        self.tell_about(int_to_bt, 6, R_should_be = '1N0')
        self.tell_about(int_to_bt, 5, R_should_be = '1NN')

    def test_memory_as_int(self):
        global memory
        store('0')
        self.tell_about(memory_as_int, R_should_be = 0)
        store('1NN')
        self.tell_about(memory_as_int, R_should_be = 5)

    def test_memory_as_bt(self):
        global memory
        store('0')
        self.assertEqual(memory_as_bt(), '0')
        store('1NN')
        self.assertEqual(memory_as_bt(), '1NN')

    def test_add(self):
        global memory
        store('1')
        self.tell_about(add, '1', M_should_be = 6)
        self.tell_about(add, '001N', M_should_be = 8)

    def test_subtract(self):
        global memory
        store('1')
        self.tell_about(subtract, '001N', M_should_be = 6)
        self.tell_about(subtract, '1', M_should_be = 5)

    def test_multiply(self):
        global memory
        store('1NN')
        self.tell_about(multiply, '1', M_should_be = 5)
        self.tell_about(multiply, '1NN', M_should_be = 25)

    def test_divide(self):
        global memory
        store(int_to_bt(25))
        self.tell_about(divide, '001N', M_should_be = 12)
        with self.assertRaises(Exception):
            divide('0')

    def test_remainder(self):
        global memory
        store(int_to_bt(12))
        self.tell_about(remainder, '1NN', M_should_be = 2)
        self.assertRaises(Exception, remainder, '0')

    def test_negate(self):
        global memory
        store(int_to_bt(2))
        self.tell_about(negate, M_should_be = -2)

    def test_store(self):
        global memory
        self.tell_about(store, '1N1', M_should_be = 7)

    def test_evaluate(self):
        global memory
        self.tell_about(evaluate, '=1NN1 + N01*1N', R_should_be = '1NN1')
        self.tell_about(evaluate, '0', R_should_be = "Equation not right")
        self.tell_about(evaluate, '=1=1=', R_should_be = "Equation not right")
        self.tell_about(evaluate, '=1+1+3', R_should_be = "Equation not right")
        self.tell_about(evaluate, '11+11', R_should_be = "Equation not right")       
        
unittest.main()
