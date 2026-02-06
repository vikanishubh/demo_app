import frappe

def context_404(context):
    frappe.log_error("404 CONTEXT LOADED", "DEBUG 404")
    context.custom_message = "Oops! This page does not exist."
    return context
 
