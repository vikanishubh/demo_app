frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'My Page',
		single_column: true
	});
	page.set_title('My Page')
	page.set_indicator('Done','red')
	let $btn=page.set_primary_action('New',()=>frappe.msgprint("Clicked New"),'octicon octicon-plus')

	page.add_menu_item('Send Email',()=>frappe.msgprint("Clicked Send Email"))

	page.add_action_item('Delete',()=>frappe.msgprint("Clicked Delete"))

	let field=page.add_field({
		label:'Status',
		fieldtype:'Select',
		fieldname:'status',
		options:[
			'open',
			'closed',
			'cancelled'
		],
		change(){
			frappe.msgprint(field.get_value());
		}
	});
	// $(frappe.render_template("programming_page",{})).appendTo(page.body);

	$(frappe.render_template("programming_page",{
		data:"Hi Frappe"
	})).appendTo(page.body);

	
}