
import frappe

def before_write_file(file_size=None, **kwargs):
    frappe.throw(f"not allowed {file_size}")
    # frappe.log_error("sfssss","cscs")
    

    
  
