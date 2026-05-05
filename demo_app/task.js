frappe.ui.form.on("Contact", {
    refresh(frm) {

        frm.add_custom_button("Click Button", () => {

            let d = new frappe.ui.Dialog({
                title: "Enter Number",
                fields: [
                    {
                        fieldname: 'number',
                        fieldtype: 'Int',
                        label: 'Enter a Number',
                        reqd: 1
                    }
                ],

                primary_action_label: 'Save',

                primary_action(values) {
                    console.log(values.number)

                    frappe.call({
                        method: "demo_app.contact.get_data",
                        args: {
                            number: values.number
                        },
                        callback: function (r) {

                            frm.set_value("first_name", r.message);

                            d.hide();
                        }
                    });
                }
            });

            d.show();
        });
    }
});