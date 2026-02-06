import frappe
import json

@frappe.whitelist(allow_guest=True)
def create_student2():
    
    data = frappe.form_dict.get("data")

    
    if not data:
        try:
            data = json.loads(frappe.local.request.get_data())
        except:
            data = None

    if not data:
        frappe.throw("No data received")

    student = frappe.new_doc("Student2")
    student.student_name = data.get("student_name")
    student.age = data.get("age")
    student.mobile_no = data.get("mobile_no")

    
    for row in data.get("courses", []):
        student.append("courses", {
            "course_name": row.get("course_name"),
            "marks": row.get("marks")
        })

    student.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "student": student.name
    }
