# Copyright (c) 2026, Shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
	pass




@frappe.whitelist()
def create_employee(student_name, date, gender, date_of_joining):
    employee = frappe.get_doc({
        "doctype": "Employee",
        "first_name": student_name,
        "gender": gender,
        "date_of_birth": date,
        "date_of_joining": date_of_joining
    })

    employee.insert(ignore_permissions=True)
    frappe.db.commit()

    return employee.name