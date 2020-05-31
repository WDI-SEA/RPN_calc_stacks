def calculate_rpn(input):
    print('You called the function!')
    bin = []
    operators = ['+', '-', '/', '*']
    split_input = input.split()
    print(split_input)
    # def recursive_calculate(split_input):
    #     if len(split_input) <= 1:
    #         return split_input
    #     else:
    for i in range(len(split_input)):
        print(split_input, 'line 9')
        if split_input[i] not in operators:
            bin.append(split_input[i])
            print(bin, 'line 12')
        else:
            print(split_input[i], 'line 14')
            num2 = int(bin.pop(i - 1))
            num1 = int(bin.pop(i -2))
            print(num1)
            print(num2)
            if split_input[i] == '+':
                result = num1 + num2
                print(result)
                bin.append(str(result))
                print(bin, 'line 22')
                continue
                # recursive_calculate(bin)
            elif split_input[i] == '-':
                result = num1 - num2
                print(result)
                bin.append(str(result))
                print(bin, 'line 29')
                continue
                #recursive_calculate(bin)
            elif split_input[i] == '/':
                result = num1 / num2
                print(str(result))
                bin.append(str(result))
                print(bin, 'line 35')
                continue
                #recursive_calculate(bin)
            else:
                result = num1 * num2
                print(result)
                bin.append(str(result))
                print(bin, 'line 41')
                continue
                #recursive_calculate(bin)
            
            

print(calculate_rpn('2 2 3 4 * *'))


