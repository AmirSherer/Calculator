import pyautogui as pag
import time
import pytest



# Open Calculate
def open_calc():
    print(pag.position())
    pag.click(60, 1420)
    pag.typewrite("calculator",interval =0.2)
    time.sleep(0.5)
    pag.press("enter")


# Performing an add operation
def add_operation(val1,val2):
    pag.press("6")
    time.sleep(0.5)
    pag.press("+")
    time.sleep(0.5)
    pag.press("6")
    time.sleep(0.5)
    pag.press("=")
    time.sleep(0.5)
    pag.click(803,799)
    total_add = val1 + val2
    return total_add

# Performing a subtraction operation
def subtraction_operation (val1,val2):
    pag.press("9")
    time.sleep(0.5)
    pag.press("-")
    time.sleep(0.5)
    pag.press("4")
    time.sleep(0.5)
    pag.press("=")
    time.sleep(0.5)
    pag.click(803,799)
    total_subtraction = val1 - val2
    return total_subtraction

# Performing a multiplication operation
def multiplication_operation(val1,val2):
    pag.press("5")
    time.sleep(0.5)
    pag.press("*")
    time.sleep(0.5)
    pag.press("5")
    time.sleep(0.5)
    pag.press("=")
    time.sleep(1)
    pag.click(803,799)
    total_multiplication = val1 * val2
    return total_multiplication

open_calc()
time.sleep(1)
Result_add = add_operation(6,6)
assert 6 + 6 == Result_add, "Wrong"

open_calc()
time.sleep(1)
Result_subtraction = subtraction_operation(9,4)
assert 9 - 4 == Result_subtraction, "Wrong"

open_calc()
time.sleep(1)
Result_multiplication = multiplication_operation(5,5)
assert 5 * 5 == Result_multiplication, "Wrong"


