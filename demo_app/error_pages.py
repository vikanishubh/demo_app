
import frappe

def handle_404(context=None):
    
    if context is None:
        context = {}

   
    context.message = "Oops! The page you are looking for does not exist."
    context.path = frappe.local.request.path

 
    return "404", context
