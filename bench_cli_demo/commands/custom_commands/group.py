import click


@click.group("calculator")
def calculator():
    pass


@calculator.command("sum", help="Find sum of two numbers")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
def sum_of_two_numbers(number1, number2):
    print(f"Sum of given two number = {number1+number2}")


@calculator.command("sub", help="Find subtraction of two numbers")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
def sub_of_two_numbers(number1, number2):
    print(f"Subtraction of given two number = {number1-number2}")


@calculator.command("div", help="Find division of two numbers")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
def div_of_two_numbers(number1, number2):
    if number2 == 0:
        return print("Error: Division by zero")
    print(f"Division of given two number = {number1/number2}")


@calculator.command("mul", help="Find multiplication of two numbers")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
def mul_of_two_numbers(number1, number2):
    print(f"Multiplication of given two number = {number1*number2}")


"""
Run Command:

bench calculator
bench calculator sum 20 2
bench calculator sub 20 2
"""