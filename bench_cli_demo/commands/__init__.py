from .custom_commands.hello_world import hello_world
from .custom_commands.arguments import sum_of_two_numbers, arithmetic
from .custom_commands.group import calculator
from .custom_commands.db import insert_todo

from .importer import rt_import

commands = [
    hello_world,
    sum_of_two_numbers,
    arithmetic,
    calculator,
    insert_todo,
    rt_import,
]
