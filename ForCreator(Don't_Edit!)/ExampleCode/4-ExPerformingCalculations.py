print("Welcome to the Simple Text Based Calculator. This calculator was programmed in Python")

no1 = int(input('Input your first number here: '))
no2 = int(input('Input your second number here: '))

print("The four main operations are addition (a), subtraction (s), multiplication (m), and division (d)")

op = input("Which operation would you like to perform: addition(a), subtraction (s), multiplication (m), and division (d)?: ")

if op == 'a': 
  print(no1 + no2)

elif op == 's':
  print(no1 - no2)

elif op == 'm':
  print(no1 * no2)

elif op == 'd':
  print(no1 / no2)

else:
  print("You didn't add an elgible operation symbol")