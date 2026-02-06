import frappe

def before_insert(doc, method):
    frappe.msgprint("HOOK: before_insert")

def validate(doc, method):
    frappe.msgprint("HOOK: validate")

def before_save(doc, method):
    frappe.msgprint("HOOK: before_save")

def after_insert(doc, method):
    frappe.msgprint("HOOK: after_insert")

def on_update(doc, method):
    frappe.msgprint("HOOK: on_update")

def on_submit(doc, method):
    frappe.msgprint("HOOK: on_submit")

def on_cancel(doc, method):
    frappe.msgprint("HOOK: on_cancel")

def on_trash(doc, method):
    frappe.msgprint("HOOK: on_trash")
    