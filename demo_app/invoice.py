import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_delivery_note as core_make_delivery_note

@frappe.whitelist()
def make_delivery_note(*args, **kwargs):
    dn = core_make_delivery_note(*args, **kwargs)
    source_invoice = kwargs.get("source_name") or args[0]
    
    frappe.db.set_value(
        "Sales Invoice",
        source_invoice,
        "custom_special_note",
        "Thank you for your business!"
    )

    
    return dn
