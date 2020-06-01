#  declare operators
ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b),
  "**": (lambda a, b: a ** b)
}
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
  stack = Stack()
  # Split the string input on spaces
  input = input.split(' ')
  # Iterate through the input
  for i in input:
    # Check if the item is an operator or not
    if i in ops:
      # If operator: Solve for the operator with the last two numbers (Two pops, then a push)
      num2 = stack.pop()
      num1 = stack.pop()
      result = ops[i](num1, num2)
      stack.push(result)
    else:
 # If number: Save for later (Push to stack)
      stack.push(int(i))
  # return the one item remaining on the stack
  return stack.pop()


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
if calculate_rpn('12 4 **') == 20736: print('✅ Passing for "12 4 **"')
else: print('🚫 Not passing for "12 4 **"')

# Test multiple calculations
if calculate_rpn('12 381 + 111 -') == 282: print('✅ Passing for "12 381 + 111 -"')
else: print('🚫 Not passing for "12 381 + 111 -"')

# Test multiple calculations
if calculate_rpn('1 2 3 + 4 * +') == 21: print('✅ Passing for "1 2 3 + 4 * +"')
else: print('🚫 Not passing for "1 2 3 + 4 * +"')
