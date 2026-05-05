import frappe

def capitalize_item_name(doc, method):
    if doc.item_name:
        doc.item_name = doc.item_name.upper()