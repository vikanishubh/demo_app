import frappe
from frappe.model.document import Document

class CustomToDo(Document):
    def on_update(self):
        # This will run whenever the ToDo is saved, Desk or API
        frappe.log_error(
            message=f"CustomToDo on_update triggered for: {self.get('name')}",
            title="Override Test"
        )
    