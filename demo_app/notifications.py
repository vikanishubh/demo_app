import frappe

def get_notification_config():
    return {
        "for_doctype": {
            "ToDo": {
                "open_count": "demo_app.notifications.get_todo_count"
            }
        }
    }

def get_todo_count():
    return frappe.db.count("ToDo", {
        "status": "Open",
        "priority": "High",
        "allocated_to": frappe.session.user
    })

# ✅ NEW FUNCTION (REAL NOTIFICATION)
def notify_todo_creation(doc, method):
    if doc.status == "Open" and doc.priority == "High":

        # ✅ Create Notification Log (REQUIRED)
        frappe.get_doc({
            "doctype": "Notification Log",
            "subject": "New ToDo Assigned",
            "email_content": f"New ToDo: {doc.name}",
            "for_user": doc.allocated_to,
            "type": "Alert"
        }).insert(ignore_permissions=True)

        # ✅ Trigger bell notification refresh
        frappe.publish_realtime(
            event="notification",
            user=doc.allocated_to
        )