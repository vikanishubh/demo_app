import frappe
from frappe.model.document import Document

class Main(Document):
    pass


@frappe.whitelist()
def update_sub_items(doctype, name, row_name, sub_items):

    doc = frappe.get_doc(doctype, name)
    for row in doc.items:
        if row.name == row_name:
            row.json_data = sub_items
            break

    doc.save(ignore_permissions=True)

    return "Done"