# Stack Class
class Stack:
    def __init__(self):     self.list = []
    def pop(self):          return self.list.pop()
    def push(self, data):   self.list.append(data)
    def length(self):       return len(self.list)
    def print_stack(self):  print([str(x) for x in self.list])

# Create a function that takes in an RPN equation and returns the result
def calculate_rpn(input):
    input = input.split(' ')
    if len(input) % 2 != 1: return None     # The length should always be odd since there is alwasy 1 more number than operation
    stack = Stack()
    calculations = {
        '+':    add,
        '-':    subtract,
        '*':    multiply,
        '/':    divide,
        '**':   exponent
    }
    for each in input:
        try:    stack.push(float(each))
        except: stack.push(calculations[each](stack.pop(),stack.pop()))
    if stack.length() != 1: return None     # Done correctly, there should only be one element left in the list
    return stack.pop()

"""
Calculation Functions
    At first I tried creating a library that returned the correct calculations.
    However, it kept breaking and I eventually realized why:
        Since the calculation was defined in the library, it was evaluating each even of them upon creation.
        It broke on test 5 because it calculated 12 ** 381 which overflowed, even though it wasn't getting returned.
    I tried using the Math module, but it didn't have functions for the simpler calculations.
        Instead of using math for some and not others, I decided to keep it uniform and created functions for each.
        I kept the dictionary, but moved it into the main function and had it reference my calculation function instead.
    I'm not sure if it's the driest, but it is the most scalable.
        I can use this system to build any 2 argument operation that doesn't inherently break python
"""
def add     (num2,num1):    return num1 + num2
def subtract(num2,num1):    return num1 - num2
def multiply(num2,num1):    return num1 * num2
def divide  (num2,num1):    return num1 / num2
def exponent(num2,num1):    return num1 ** num2


"""
Test Cases
"""
# 1. Basic Test
if calculate_rpn('2.5 4.5 +') == 7: print('✅ Passing for "2 4 +"')
else: print('🚫 Not passing for "2 4 +"')

# 2. Test for single number as input
if calculate_rpn('2') == 2: print('✅ Passing for "2"')
else: print('🚫 Not passing for "2"')

# 3. Test for subtraction
if calculate_rpn('2 1 -') == 1: print('✅ Passing for "2 1 -"')
else: print('🚫 Not passing for "2 1 -"')

# 4. Test for 2-digit numbers
if calculate_rpn('12 4 *') == 48: print('✅ Passing for "12 4 *"')
else: print('🚫 Not passing for "12 4 *"')

# 5. Test multiple calculations
if calculate_rpn('12 381 + 111 -') == 282: print('✅ Passing for "12 381 + 111 -"')
else: print('🚫 Not passing for "12 381 + 111 -"')

# 6. Test multiple calculations
if calculate_rpn('1 2 3 + 4 * +') == 21: print('✅ Passing for "1 2 3 + 4 * +"')
else: print('🚫 Not passing for "1 2 3 + 4 * +"')

# 7. Test for exponents
if calculate_rpn('2 2 2 + **') == 16: print('✅ Passing for "2 2 2 + **"')
else: print('🚫 Not passing for "2 2 2 + **"')