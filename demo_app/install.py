import frappe

def before_install():
    frappe.log_error("Before install hook triggered!", "DEMO_APP")

def after_install():
    frappe.log_error("After install hook triggered!", "DEMO_APP")

def before_uninstall():
    frappe.log_error("Before uninstall hook triggered!", "DEMO_APP")

def after_uninstall():
    frappe.log_error("After uninstall hook triggered!", "DEMO_APP")
