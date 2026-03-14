import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.utils import today

def create_purchase_order(doc, method):

    if doc.material_request_type != "Purchase":
        return

    
    supplier_items = {}

    for item in doc.items:
        supplier = item.custom_supplier

        if not supplier:
            frappe.throw(f"Supplier missing in item {item.item_code}")

        if supplier not in supplier_items:
            supplier_items[supplier] = []
        supplier_items[supplier].append(item)

    
    for supplier, items in supplier_items.items():

        po = get_mapped_doc("Material Request",doc.name,
            {
                "Material Request": {
                    "doctype": "Purchase Order"
                },
                "Material Request Item": {
                    "doctype": "Purchase Order Item"
                }
            }
        )

        po.supplier = supplier
        po.delivery_date=today()

        po.items = []

        for item in items:
            po.append("items", {
                "item_code": item.item_code,
                "qty": item.qty,
                "schedule_date": item.schedule_date,
                "material_request": doc.name,
                "material_request_item": item.name,
            })

        po.insert()
        