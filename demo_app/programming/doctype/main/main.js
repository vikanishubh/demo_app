frappe.ui.form.on('Main Item', {

    form_render(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        render_items_table(frm, row);
    },

    sub_items: function(frm, cdt, cdn) {

        let row = locals[cdt][cdn];

        function open_dialog() {    

            let grid_row = frm.fields_dict[row.parentfield].grid.grid_rows_by_docname[row.name];
            if (grid_row) {
                grid_row.toggle_view(false);
            }

            let data = row.json_data ? JSON.parse(row.json_data) : [];

            let d = new frappe.ui.Dialog({
                title: 'Sub Items Details',
                size: 'large',
                fields: [
                    {
                        fieldname: 'sub_items_table',
                        fieldtype: 'Table',
                        label: 'Sub Items',
                        in_place_edit: true,
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
                            }
                        ]
                    }
                ],
                primary_action_label: 'Save',

                primary_action(values) {

                    let updated_items = values.sub_items_table.map(item => {
                        return {
                            ...item,
                            name: item.name && !item.name.startsWith("row")
                                ? item.name
                                : frappe.utils.get_random(10)
                        };
                    });

                    frappe.call({
                        method: "demo_app.programming.doctype.main.main.update_sub_items",
                        args: {
                            doctype: frm.doc.doctype,
                            name: frm.doc.name,
                            row_name: row.name,
                            sub_items: JSON.stringify(updated_items)
                        },
                        callback: function(r) {

                            row.json_data = JSON.stringify(updated_items);
                            render_items_table(frm, row);

                            d.hide();
                        }
                    });
                }
            });

            d.show();
        }

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
            <tr data-index="${index}">
                <td>${index + 1}</td>

                <td>
                    <span class="view-mode">${item.sub_item_name || ""}</span>
                    <input type="text" class="edit-mode form-control sub-name"
                        value="${item.sub_item_name || ""}" style="display:none;">
                </td>

                <td>
                    <span class="view-mode">${item.quantity || ""}</span>
                    <input type="number" class="edit-mode form-control sub-qty"
                        value="${item.quantity || ""}" style="display:none;">
                </td>

                <td>
                    <button class="btn btn-sm btn-primary edit-subitem" data-index="${index}">Edit</button>
                    <button class="btn btn-sm btn-success save-subitem" data-index="${index}" style="display:none;">Save</button>
                    <button class="btn btn-sm btn-danger delete-subitem" data-index="${index}">Delete</button>
                </td>
            </tr>
        `;
    });

    html += `</tbody></table>`;

    wrapper.html(html);

    // ✅ EDIT CLICK
    wrapper.find(".edit-subitem").click(function () {

        let tr = $(this).closest("tr");

        tr.find(".view-mode").hide();
        tr.find(".edit-mode").show();

        $(this).hide();
        tr.find(".save-subitem").show();
    });

    // ✅ SAVE CLICK
    wrapper.find(".save-subitem").click(function () {

        let index = $(this).data("index");
        let tr = $(this).closest("tr");

        let items = JSON.parse(row.json_data || "[]");

        let name = tr.find(".sub-name").val();
        let qty = tr.find(".sub-qty").val();

        items[index].sub_item_name = name;
        items[index].quantity = qty;   

        frappe.call({
            method: "demo_app.programming.doctype.main.main.update_sub_items",
            args: {
                doctype: frm.doc.doctype,
                name: frm.doc.name,
                row_name: row.name,
                sub_items: JSON.stringify(items)
            },
            callback: function () {

                row.json_data = JSON.stringify(items);
                render_items_table(frm, row);
            }
        });
    });

    // DELETE
    wrapper.find(".delete-subitem").click(function () {
        delete_subitem(frm, row, $(this).data("index"));
    });
}


// ========================
// DELETE
// ========================
function delete_subitem(frm, row, index) {

    let items = JSON.parse(row.json_data || "[]");

    items.splice(index, 1);

    frappe.call({
        method: "demo_app.programming.doctype.main.main.update_sub_items",
        args: {
            doctype: frm.doc.doctype,
            name: frm.doc.name,
            row_name: row.name,
            sub_items: JSON.stringify(items)
        },
        callback: function(r) {

            row.json_data = JSON.stringify(items);
            render_items_table(frm, row);
        }
    });
}