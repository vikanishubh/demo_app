# Copyright (c) 2026, Shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student2(Document):
	def validate(self):
		doc = frappe.get_doc('Student2', '1au39le6nv')
		for row in doc.get('courses'):
			frappe.msgprint(frappe._("{0}.course name is '{1}' and marks is '{2}'").format(row.idx,row.course_name,row.marks))
