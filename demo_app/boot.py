import frappe

def boot_session(bootinfo):
   
    
    bootinfo["custom_greeting"] = f"Hello {frappe.session.user}!"
    return bootinfo
