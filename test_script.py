from Python_lab_3 import *

def test_calculate():
    returnedArray = calculate(1000, 12, 8)
    assert len(returnedArray) == 5