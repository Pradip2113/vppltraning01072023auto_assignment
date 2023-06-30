# Copyright (c) 2023, Abhishek Chougule and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date

def cron():
	
	today = date.today()
	print("Today's date:", today)

	data = frappe.db.get_list("Auto Shift Assignment", fields=["name", "start_date", "end_date", "status", "employee_group", "company", "shift_type"], filters={"status": 'Active', "start_date": str(today)})

	for eg in data:
		emp = frappe.db.get_list("Employee", fields=["name", "employee_group", "employee_name"], filters={"employee_group": str(eg.employee_group)})
		
		for e in emp:
			# Retrieve Shift Assignment records for the given employee
			sa = frappe.db.get_list('Shift Assignment', fields=["name", "start_date", "end_date", "status", "employee", "company", "shift_type"], filters={"employee": e.name})

			employee_assigned = False
			for k in sa:
				if e.employee_name == k.employee:
					frappe.db.set_value("Shift Assignment", k.name, "shift_type", eg.shift_type)
					frappe.db.set_value("Shift Assignment", k.name, "start_date", eg.start_date)
					frappe.db.set_value("Shift Assignment", k.name, "end_date", eg.end_date)
					employee_assigned = True
					break
			
			if not employee_assigned:
				new_doc = frappe.new_doc('Shift Assignment')
				new_doc.employee = e.employee_name
				new_doc.employee_name = e.employee_name
				new_doc.shift_type = eg.shift_type
				new_doc.start_date = eg.start_date
				new_doc.end_date = eg.end_date
				new_doc.insert(ignore_permissions=True)
	

class AutoShiftAssignment(Document):
	pass
