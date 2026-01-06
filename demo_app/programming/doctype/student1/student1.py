# Copyright (c) 2025, Shubh and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Student1(Document):
	def validate(self):
		self.percentage_calculation()
	def percentage_calculation(self):
		total=0
		max_total=0

		for row in self.get('subject'):
			total=total+row.marks
			max_total=max_total+row.max_marks

			if max_total>0:
				self.percentage=(total/max_total)*100	
