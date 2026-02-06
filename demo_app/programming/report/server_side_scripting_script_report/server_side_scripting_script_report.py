# Copyright (c) 2026, Shubh and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    cs_data = get_cs_data(filters)

    if not cs_data:
        frappe.msgprint(frappe._("No records found"))
        return columns, []

    data = []
    for d in cs_data:
        row = frappe._dict({
            "first_name": d.first_name,
            "dob": d.dob,
            "age": d.age
        })
        data.append(row)

    chart = get_chart_data(data)
    report_summary = get_report_summary(data)

    return columns, data, None, chart, report_summary


def get_columns():
    return [
        {
            "fieldname": "first_name",
            "label": frappe._("First Name"),
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "fieldname": "age",
            "label": frappe._("Age"),
            "fieldtype": "Int",
            "width": 80,
        },
        {
            "fieldname": "dob",
            "label": frappe._("D.O.B"),
            "fieldtype": "Date",
            "width": 120,
        }
    ]


def get_cs_data(filters):
    conditions = get_conditions(filters)
    return frappe.get_all(
        "server side scripting",
        fields=["first_name", "dob", "age"],
        filters=conditions,
        order_by="first_name desc"
    )


def get_conditions(filters):
    conditions = {}
    for key, value in filters.items():
        if value:
            conditions[key] = value
    return conditions


def get_chart_data(data):
    if not data:
        return None

    labels = ["Age ≤ 45", "Age > 45"]

    age_data = {
        "Age ≤ 45": 0,
        "Age > 45": 0,
    }

    for entry in data:
        if entry.age and entry.age <= 45:
            age_data["Age ≤ 45"] += 1
        else:
            age_data["Age > 45"] += 1

    return {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Age Status",
                    "values": [
                        age_data["Age ≤ 45"],
                        age_data["Age > 45"],
                    ],
                }
            ],
        },
        "type": "line",
        "height": 300,
    }


def get_report_summary(data):
    if not data:
        return None

    age_below_45 = 0
    age_above_45 = 0

    for entry in data:
        if entry.age < 45:
            age_below_45 += 1
        else:
            age_above_45 += 1

    return [
        {
            "value": age_below_45,
            "indicator": "Green",
            "label": "Age Below 45",
            "datatype": "Int",
        },
        {
            "value": age_above_45,
            "indicator": "Red",
            "label": "Age Above 45",
            "datatype": "Int",
        }
    ]
