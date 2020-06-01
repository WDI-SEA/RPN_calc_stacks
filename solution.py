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
  stacker = Stack()
  # Split the string input on spaces
  input = input.split(' ')
  print(input)
  operators = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply',
    '/': 'divide'
  }
  # Iterate through the input
  for i in input:
    opCheck = False
    for j in operators.keys():
      if i == j:
        opCheck = True
        print('op')
        if i == '+':
          stacker.push(float(stacker.pop()) + float(stacker.pop()))
        elif i == '-':
          stacker.push(float(stacker.pop()) - float(stacker.pop()))
        elif i == '*':
          stacker.push(float(stacker.pop()) * float(stacker.pop()))
        elif i == '/':
          stacker.push(float(stacker.pop()) / float(stacker.pop()))
        stacker.print_stack()
    if opCheck == False:
      print('non op')
      stacker.push(i)

    # Check if the item is an operator or not
      # If operator: Solve for the operator with the last two numbers (Two pops, then a push) 
      # If number: Save for later (Push to stack)
  # return the one item remaining on the stack

calculate_rpn('1 2 3 + 4 * +')
  

