class Stack:
  def __init__(self):
    self.list = []

  def pop(self):
    return self.list.pop()

  def push(self, data):
    self.list.append(data)

  def length(self):
    return len(self.list)

  def print_stack(self):
    print([str(x) for x in self.list])

def calculate_rpn(input):
  # Declare an empty stack
  stack = Stack().list
  # Split the string input on spaces
  inputs = input.split(' ')
  # Iterate through the input
  print(inputs)
  for i in inputs:
    # Check if the item is an operator or not
    ops = ['+','-','*','/','^','%']
    if i not in ops:
      # If number: Save for later (Push to stack)
      stack.append(float(i))
      print(stack)
    if i in ops and len(stack) > 1:
      a = stack.pop()
      b = stack.pop()
      # If operator: Solve for the operator with the last two numbers (Two pops, then a push)
      if i == '+':
        stack.append(b+a)
        print(stack)
      elif i == '-':
        stack.append(b-a)
        print(stack)
      elif i == '*':
        stack.append(b*a)
        print(stack)
      elif i == '/':
        stack.append(b/a)
        print(stack)
      elif i == '^':
        stack.append(b**a)
        print(stack)
      elif i == '%':
        stack.append(b%a)
        print(stack)
  # return the one item remaining on the stack
  print(stack[0])
  return stack[0]
    
  
# Basic Test
if calculate_rpn('2 4 +') == 6: print('✅ Passing for "2 4 +"')
else: print('🚫 Not passing for "2 4 +"')

# Test for single number as input
if calculate_rpn('2') == 2: print('✅ Passing for "2"')
else: print('🚫 Not passing for "2"')

# Test for subtraction
if calculate_rpn('2 1 -') == 1: print('✅ Passing for "2 1 -"')
else: print('🚫 Not passing for "2 1 -"')

# Test for 2-digit numbers
if calculate_rpn('12 4 *') == 48: print('✅ Passing for "12 4 *"')
else: print('🚫 Not passing for "12 4 *"')

# Test multiple calculations
if calculate_rpn('12 381 + 111 -') == 282: print('✅ Passing for "12 381 + 111 -"')
else: print('🚫 Not passing for "12 381 + 111 -"')

# Test multiple calculations
if calculate_rpn('1 2 3 + 4 * +') == 21: print('✅ Passing for "1 2 3 + 4 * +"')
else: print('🚫 Not passing for "1 2 3 + 4 * +"')

# Test multiple calculations with exponents
if calculate_rpn('3 5 ^ 3 - 4 /') == 60: print('✅ Passing for "3 5 ^ 3 - 4 /"')
else: print('🚫 Not passing for "3 5 ^ 3 - 4 /"')

# Test multiple calculations with exponents and modulus
if calculate_rpn('3 5 ^ 3 - 4 / 8 % 2 4 ^ +') == 20: print('✅ Passing for "3 5 ^ 3 - 4 / 8 % 2 4 ^ +"')
else: print('🚫 Not passing for "3 5 ^ 3 - 4 / 8 % 2 4 ^ +"')