import click

"""
Run Command:

bench hello-world
"""


@click.command("hello-world")
def hello_world():
    print("Hello, world!")

