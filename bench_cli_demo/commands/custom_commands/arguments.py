import click


"""
Run Command:

1.
bench sum 20 2

2.
bench arithmetic --help
bench arithmetic 12 2 --operation div
bench arithmetic 12 2 --operation sum
bench arithmetic --operation sub 12 2

"""

@click.command("sum")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
def sum_of_two_numbers(number1, number2):
    print(f"Sum of given two number = {number1+number2}")


@click.command("arithmetic", help="Perform operation on given two numbers")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
@click.option(
    "--operation",
    type=click.Choice(["div", "mul", "sub", "sum"]),
    default="sum",
    help="Operation to perform on given two numbers",
)
def arithmetic(number1, number2, operation):
    if operation == "sum":
        result = number1 + number2
    elif operation == "sub":
        result = number1 - number2
    elif operation == "mul":
        result = number1 * number2
    elif operation == "div":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error: Division by zero"

    print(f"{operation} = {result}")