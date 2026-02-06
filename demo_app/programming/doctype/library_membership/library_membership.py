# Copyright (c) 2026, Shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from frappe.utils import getdate, today

class LibraryMembership(Document):
	def validate(self):
		today_date = getdate(today())
		if getdate(self.from_date) < today_date or getdate(self.to_date) < today_date or getdate(self.to_date) < getdate(self.from_date):
			frappe.throw("From and To Date cannot be in the past.")
			
	def before_submit(self):
		exists=frappe.db.exists('Library Membership',
		{
		"library_member":self.library_member,
		"docstatus":DocStatus.submitted(),
		"to_date":(">",self.from_date) ,
		"from_date":("<",self.to_date)
		})
		if exists:
			frappe.throw("Library Membership already exists for this member in the given date range.")    
	
		  