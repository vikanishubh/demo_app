import frappe
from frappe.model.document import Document


import frappe

class AddressMixin(Document):
    def validate(self):
        frappe.throw(
            "jnfsn"
        )
        # Log a test message instead of showing a popup
        # frappe.log_error(
        #     message=f"AddressMixin after_save triggered for Address: {self.get('name')}",
        #     title="Mixin Test"
        # )


