frappe.ui.form.on('Main Item', {

    form_render(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        render_items_table(frm, row);
    },

    // ✅ SUB ITEMS WITH AUTO SAVE ADDED
    sub_items: function(frm, cdt, cdn) {

        let row = locals[cdt][cdn];

        function open_dialog() {

            let grid_row = frm.fields_dict[row.parentfield].grid.grid_rows_by_docname[row.name];
            if (grid_row) {
                grid_row.toggle_view(false);
            }

            let data = [];
            if (row.json_data) {
                data = JSON.parse(row.json_data || "[]");
            }

            let d = new frappe.ui.Dialog({
                title: 'Sub Items Details',
                size: 'large',
                fields: [
                    {
                        fieldname: 'sub_items_table',
                        fieldtype: 'Table',
                        label: 'Sub Items',
                        // in_place_edit: true,
                        data: data,
                        fields: [
                            {
                                fieldtype: 'Data',
                                fieldname: 'sub_item_name',
                                label: 'Sub Item Name',
                                in_list_view: 1
                            },
                            {
                                fieldtype: 'Int',
                                fieldname: 'quantity',
                                label: 'Quantity',
                                in_list_view: 1
                            },
                            {
                            fieldtype: 'Int',
                                fieldname: 'quantity',
                                label: 'Quantity',
                                in_list_view: 1
                        }

                        ]
                    }
                ],
                primary_action_label: 'Save',
                primary_action(values) {

                    let updated_items = values.sub_items_table;
                    
                    frappe.call({
                        method: "demo_app.programming.doctype.main.main.update_sub_items",
                        args: {
                            doctype: row.doctype,
                            name: row.name,
                            sub_items: JSON.stringify(updated_items)
                        },
                        callback: function(r) {
                            // row.json_data = JSON.stringify(updated_items);
                            render_items_table(frm, row);
                            frm.reload_doc();
                            d.hide();
                        }
                    });
                }
            });

            d.show();
        }
      console.log("Is dirty:", frm.is_dirty(), "Is new:", frm.is_new());
        // 🔥 AUTO SAVE BEFORE OPENING DIALOG
        if (frm.is_new() || frm.is_dirty()) {

            frappe.dom.freeze("Saving document...");

            frm.save().then(() => {
                frappe.dom.unfreeze();
                open_dialog();
            });

        } else {
            open_dialog();
        }
    }
});


// ========================
// RENDER TABLE
// ========================
function render_items_table(frm, row) {

    if (!row) return;

    let grid_row = frm.fields_dict[row.parentfield].grid.grid_rows_by_docname[row.name];

    if (!grid_row || !grid_row.grid_form) return;

    let wrapper = grid_row.grid_form.fields_dict.html.$wrapper;

    let items = JSON.parse(row.json_data || "[]");

    let html = `
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Sr.no</th>
                    <th>Sub Item Name</th>
                    <th>Quantity</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
    `;

    items.forEach((item, index) => {
        html += `
            <tr>
                <td>${index + 1}</td>
                <td>${item.sub_item_name || ""}</td>
                <td>${item.quantity || ""}</td>
                <td>
                    <button class="btn btn-sm btn-primary edit-subitem" data-index="${index}">Edit</button>
                    <button class="btn btn-sm btn-danger delete-subitem" data-index="${index}">Delete</button>
                </td>   
            </tr>
        `;
    });

    html += `</tbody></table>`;

    wrapper.html(html);

    wrapper.find(".edit-subitem").click(function () {
        edit_subitem(frm, row, $(this).data("index"));
    });

    wrapper.find(".delete-subitem").click(function () {
        delete_subitem(frm, row, $(this).data("index"));        
    });
}


// ========================
// EDIT SUB ITEM
// ========================
function edit_subitem(frm, row, index) {

    let items = JSON.parse(row.json_data || "[]");
    let item = items[index];

    let d = new frappe.ui.Dialog({
        title: "Edit Sub Item",
        fields: [
            {
                fieldtype: 'Data',
                fieldname: 'sub_item_name',
                label: 'Sub Item Name',
                default: item.sub_item_name
            },
            {
                fieldtype: 'Int',
                fieldname: 'quantity',
                label: 'Quantity',
                default: item.quantity
            }
        ],
        primary_action(values) {

            Object.assign(item, values);

            frappe.call({
                method: "demo_app.programming.doctype.main.main.update_sub_items",
                args: {
                    doctype: row.doctype,
                    name: row.name,
                    sub_items: JSON.stringify(items)
                },
                callback: function(r) {
                    frm.reload_doc();
                    d.hide();
                    render_items_table(frm, row);
                }
            });
        }
    });

    d.show();
}


// ========================
// DELETE SUB ITEM
// ========================
function delete_subitem(frm, row, index) {

    let items = JSON.parse(row.json_data || "[]");

    items.splice(index, 1);

    frappe.call({
        method: "demo_app.programming.doctype.main.main.update_sub_items",
        args: {
            doctype: row.doctype,
            name: row.name,
            sub_items: JSON.stringify(items)
        },
        callback: function(r) {
                
                row.json_data = JSON.stringify(items);
                render_items_table(frm, row);
            
            
        }
    });
}