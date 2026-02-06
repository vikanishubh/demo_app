import frappe

def before_migrate():
    print("Before migrate hook triggered!")

def after_migrate():
    print("After migrate hook triggered!")
    
    
    
