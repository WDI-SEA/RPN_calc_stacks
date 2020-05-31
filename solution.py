def calculate_rpn(input):
    print('You called the function!')
    bin = []
    operators = ['+', '-', '/', '*']
    split_input = input.split()
    print(split_input)
    # def recursive_calculate(split_input):
    #     if len(split_input) == 1:
    #         return split_input
    #     else:
    for i in range(len(split_input)):
        new_input = split_input
        print(new_input, 'line 9')
        if new_input[i] not in operators:
            bin.append(new_input[i])
            print(bin, 'line 12')
        else:
            print(new_input[i], 'line 14')
            num2 = int(bin.pop())
            num1 = int(bin.pop(-1))
            print(num1)
            print(num2)
            if new_input[i] == '+':
                result = num1 + num2
                print(result)
                bin.append(str(result))
                print(bin, 'line 22')
                # recursive_calculate(bin)
            elif new_input[i] == '-':
                result = num1 - num2
                print(result)
                bin.append(str(result))
                print(bin, 'line 29')
                # recursive_calculate(bin)
            elif new_input[i] == '/':
                result = num1 / num2
                print(str(result))
                bin.append(str(result))
                print(bin, 'line 35')
                # recursive_calculate(bin)
            else:
                result = num1 * num2
                print(result)
                bin.append(str(result))
                print(bin, 'line 41')
                # recursive_calculate(bin)
            

print(calculate_rpn('2 4 +')) 
print(calculate_rpn('2')) 
print(calculate_rpn('2 1 -')) 
print(calculate_rpn('12 4 *')) 
print(calculate_rpn('12 381 + 111 -')) 
print(calculate_rpn('1 2 3 + 4 * +'))        
# Basic Test
# if calculate_rpn('2 4 +') == 6: print('✅ Passing for "2 4 +"')
# else: print('🚫 Not passing for "2 4 +"')

# # Test for single number as input
# if calculate_rpn('2') == 2: print('✅ Passing for "2"')
# else: print('🚫 Not passing for "2"')

# # Test for subtraction
# if calculate_rpn('2 1 -') == 1: print('✅ Passing for "2 1 -"')
# else: print('🚫 Not passing for "2 1 -"')

# # Test for 2-digit numbers
# if calculate_rpn('12 4 *') == 48: print('✅ Passing for "12 4 *"')
# else: print('🚫 Not passing for "12 4 *"')

# # Test multiple calculations
# if calculate_rpn('12 381 + 111 -') == 282: print('✅ Passing for "12 381 + 111 -"')
# else: print('🚫 Not passing for "12 381 + 111 -"')

# # Test multiple calculations
# if calculate_rpn('1 2 3 + 4 * +') == 21: print('✅ Passing for "1 2 3 + 4 * +"')
# else: print('🚫 Not passing for "1 2 3 + 4 * +"')



