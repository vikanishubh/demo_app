import frappe

def before_save(doc, method):
    if not doc.get("discount_percentage"):
        doc.discount_percentage = 5