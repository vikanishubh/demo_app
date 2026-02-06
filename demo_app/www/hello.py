import frappe

def get_context(context):
    context.name = frappe.form_dict.get("name") or "Guest"
