import click

@click.command("hello-world")
def hello_world():
    print("Hello, world!")


"""
Run Command:

bench hello-world
"""