frappe.listview_settings['Customer'] = {
  onload: function(listview) {
    listview.page.add_inner_button(__('My Custom Button'), function() {
      frappe.msgprint(__('Hello from Customer List View'));
    });
  }
};

frappe.listview_settings['Student'] = {
add_fields: ['status'],


get_indicator: function(doc) {
if (doc.status === 'Active') {
return [__('Active'), 'green', 'status,=,Active'];
}
if (doc.status === 'Inactive') {
return [__('Inactive'), 'red', 'status,=,Inactive'];
}
if (doc.status === 'Passed') {
return [__('Passed'), 'blue', 'status,=,Passed'];
}
return [__(doc.status), 'gray', 'status,=,' + doc.status];
}
};

