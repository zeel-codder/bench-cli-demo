import frappe
import click
from frappe.commands import get_site, pass_context

"""Run Command:
bench use bench-cli-demo.localhost
bench insert-todo --description "This is test todo"
"""


@click.command("insert-todo")
@click.option("--description", default="Test", help="Description for the ToDo")
@click.option(
    "--status",
    default="Open",
    type=click.Choice(["Open", "Closed"]),
    help="Status of the ToDo",
)
@pass_context
def insert_todo(context, description, status):
    try:
        site = get_site(context)

        frappe.init(site=site)
        frappe.connect()

        todo = frappe.get_doc(
            {"doctype": "ToDo", "description": description, "status": status}
        )

        todo.insert()

        print("ToDo inserted successfully")

    except Exception as e:
        print("Please specify --site sitename")
    finally:
        frappe.db.commit()
        frappe.destroy()



