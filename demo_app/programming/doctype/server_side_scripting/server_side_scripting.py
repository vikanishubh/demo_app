# Copyright (c) 2025, Shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class serversidescripting(Document):
	pass

    # def autoname(self):
    #     self.name = f"{self.first_name} {self.last_name}"

    # def on_change(self):
    #     frappe.msgprint("Document changed")

	# def before_insert(self):
	#     frappe.msgprint("hello before insert")
	
	# def after_insert(self):  
	# 	frappe.msgprint("hello after")

	# def validate(self):
	# 	frappe.msgprint("hello validate")

	# def before_save(self):
	# 	frappe.msgprint("before save")
	
	# def on_update(self):
	# 	frappe.msgprint("on update")

	# def before_submit(self):
	# 	frappe.msgprint("before submit")

	# def on_submit(self):
	# 	frappe.throw("on submit")

	# def on_cancel(self):
	# 	frappe.msgprint("on cancel")

	# def on_trash(self):
	# 	frappe.msgprint("on delete")
	
	# def after_delete(self):
	# 	frappe.msgprint("after delete")
	
    # def validate(self):
	#     frappe.msgprint(frappe._("Hello '{0}'").format(
    #         f"{self.first_name} {self.middle_name} {self.last_name}"
    #     )
    # )

    # def validate(self):
	# 	for row in self.get('family_member'):
	# 	    frappe.msgprint(frappe._("{0}.the family name is '{1}' and relation is {2} and age is {3}").format(row.idx,row.name1,row.relation,row.age))

 
####frappe.get_doc()####
	# def validate(self):
	# 	self.get_document()
	
	# def get_document(self):
	# 	doc=frappe.get_doc('client side scripting',self.client_side_doc)
	# 	frappe.msgprint(frappe._("the first Name is '{0}' and age is '{1}'").format(doc.first_name,doc.age))

	# 	for row in doc.get('family_member'):
	# 		frappe.msgprint(frappe._("{0} the name is {1} and relation is {2} and age is {3}").format(row.idx,row.name1,row.relation,row.age))


# ####frappe.get_last_doc()####
	# def validate(self):
	# 	last_doc=frappe.get_last_doc('client side scripting')
	# 	frappe.msgprint(frappe._("the last document name is '{0}' and first name is '{1}'").format(last_doc.name,last_doc.first_name))

####frappe.get_cached_doc()####
    # def validate(self):
	#     if not self.client_side_doc:
	# 	    frappe.throw("Please select Client Side Scripting document")
	#     doc=frappe.get_cached_doc('client side scripting',self.client_side_doc)
	#     frappe.msgprint(frappe._("the first Name is '{0}' and age is '{1}'").format(doc.first_name,doc.age))

##frappe.rename_doc()##
	# def before_insert(self):
	# 	frappe.rename_doc(
    #     "client side scripting",
    #     "PRE-0063",
    #     "PRE-0065"
    # )
##frappe.new_doc()##
    # def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc=frappe.new_doc("client side scripting")
	# 	doc.first_name="hello"
	# 	doc.middle_name="K"	
	# 	doc.last_name="world"
	# 	doc.age=20
	# 	doc.append("family_member",{ "name1":"raj",
	# 	"relation":"brother",
	# 	"age":22
	# 	})
	# 	doc.insert(ignore_permissions=True)

####frappe.delete_doc()####

	# def validate(self):
	# 	frappe.delete_doc("client side scripting","PRE-0064")

	# def validate(self):
	# 	self.save_document()
	# def save_document(self):
	# 	doc=frappe.new_doc("client side scripting")
	# 	doc.first_name="hello"
	# 	doc.middle_name="K"	
	# 	doc.last_name="world"
	# 	doc.age=20 
	# 	doc.save()


#### delete :doc.delete()####
    # def validate(self):
    #     self.delete_document()

    # def delete_document(self):
    #     doc = frappe.get_doc("client side scripting", "PRE-0030")
    #     doc.delete(ignore_permissions=True)
	


####doc.reload()####
	# def validate(self):
	# 	doc = frappe.get_doc("client side scripting", "PRE-0064")
	# 	doc.db_set('age', 45)
	# 	doc.reload()
	# 	frappe.msgprint(frappe._("the age after db_set is {0}").format(doc.age))


####doc.get_title()####
	# def validate(self):
	# 	doc=frappe.get_doc("client side scripting","PRE-0064")
	# 	title=doc.get_title()
	# 	frappe.msgprint(title)


####doc.add_comment()####
	# def validate(self):
	# 	doc=frappe.get_doc("client side scripting","PRE-0065")
	# 	doc.add_comment("Comment","This is a comment from server side scripting")

####doc.add_tag()####
	# def validate(self):
	# 	doc=frappe.get_doc("client side scripting","PRE-0064")
	# 	doc.add_tag("urgent")

####doc.get_tags()#### 
	# def validate(self):
	# 	doc=frappe.get_doc("client side scripting","PRE-0064")
	# 	tags=doc.get_tags()
	# 	frappe.msgprint(".".join(tags))

##doc.db_set()##
    # def validate(self):
    #     self.db_set_document()

    # def db_set_document(self):
    #     doc = frappe.get_doc("client side scripting", "PRE-0029")
    #     doc.db_set('age', 45)



###get list of record :get_list()##
    # def validate(self):
	#     self.get_list()

    # def get_list(self):
    #     docs = frappe.db.get_list(
    #     'client side scripting',
    #     filters={
    #         'enable': 1
    #     },
    #     fields=['first_name', 'age']
    # )

    #     for d in docs:
    #         frappe.msgprint(
    #         frappe._("The parent name is {0} and age is {1}")
    #         .format(d.first_name, d.age)
    #     )

#####get_value#######
    # def validate(self):
	#     self.get_value()

    # def get_value(self):
	#     first_name,age=frappe.db.get_value('client side scripting','PRE-0053',['first_name','age'])
	#     frappe.msgprint(frappe._("the parent first name is {0} and age is {1}").format(first_name,age))

###########set_value#######
	# def validate(self):
	# 	self.set_value()
	
	# def set_value(self):
	# 	frappe.db.set_value('client side scripting','PRE-0025','age',25)

####db.exists()##
    # def validate(self):
	#     if frappe.db.exists('client side scripting','PRE-00256'):
	# 	    frappe.msgprint("it exists")
	#     else:
	# 	    frappe.msgprint("not exists")

##db.count##
    # def validate(self):
	#     doc_count=frappe.db.count('client side scripting',{'enable':1})
	#     frappe.msgprint(frappe._("the enable document count is {0}").format(doc_count))

###db.sql##
    # def validate(self):
	#     self.sql()
    # def sql(self):
	#     data = frappe.db.sql("""
	# 	select
	# 	first_name,
	# 	age
	# 	from
	# 	`tabclient side scripting`
	# 	where enable=1
	# 	""",as_dict=1)

	#     for d in data:
	# 	    frappe.msgprint(frappe._("the parent name is {0} and age is {1}").format(d.first_name,d.age))

#####frappe.frm_call##
    # @frappe.whitelist()
    # def frm_call(self,msg):
	#     import time
	#     time.sleep(5)
	#     # frappe.msgprint(msg)
	#     self.first_name="shubh"
	#     # return "hi from server side"






	

	