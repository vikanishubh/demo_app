# Copyright (c) 2026, Shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	pass

@frappe.whitelist()
def get_author_articles(author):
	articles=frappe.db.sql(f"""
	select name from `tabArticle Library` where author='{author}'""",as_dict=1)
	return articles 