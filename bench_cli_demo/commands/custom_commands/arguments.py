import click


@click.command("sum")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
def sum_of_two_numbers(number1, number2):
    print(f"Sum of given two number = {number1+number2}")


@click.command("operation", help="Perform operation on given two numbers")
@click.argument("number1", type=int)
@click.argument("number2", type=int)
@click.option(
    "--type",
    type=click.Choice(["div", "mul", "sub", "sum"]),
    default="sum",
    help="Operation to perform on given two numbers",
)
def operation_of_two_numbers(number1, number2, type):
    if type == "sum":
        result = number1 + number2
    elif type == "sub":
        result = number1 - number2
    elif type == "mul":
        result = number1 * number2
    elif type == "div":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error: Division by zero"

    print(f"{type} = {result}")


"""
Run Command:

1.
bench sum 20 2

2.
bench operation --help
bench operation 12 2 --type div
bench operation 12 2 --type sum
bench operation --type sub 12 2

"""
