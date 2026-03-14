frappe.ui.form.on('Main Item', {
    form_render(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        render_items_table(frm, row);
    },
    sub_items: function(frm, cdt, cdn) {

        let row = locals[cdt][cdn];
        let data = [];
        if (row.json_data) {
            data = JSON.parse(row.json_data);
        }

        let d = new frappe.ui.Dialog({
            title: 'Sub Items Details ',
            size: 'large',
            fields: [
                {
                    fieldname: 'sub_items_table',
                    fieldtype: 'Table',
                    label: 'Sub Items',
                    in_place_edit: true,
                    data:data,
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
                frappe.model.set_value(
                    cdt,
                    cdn,
                    "json_data",
                    JSON.stringify(values.sub_items_table)
                );
                frm.save();

                d.hide();
            }
        });
           d.show();
    }
});


function render_items_table(frm, row) {

    if (!row) return;

//parentfield:name of child table from parent (items)
    let grid_row = frm.fields_dict[row.parentfield]
        .grid.grid_rows_by_docname[row.name];

    if (!grid_row || !grid_row.grid_form) return;

    let wrapper = grid_row.grid_form.fields_dict.html.$wrapper;

    let items = JSON.parse(row.json_data || "[]");

    let html = `
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>#</th>
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
                    <button class="btn btn-sm btn-primary edit-subitem" data-index="${index}">
                        Edit
                    </button>
                    <button class="btn btn-sm btn-danger delete-subitem" data-index="${index}">
                        Delete
                    </button>
                </td>
            </tr>
        `;
    });

    html += `</tbody></table>`;

    wrapper.html(html);

    //get index where we have clicked in row 
    wrapper.find(".edit-subitem").click(function () {
        edit_subitem(frm, row, $(this).data("index"));
    });

    wrapper.find(".delete-subitem").click(function () {
        delete_subitem(frm, row, $(this).data("index"));
    });
}




function edit_subitem(frm, row, index) {
    
    let items = JSON.parse(row.json_data || "[]");
    let item = items[index];

    let d = new frappe.ui.Dialog({
        title: "Edit Sub Task",
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
            console.log(values);
            Object.assign(item, values);
           
            frappe.model.set_value(
                row.doctype,
                row.name,
                "json_data",
                JSON.stringify(items)
            );
            frm.save();

            d.hide();
            render_items_table(frm, row);
        }
    });

    d.show();
}



function delete_subitem(frm, row, index) {
    
    let items = JSON.parse(row.json_data || "[]");

    items.splice(index, 1);

    frappe.model.set_value(
        row.doctype,
        row.name,
        "json_data",
        JSON.stringify(items)
    );
    frm.save();

    render_items_table(frm, row);
}