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
def calc(x, y, op):
    operations = {
        '+': x + y,
        '-': x - y,
        '/': x / y,
        '*': x * y,
        '%': x % y,
        '**': x ** y
    }
    return operations[op]
def calculate_rpn(input):
    # Declare an empty stack - secretly a list that we're using like a stack
    stack = Stack()
    # Split the string input on spaces
    input = input.split(' ')
    # Define operators
    ops = ('+', '-', '/', '%', '*', '**')
    # Iterate through the input
    for c in input:
        print('encountered item:', c)
        # Check if the item is an operator or not
        # If operator: Solve for the operator with the last two numbers (Two pops, then a push) 
        if c in ops:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(calc(num2, num1, c))
        # If number: Save for later (Push to stack)
        else: stack.push(float(c))
        print('Stack looks like this now:')
        stack.print_stack()
    # return the one item remaining on the stack
    return stack.pop()