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

  def getElementAtIndex(self, index):
      return self.list[index] 




def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    if n2 == 0:
       return 'Infinity'
    return n1/n2

def exponent(n1,n2):
    # return pow(n1,n2)
      return n1 ** n2

# Calculator for Reverse Polish Notation, Postfix version
def calculate_rpn(input):
 
    operator={
    "+" : addition,
    "-" : subtraction,
    "*": multiplication,
    "/" : division,
    "**": exponent
    }

    stack =  Stack() 
    # Invalid input if length is even, there has to be one extra number over operators
    inputList = list(input.split(" ")) 
    if(len(inputList)%2 == 0): return None
   
    print('list',inputList) 
    for each in inputList:
      
        if each not in operator:
             stack.push(each)
             
        elif each in operator:
              #  stack.print_stack()
            try: 
                number1 = stack.pop()
                number2 = stack.pop()
                # print(f'{number1},{number2}')
                number1 = float(number1)
                number2 = float(number2)
                result = operator[each](number2, number1)
                stack.push(result)
                # stack.print_stack()
            except: # This catches even expression which has odd length but not in RPN notation
                  print("Input may be invalid and there is pop error")                 

    stack.print_stack()
    # If calculation went well, stack will have only element which is the result of calculation
    if(stack.length!= 0): 
        number = stack.getElementAtIndex(0)
        print("num", float(number))
        return float(number)
    else: # stack empty means no result after calculation
        return None    



# calculate_rpn('10 2 3 - 4 * +')             

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

# Test multiple calculations
if calculate_rpn('1.5 2.5 3.5 + 4 * +') == 25.5: print('✅ Passing for "1.5 2.5 3.5 + 4 * +"')
else: print('🚫 Not passing for "1.5 2.5 3.5 + 4 * +"')

# Test multiple calculations
if calculate_rpn('3 2 2 + **') == 81: print('✅ Passing for "3 2 2 + **"')
else: print('🚫 Not passing 3 2 2 + **')

# Test multiple calculations
if calculate_rpn('3 2 2 + 1 - **') == 27: print('✅ Passing for "3 2 2 + 1 - **"')
else: print('🚫 Not passing 3 2 2 + 1 - **')

# Test multiple calculations
if calculate_rpn('5 6 3 / +') == 7: print('✅ Passing for "5 6 3 / +"')
else: print('🚫 Not passing for "5 6 3 / +"')





