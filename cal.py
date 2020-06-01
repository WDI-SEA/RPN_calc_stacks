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
    ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "x": (lambda a, b: a * b),
  "/": (lambda a, b: a / b),
  "%": (lambda a, b: a % b)
}
  # Declare an empty stack
    stack = Stack()
  # Split the string input on spaces
    split = input.split( )
  # Iterate through the input
    for i in split:
    # Check if the item is an operator or not
        if i in ops:
      # If operator: Solve for the operator with the last two numbers (Two pops, then a push) 
            num2 = stack.pop()
            num1 = stack.pop()
            result = ops[i](num1, num2)
            stack.push(result)
      # If number: Save for later (Push to stack)
        else:
            stack.push(float(i))
  # return the one item remaining on the stack
    return stack.pop()

if calculate_rpn('2 4 +') == 6: print('✅ Passing for "2 4 +"')
else: print('🚫 Not passing for "2 4 +"')

print(calculate_rpn('2 4 7 +'))