def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def quotient(a, b):
    return a / b

def remainder(a, b):
    return a % b

def calculator():
    print("1 = add")
    print("2 = sub")
    print("3 = mul")
    print("4 = quotient")
    print("5 = remainder")
    print("Type 'exit' to quit")
    
    while True:
        choice = input("Select operation from above: ")
        
        if choice == 'exit':
            print("Exiting calculator.")
            break
        
        
        if choice in ['1', '2', '3', '4', '5']:
            a = float(input("a = "))
            b = float(input("b = "))
            

            if choice == '1':
                print(f'{a} + {b} = {add(a, b)}')
            elif choice == '2':
                print(f'{a} - {b} = {sub(a, b)}')
            elif choice == '3':
                print(f'{a} * {b} = {mul(a, b)}')
            elif choice == '4':
                print(f'{a} / {b} = {quotient(a, b)}')
            elif choice == '5':
                print(f'{a} % {b} = {remainder(a, b)}')
    else:
            print("Invalid input")

calculator()
