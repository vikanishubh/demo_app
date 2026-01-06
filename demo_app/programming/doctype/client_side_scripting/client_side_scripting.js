// Copyright (c) 2025, Shubh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("client side scripting", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("client side scripting",{
    

   
    // refresh:function (frm){
    //   frappe.throw("hello refresh")
    // }

    // before_load(frm) {
    // frappe.throw("Before load");
    // }

    // onload:function(frm){
    //     frappe.throw("hello onload")
    // }

    // validate:function(frm){
    //     frappe.throw("helloo validate")
    // }

    // before_save:function(frm){
    //     frappe.throw("hello before save")
    // }

    // after_save:function(frm){
    //     frappe.throw("hello after")
    // }

    // before_submit:function(frm){
    //     frappe.throw("hello before submit")
    // }
    
    // on_submit:function(frm){
    //     frappe.throw("hello on submit")
    // }

    // before_cancel:function(frm){
    //     frappe.throw("hello before")
    // }

    // after_cancel:function(frm){
    //     frappe.throw("hello after")
    // }
    

     // enable:function(frm){
    //     frappe.msgprint("helloo enable")
    // }

    // family_member_on_form_rendered:function(frm){
    //     frappe.msgprint("hello family member")
    // }
 
    // helloo:function(frm) {
    //     frappe.msgprint('Button field clicked!');
    // }

    // after_save:function(frm){
    //     frappe.msgprint(__("The full name is {0}",
    //         [frm.doc.first_name+" "+frm.doc.middle_name+" "+frm.doc.last_name]
    //     ))
    //     for(let row of frm.doc.family_member){
    //     frappe.msgprint(__("{0}.the family name is '{1}' and relation is '{2}'",
    //         [row.idx,row.name1,row.relation]
    //     ))
    // }
    // }
     
    // refresh:function(frm){
    //     // frm.set_intro("now you can create new client")

    //     if(frm.is_new()){
    //         frm.set_intro("now you can create new client")
    //     }
    // }

    // validate:function(frm){
    //     // frm.set_value('full_name',frm.doc.first_name+" "+frm.doc.middle_name+" "+frm.doc.last_name)

    //     let row=frm.add_child('family_member',{
    //         name1:"raj",
    //         relation:"father", 
    //         age:"77"
    //     })
    // }


    // enable:function(frm){
    //     // frm.set_df_property("first_name",'reqd',1)

    //     // frm.set_df_property("middle_name",'read_only',1) 

    //     // frm.toggle_reqd('age',1)
    // }

    

    // refresh:function(frm){
    //     // frm.add_custom_button("Click Button",()=>{
    //     //     frappe.msgprint(__("you clicked the button"));
    //     // })

    //     frm.add_custom_button("click Button1",()=>{
    //         frappe.msgprint(__("you click1"))
    //     },'click me')
    //     frm.add_custom_button("click Button2",()=>{
    //         frappe.msgprint(__("you click2"))
    //     },'click me')
    // }


})   

// frappe.ui.form.on("Family Member",{
//     // name1:function(frm){
//     // frappe.msgprint("hello from 'name1' heloooo!")
//     // }

// //     age:function(frm){
// //     frappe.throw("hello from 'age' heloooo!")
// //     }
// })


