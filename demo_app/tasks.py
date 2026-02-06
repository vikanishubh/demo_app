import frappe 
import string
import random


# def all():
#     pass

def cron():
    letters = string.ascii_letters
    note= " ".join(random.choice(letters) for i in range(20))
    new_note= frappe.get_doc({"doctype":"Scheduler","title":note})

    new_note.insert(ignore_permissions=True)
    frappe.db.commit()


def all():
    frappe.log_error("Scheduler 'all' executed", "Scheduler Test")

def daily():
    frappe.log_error("Daily task executed", "Scheduler Test")

def hourly():
    frappe.log_error("Hourly task executed", "Scheduler Test")

def weekly():
    frappe.log_error("Weekly task executed", "Scheduler Test")

def monthly():
    frappe.log_error("Monthly task executed", "Scheduler Test")

