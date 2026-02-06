app_name = "demo_app"
app_title = "Demo App"
app_publisher = "Shubh"
app_description = "It is a demo app"
app_email = "shubhvikani13@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "demo_app",
# 		"logo": "/assets/demo_app/logo.png",
# 		"title": "Demo App",
# 		"route": "/demo_app",
# 		"has_permission": "demo_app.api.permission.has_app_permission"
# 	}
# ]





# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/demo_app/css/demo_app.css"
# app_include_js = "/assets/demo_app/js/demo_app.js"
# demo_app/hooks.py


# include js, css files in header of web template
# web_include_css = "/assets/demo_app/css/demo_app.css"
# web_include_js = "/assets/demo_app/js/demo_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "demo_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "demo_app/public/icons.svg"


# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "demo_app.utils.jinja_methods",
# 	"filters": "demo_app.utils.jinja_filters"
# }



# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "demo_app.utils.before_app_install"
# after_app_install = "demo_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "demo_app.utils.before_app_uninstall"
# after_app_uninstall = "demo_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config



# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes


# Document Events
# ---------------
# Hook on document methods and events


	# "Demo":{
	# 	"before_save":"demo_app.event.before_save",
	# 	"before_insert": "demo_app.event.before_insert",
    #     "validate": "demo_app.event.validate",
    #     "before_save": "demo_app.event.before_save",
    #     "after_insert": "demo_app.event.after_insert",
    #     "on_update": "demo_app.event.on_update",
    #     "on_submit": "demo_app.event.on_submit",
    #     "on_cancel": "demo_app.event.on_cancel",
    #     "on_trash": "demo_app.event.on_trash",
	# }


	
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}


# Scheduled Tasks
# ---------------

scheduler_events = {
    # "cron": {
    #     "* * * * *":[
    #         "demo_app.tasks.cron"
    #     ]
    # },   

	"all": [
		"demo_app.tasks.cron"
	],
	"daily": [
		"demo_app.tasks.daily"
	],
	"hourly": [
		"demo_app.tasks.cron"
	],
	"weekly": [
		"demo_app.tasks.weekly"
	],
	"monthly": [
		"demo_app.tasks.monthly"
	],
}



# Testing
# -------

# before_tests = "demo_app.install.before_tests"


#

# override_doctype_dashboards = {
# 	"Task": "demo_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["demo_app.utils.before_request"]
# after_request = ["demo_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["demo_app.utils.before_job"]
# after_job = ["demo_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------


# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }



# website_error_handlers = {
#     "404": "demo_app.www.error_pages.handle_404"
# }

# doc_events = {
	
# 		
		
# }
##task-2 week 7
override_doctype_class = {
	"Purchase Order":"demo_app.purchase_order.CustomPurchaseOrder"
	
}
		
##task-3 week 7
override_whitelisted_methods = {
    "erpnext.accounts.doctype.sales_invoice.sales_invoice.make_delivery_note":"demo_app.invoice.make_delivery_note"
}









# override_doctype_class = {
#     "ToDo": "demo_app.todo.CustomToDo"
# }





# app_include_js = "/assets/demo_app/js/global.js"
# app_include_css = "/assets/demo_app/css/global.css"


# web_include_js = "/assets/demo_app/js/global.js"
# web_include_css = "/assets/demo_app/css/global.css"
 
# page_js = {"programming-page" : "public/js/global.js"}

# webform_include_js = {
#     "server side scripting": "public/js/global.js"
# }
# webform_include_css = {
#     "server side scripting": "public/css/global.css"
# }

sounds=[
	{
	"name":"shubh",
	"src": "/assets/demo_app/sounds/custom_sound.wav", 
	"volume": 0.9
}
]

# Installation
# ------------

before_install = "demo_app.install.before_install"
after_install = "demo_app.install.after_install"

# Uninstallation
# ------------

before_uninstall = "demo_app.install.before_uninstall"
after_uninstall = "demo_app.install.after_uninstall"


before_migrate = "demo_app.installl.before_migrate"
after_migrate = "demo_app.installl.after_migrate"

before_tests = "demo_app.tests.before_tests"
after_tests = "demo_app.tests.after_tests"

# before_test = "demo_app.tests.before_test"
# after_test = "demo_app.tests.after_test"


##files hook
before_write_file = "demo_app.files.before_write_file"
# write_file = "demo_app.files.write_file"
# delete_file_data_content = "demo_app.files.delete_file_data_content"

# Email Hooks
# override_email_send = "demo_app.email.send"
# get_sender_details = "demo_app.email.get_sender_details"

##Bootinfo
boot_session = "demo_app.boot.boot_session"

##Website Context
website_context = {"custom_greeting":"hello"}
update_website_context = "demo_app.website_context.web_context"

# Website Controller Context
extend_website_page_controller_context = {
    "frappe.www.404": "demo_app.pages.context_404"
}

##website_clear_cache hooks
# website_clear_cache = "demo_app.cache.clear_website_cache"

##website_redirects hooks
website_redirects = [
    {"source": "/compare", "target": "/comparison"}
]

# website_route_rules = [
#     {"from_route": "/sigzen", "to_route": "hello"}
# ]	

# Website Path Resolver
# website_path_resolver = "demo_app.path_resolver.resolve_path"

# Home Pages
# ----------

homepage = "homepage1"
# role_home_page = {
#     "Customer": "orders"
# }

# get_website_user_home_page = "demo_app.website.get_home_page"

portal_sidebar_items = "demo_app.sidebar.get_sidebar_items"

###task
brand_html='<div class="navbar-brand"><img src="/assets/demo_app/images/logo.png" height="200" width="50">Demo App<div>'


# calendars = ["Appointment"]
# doctype_calendar_js = {
#     "Appointment": "public/js/appointment_calendar.js"
# }

###
# mail_footer = "demo_app.mail.get_mail_footer"

# ####session
# on_login = "demo_app.login.successful_login"
# on_session_creation = "demo_app.login.allocate_free_credits"
on_logout = "demo_app.login.clear_user_cache"

# auth_hooks = [
# 	"demo_app.auth.validate"
# ]


fixtures=["Practice2"]

permission_query_conditions = {
    "Demo": "demo_app.permissions.demo_conditions"
}
has_permission = {
    "Demo": "demo_app.permissions.has_demo_permission"
}


####extend class
# extend_doctype_class = {
#     "Address": ["demo_app.address.AddressMixin"]
# }

# override_doctype_class = {
# 	# "ToDo": "custom_app.overrides.CustomToDo"
# }

doc_events = {
	
		"Student1": {
			"validate": "demo_app.programming.doctype.student1.events.validate",
			
		},	
		 "Customer": {
		 
        "after_insert": ["demo_app.customer_event.after_insert","demo_app.customer_event.customer_after_save"],
        "on_update": "demo_app.customer_event.on_update",
		},

		"Item": {
        "before_insert": "demo_app.item.set_serial_batch_series",
		
    },
	###task-1 week 7
	"Sales Order": {
		"before_save": "demo_app.sale_order.before_save",
			
 		}
		
    }


# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "demo_app.event.get_events"
# }

ignore_links_on_delete = [
    "parent"
]


additional_timeline_content = {
   
    "ToDo": ["demo_app.timeline.todo_timeline"]
}

# notification_config = "demo_app.notifications.get_notification_config"



####task3 week 8
doctype_list_js = {
    "Student": "public/js/student_list.js",
    "Customer": "public/js/student_list.js"
}

