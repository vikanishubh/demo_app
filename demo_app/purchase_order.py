from erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder
import frappe

class CustomPurchaseOrder(PurchaseOrder):
    def validate(self):
        super().validate()
        if not self.delivery_date:
            frappe.throw("Expected Delivery Date is required.")