import frappe

def get_sidebar_items(user=None):
   

    user = user or frappe.session.user

   
    items = [
        {"title": "Home", "route": "/", "icon": "home"},
        {"title": "My Orders", "route": "/orders", "icon": "shopping-cart"},
        {"title": "Support Tickets", "route": "/tickets", "icon": "help-circle"},
    ]

    if user == "Administrator":
        items.append({"title": "Admin Panel", "route": "/admin", "icon": "settings"})

    return items
