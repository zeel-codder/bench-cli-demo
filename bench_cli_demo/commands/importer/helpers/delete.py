import frappe
import click
from ..site import init_site_decorate


@click.command("delete-documents")
@click.argument("doctype", type=str)
@init_site_decorate
def delete_documents(doctype):
    documents = frappe.get_all(doctype, filters={})

    for document in documents:
        magic_delete_document(doctype, document["name"])
        frappe.db.commit()

    print("All documents are deleted successfully!")


def magic_delete_document(doctype, doc_name, docs_to_skip=set()):
    doc_key = f"{doctype} {doc_name}"
    if doc_key in docs_to_skip:
        return

    try:
        doc_status = frappe.get_value(doctype, doc_name, "docstatus")

        if doc_status != 0:
            frappe.db.set_value(doctype, doc_name, "docstatus", 0)

        frappe.delete_doc(doctype, doc_name)
    except frappe.LinkExistsError as e:
        docs_to_skip.add(doc_key)

        linked_doctypes = frappe.get_all(
            "DocField",
            filters={"options": doctype, "fieldtype": "Link"},
            fields=["parent", "fieldname"],
        )

        for link_doctype in linked_doctypes:
            linked_docs = frappe.get_all(
                link_doctype["parent"],
                filters={f"{link_doctype['fieldname']}": doc_name},
            )

            for linked_doc in linked_docs:
                magic_delete_document(
                    link_doctype["parent"], linked_doc["name"], docs_to_skip
                )

        frappe.delete_doc(doctype, doc_name, force=True)
        docs_to_skip.remove(doc_key)

    except Exception as e:
        print("Sorry can't delete all documents :))))")
        import sys

        sys.exit()
