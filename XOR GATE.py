Name = "Yousuf"
Age = 17
input_name = input("please enter your name: ")
input_age = int(input("please enter your age: "))
Value2 = True
if input_name == Name or input_age == Age:
    Value1 = True
if input_name == Name and input_age == Age:
    Value2 = False
if Value1 == True and Value2 == True:
    print(True)
else:
    print(False)
