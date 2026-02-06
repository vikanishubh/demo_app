import frappe

# def successful_login(login_manager):
#     user = frappe.session.user

#     frappe.msgprint(
#         f"Welcome {user}! Login successful "
#     )

# import frappe

# def allocate_free_credits(login_manager):
#     user = frappe.session.user

#     frappe.log_error(
#         title="SESSION HOOK",
#         message=f"allocate_free_credits ran for {user}"
#     )

#     if user == "Administrator":
#         return

#     frappe.db.set_value(
#         "User",
#         user,
#         "bio",
#         "Free credits allocated on first session"
#     )
# import frappe

def clear_user_cache(login_manager):
    user = frappe.session.user

    # Practical proof
    frappe.log_error(
        title="LOGOUT HOOK",
        message=f"User logged out: {user}"
    )
    frappe.msgprint("succesful logout")

   

