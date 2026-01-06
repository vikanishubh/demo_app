import frappe 
import string
import random


def all():
    pass

def cron():
    letters = string.ascii_letters
    note= " ".join(random.choice(letters) for i in range(20))
    new_note= frappe.get_doc({"doctype":"Scheduler","title":note})

    new_note.insert(ignore_permissions=True)
    frappe.db.commit()