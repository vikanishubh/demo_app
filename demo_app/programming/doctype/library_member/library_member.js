// Copyright (c) 2026, Shubh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
	validate:function(frm) {
        frm.set_value("full_name",frm.doc.first_name + " " + frm.doc.last_name)

	},
});
