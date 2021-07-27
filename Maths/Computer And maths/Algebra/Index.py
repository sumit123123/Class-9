Identity = """
1. (x+y)2 = x2 + 2xy + y2
2. (x-y)2 = x2 - 2xy + y2
3. x2-y2 = (x+y)(x-y)
"""

print(Identity)

ide = int(input("Enter the Identity number\n"))

if (ide == 1):
    input_1 = int(input("Enter the number x\n"))
    input_2 = int(input("Enter the number Y\n"))

    print("Value is :-" , int(input_1*input_1)+2*int(input_1)*int(input_2)+int(input_2*input_2))

elif (ide == 2):

    input_1 = int(input("Enter the number x\n"))
    input_2 = int(input("Enter the number Y\n"))

    print("Value is :-",int(input_1*input_1)-2*int(input_1)*int(input_2)+int(input_2*input_2))
else:
    pass