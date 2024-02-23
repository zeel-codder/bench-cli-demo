from .custom_commands.hello_world import hello_world
from .custom_commands.arguments import sum_of_two_numbers, operation_of_two_numbers
from .custom_commands.group import calculator
from .custom_commands.db import insert_todo

commands = [
    hello_world,
    sum_of_two_numbers,
    operation_of_two_numbers,
    calculator,
    insert_todo,
]
