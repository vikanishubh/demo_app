// Copyright (c) 2026, Shubh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Demo", {
	validate(frm) {
        frappe.msgprint("helllo how are you")
        frappe.utils.play_sound("shubh")
           
	},
});
