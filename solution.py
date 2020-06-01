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

opers = ['+', '-', '/', '*']

# def calculate_rpn(input):
def calculate_rpn(input):
  # Declare an empty stack
    stacker = Stack()
  # Split the string input on spaces
    splitted = input.split(' ')
  # Iterate through the input
    for x in splitted:
    # Check if the item is an operator or not
        if x in opers:
      # If operator: Solve for the operator with the last two numbers (Two pops, then a push) 
            if x == '+':
                num1=stacker.pop()
                num2=stacker.pop()
                result = num1 + num2
                stacker.push(result)
            elif x == '-':
                num1=stacker.pop()
                num2=stacker.pop()
                result = num2 - num1
                stacker.push(result)
            elif x == '/':
                num1=stacker.pop()
                num2=stacker.pop()
                result = num2 / num1
                stacker.push(result)
            elif x == '*':
                num1=stacker.pop()
                num2=stacker.pop()
                result = num2 * num1
                stacker.push(result)
      # If number: Save for later (Push to stack)
        else:
            stacker.push(int(x))
  # return the one item remaining on the stack
    stacker.print_stack()
    return stacker.pop()
  



