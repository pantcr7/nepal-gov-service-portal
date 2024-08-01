# Copyright (c) 2024, PP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class UtilityConsumer(Document):
	pass


@frappe.whitelist()
def create_user(consumer, email=None):
	conm = frappe.get_doc("Utility Consumer", consumer)

	first_name = conm.consumer_name
	email = email or conm.email

	user = frappe.new_doc("User")
	user.update(
		{
			"email": email,
			"first_name": first_name,
			"enabled": 1,
			"send_welcome_email": 0,
			"user_type": "Website User",
			"roles": [
				{
					"role": "Utility User",
					"doctype": "Has Role",
					"parentfield": "roles",
					"parenttype": "User",
				}
			],
		}
	)
	user.insert(ignore_permissions=True)

	conm.user_id = user.name
	conm.save(ignore_permissions=True)






	
	return user.name
