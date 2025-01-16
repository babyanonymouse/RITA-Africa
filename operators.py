# if input is float give result as float
def format_result(result):
    if result.is_integer():
        return int(result)
    return result.__round__(2)


# operators and expression
a = float(input("Enter the first Number: "))
b = float(input("Enter the second number: "))
print("---------------------------------------")

addition = a + b
print(f" => addition: {a} + {b} = {format_result(addition)}")
subtraction = a - b
print(f" => subtraction: {a} - {b} = {format_result(subtraction)}")
multiplication = a * b
print(f" => multiplication: {a} * {b} = {format_result(multiplication)}")
modulus = a % b
print(f" => modulus: {a} % {b} = {format_result(modulus)}")
exponentiation = a ** b
print(f" => exponentiation: {a} ** {b} = {format_result(exponentiation)}")
print("---------------------------------------")
