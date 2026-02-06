import frappe

@frappe.whitelist(allow_guest=False)
def get_customers_groupwise():
    data = frappe.local.form_dict

    customer_group = data.get("customer_group")   
    status = data.get("status", "Active")
    limit = int(data.get("limit", 50))
        

    
    group_condition = ""
    if customer_group:
        group = frappe.db.get_value(
            "Customer Group",
            customer_group,
            ["lft", "rgt"],
            as_dict=True
        )

        if not group:
            frappe.throw("Invalid Customer Group")

        group_condition = f"""
            AND cg.lft >= {group.lft}
            AND cg.rgt <= {group.rgt}
        """

    query = f"""
        SELECT
            c.name,
            c.customer_name,
            c.customer_group,
            c.territory,
            c.customer_type,
            cg.lft AS group_sequence
        FROM `tabCustomer` c
        INNER JOIN `tabCustomer Group` cg
            ON c.customer_group = cg.name
        WHERE
            c.disabled = 0
            {group_condition}
        ORDER BY
            cg.lft ASC,
            c.customer_name ASC
        LIMIT {limit}
    """

    customers = frappe.db.sql(query, as_dict=True)

    return {
        "status": "success",
        "count": len(customers),
        "data": customers
    }

