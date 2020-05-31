def calculate_rpn(input):
    input = input.split(' ')
    calculations = {"+", "-", "*", "/"}
    stack = []
    for each in input:
        if each not in calculations:
            stack.append(int(each))
        elif each == "+":
            stack.append((stack.pop() + stack.pop()))
        elif each == "-":
            stack.append((stack.pop() - stack.pop()) * - 1)
        elif each == "*":
            stack.append((stack.pop() * stack.pop()))
        elif each == "/":
            stack.append((stack.pop() / stack.pop()))

    return stack[0]

# print(calculate_rpn('2 4 *'))
if calculate_rpn('2 4 +') == 6: print('✅ Passing for "2 4 +"')
else: print('🚫 Not passing for "2 4 +"')

# # Test for single number as input
if calculate_rpn('2') == 2: print('✅ Passing for "2"')
else: print('🚫 Not passing for "2"')

# # Test for subtraction
if calculate_rpn('2 1 -') == 1: print('✅ Passing for "2 1 -"')
else: print('🚫 Not passing for "2 1 -"')



#############################################################
## tests to make sure a negative subtraction remains negative
#############################################################
if calculate_rpn('1 2 -') == -1: print('✅ Passing for "1 2 -"')
else: print('🚫 Not passing for "2 1 -"')



# # Test for 2-digit numbers
if calculate_rpn('12 4 *') == 48: print('✅ Passing for "12 4 *"')
else: print('🚫 Not passing for "12 4 *"')

# # Test multiple calculations
if calculate_rpn('12 381 + 111 -') == 282: print('✅ Passing for "12 381 + 111 -"')
else: print('🚫 Not passing for "12 381 + 111 -"')

# # Test multiple calculations

if calculate_rpn('1 2 3 + 4 * +') == 21: print('✅ Passing for "1 2 3 + 4 * +"')
else: print('🚫 Not passing for "1 2 3 + 4 * +"')