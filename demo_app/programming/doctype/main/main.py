import frappe
from frappe.model.document import Document

class Main(Document):
    pass

@frappe.whitelist()
def update_sub_items(doctype, name, sub_items=None):
    frappe.db.set_value(doctype, name, "json_data", sub_items)
    frappe.db.commit()
    return "Done"