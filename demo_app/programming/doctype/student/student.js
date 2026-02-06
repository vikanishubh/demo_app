// Copyright (c) 2026, Shubh and contributors
// For license information, please see license.txt



frappe.ui.form.on("Student", {

    refresh:function(frm){
        frm.add_custom_button("Create Employee",()=>{
            frappe.call({
                method:"demo_app.programming.doctype.student.student.create_employee",
                args: {
                    student_name: frm.doc.name1,
                    date: frm.doc.dob,
                    gender: frm.doc.gender,
                    date_of_joining: frm.doc.enrollement_date


                },
                callback:function(r){
                    frappe.msgprint(__("employee created"))
                }
            })
           
        })
    }
})
// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });
