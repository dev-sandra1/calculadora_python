num1 =int(input("numero 1:  "))  
num2 = int(input("numero 2:  "))

operacion = input("operacion:  ")

if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    print(num1 / num2)
else:
    print("operacion no valida")