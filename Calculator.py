number1 = input("please input the first value")
notation = input("please select the preffered notation")
number2 = input("please input in your second value")

if notation == '*' :
    multiply_ans = int(number1) * int(number2)
    print ( "The answer is " + str(multiply_ans))
elif notation == '/' :
    Divison_ans = int(number1) / int(number2)
    print ("The answer is " + str(Divison_ans))
elif notation == '+' :
    Addition_ans = int(number1) + int(number2)
    print ("The answer is " + str(Addition_ans))
elif notation == '-' :
    Subtraction_ans = int(number1) - int(number2)
    print ("The answer is " + str(Subtraction_ans))
