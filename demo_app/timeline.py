import frappe

def todo_timeline(doctype, docname):
    doc = frappe.get_doc(doctype, docname)

    if doc.status == "Closed":
        return [
            {
                "icon": "check",
                "label": "ToDo Status",
                "content": "<b style='color:green'>✔ This ToDo is completed</b>"
            }
        ]

    return []
