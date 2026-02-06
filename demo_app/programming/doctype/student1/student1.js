// Copyright (c) 2025, Shubh and contributors
// For license information, please see license.txt



frappe.ui.form.on("Student1", {
    
    validate: function(frm) {
        let rows = frm.doc.subject || [];

        for (let i = 0; i < rows.length; i++) {
            let row = rows[i];

            if ((row.marks|| 0.0) < 0.0) {
                frappe.throw(__("Marks Obtained cannot be negative"));
            }

            if ((row.max_marks || 0.0) < 0.0) {
                frappe.throw(__("Max Marks cannot be negative"));
            }
        }
    }
    })

// frappe.ui.form.on("Student1  Subject",{
//     marks:function(frm,cdt,cdn){
//         let row = locals[cdt][cdn];
//         console.log(row.marks);
//         if (((row.marks)|| 0.0) < 0.0) {
        
//                 frappe.throw(__("Marks Obtained cannot hey negative"));
//         }

// }
// })





    

