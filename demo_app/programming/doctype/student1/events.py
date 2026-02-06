import frappe

def validate(doc, method):
    total = 0
    max_total = 0

    for row in doc.subject:
        total += row.marks or 0
        max_total += row.max_marks or 0

    if max_total > 0:
        doc.custom_percentage = round((total / max_total) * 100, 2)

        if doc.custom_percentage < 33:
            doc.custom_status = "Fail"
        elif doc.custom_percentage <= 50:
            doc.custom_status = "Pass"
        else:
            doc.custom_status = "Excellent"
