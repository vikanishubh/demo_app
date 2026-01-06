# Copyright (c) 2026, Shubh and contributors
# For license information, please see license.txt

# Copyright (c) 2026, Shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):

    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            article = frappe.get_doc("Article Library", self.article)
            article.status = "Issued"
            article.save()

        elif self.type == "Return":
            self.validate_return()
            article = frappe.get_doc("Article Library", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article Library", self.article)
        if article.status == "Issued":
            frappe.throw("This article is already issued.")

    def validate_return(self):
        self.validate_membership()
        article = frappe.get_doc("Article Library", self.article)
        if article.status == "Available":
            frappe.throw("This article is not issued yet.")

    def validate_membership(self):
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<=", self.date),
                "to_date": (">=", self.date),
            }
        )

        if not valid_membership:
            frappe.throw(
                "No valid membership found for this member on the transaction date."
            )
