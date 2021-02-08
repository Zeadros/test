def func(pie):
    print(pie + " test")
pog = ["Red", "Yellow", "Blue"]
x = int(input("Num -"))
if(x > 5):
    print("correct")
y = input("Word -")
if(y == "yes"):
    print("good")
else:
    for i in range(len(pog)):
        func(pog[i])