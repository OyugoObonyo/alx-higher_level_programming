while True:
    x = input("Enter First number: ")
    if x == 'q':
        break
    y = input("Enter Second number: ")
    if y == 'q':
        break
    try:
        int(x) / int(y)
    except ZeroDivisionError:
        print("Don't Divide number by zero")
    else:
        z = int(x) / int(y)
        print(z)  
