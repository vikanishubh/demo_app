import frappe

def get_sender_details(sender, **kwargs):
    frappe.log_error(
        message=f"get_sender_details called with sender={sender}, kwargs={kwargs}",
        title="Test Email Hook"
    )
    return {
        "sender": "support@example.com",
        "sender_name": "Demo App Support"
    }
