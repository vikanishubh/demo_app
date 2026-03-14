import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():
    field = {
        "fieldname": "age",
        "label": "Age",
        "fieldtype": "Int",
        "insert_after": "demo_field"
    }

    create_custom_field("Demo", field)