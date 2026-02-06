import frappe

def set_serial_batch_series(doc, method):
    if not doc.item_code or not doc.item_group:
        return

    item_code_prefix = doc.item_code[:2]
    item_group_prefix = doc.item_group[:2]
    prefix = f"{item_group_prefix}-{item_code_prefix}"

    
    doc.has_batch_no = 1
    doc.create_new_batch=1
    doc.has_serial_no = 1

    doc.serial_no_series = f"{prefix}-S-.#####"

    doc.batch_number_series = f"{prefix}-B-.#####"


