import frappe

def demo_conditions(user):
    
    if user == "Administrator":
        return None   

    return f"`tabDemo`.owner = '{user}'"

def has_demo_permission(doc, user):
    
    if user == "Administrator":
        return True

    
    if doc.owner == user:
        return True

    
    return False
