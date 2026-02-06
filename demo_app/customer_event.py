import frappe


def after_insert(doc, method):
    update_customer_group_count(doc.customer_group)


def on_update(doc, method):
    
    if doc.has_value_changed("customer_group"):
        
        update_customer_group_count(doc.customer_group)
        if doc.get_doc_before_save():
            old_group = doc.get_doc_before_save().customer_group
            if old_group and old_group != doc.customer_group:
                update_customer_group_count(old_group)


def update_customer_group_count(group):
    total = frappe.db.count("Customer", {"customer_group": group})
    frappe.db.set_value("Customer Group", group, "total_customers", total)


def customer_after_save(doc, method):
    if doc.primary_address:
        frappe.msgprint(
            title="Primary Address Selected",
            msg=f"Customer <b>{doc.customer_name}</b> has primary address: <b>{doc.primary_address}</b>.",
            indicator="green"
        )