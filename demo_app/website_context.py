
import frappe

def web_context(context):
    
    if frappe.session.user != "Guest":
        context.test_context = f"Hello {frappe.session.user}!"
    else:
        context.test_context = "Welcome, Guest!"
    
    return context
