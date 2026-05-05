import frappe
import requests

@frappe.whitelist()
def get_data(number):
    r = requests.get(f'https://swapi.py4e.com/api/people/{number}')
    num=r.json()
    return num["name"]