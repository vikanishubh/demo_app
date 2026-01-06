// Copyright (c) 2026, Shubh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Membership", {
	library_member:function(frm) {
        frappe.db.get_doc("Library Member",frm.doc.library_member).then(doc=>{
        frm.set_value("full_name",doc.first_name + " " + doc.last_name)})
    }

});


