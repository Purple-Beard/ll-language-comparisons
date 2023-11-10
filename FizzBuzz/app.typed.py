# FizzBuzz in Python using print
for i in range(1, 101):
    output: str = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
