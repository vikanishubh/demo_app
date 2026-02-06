import frappe

def before_tests():
    # def before_tests():
    print("Before ALL tests")


def after_tests():
    print("After ALL tests")

def before_test():
    print("Before EACH test")

def after_test():
    print("After EACH test")    