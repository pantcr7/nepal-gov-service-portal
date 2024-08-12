import frappe
from frappe import _

@frappe.whitelist()
def get_user_info():

    if frappe.request.method != "GET":
        frappe.throw(_("Method Not Allowed"), frappe.PermissionError)
    try:
        if not frappe.session.user:
            frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

        user = frappe.get_doc("User", frappe.session.user, ignore_permissions=True)
        roles = frappe.get_roles(frappe.session.user)
        return {
            "user_info": {
                "name": user.first_name,
                "user_image": user.user_image,
                "roles": roles
            }
        }
    except Exception as e:
        frappe.throw(str(e))

import frappe
from frappe import _

@frappe.whitelist()
def get_user_info():
    if frappe.request.method != "GET":
        frappe.throw(_("Method Not Allowed"), frappe.PermissionError)
    try:
        if not frappe.session.user:
            frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

        user = frappe.get_doc("User", frappe.session.user, ignore_permissions=True)
        roles = frappe.get_roles(frappe.session.user)
        return {
            "user_info": {
                "name": user.first_name,
                "user_image": user.user_image,
                "roles": roles
            }
        }
    except Exception as e:
        frappe.throw(str(e))


import frappe
from frappe import _

@frappe.whitelist()
def get_electricity_consumption():
    if frappe.request.method != "GET":
        frappe.throw(_("Method Not Allowed"), frappe.PermissionError)
    try:
        if not frappe.session.user:
            frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

        # Assuming there's a relation between the logged-in user and the consumer
        consumer_name = frappe.get_value("Utility Consumer", {"email": frappe.session.user}, "name")
        
        sql_query_consumption_summary = """
            SELECT 
                COUNT(CASE WHEN status = 'unpaid' THEN 1 END) AS unpaid_bill,
                SUM(CASE WHEN status = 'unpaid' THEN amount ELSE 0 END) AS total_unpaid_amount,
                MAX(CASE WHEN status = 'paid' THEN modified END) AS last_paid_date
            FROM 
                `tabNEA Bill`
            WHERE
                consumer_name = %s
        """
        consumption_summary = frappe.db.sql(sql_query_consumption_summary, (consumer_name,), as_dict=True)
        
        # Ensure last_paid_date shows "Not Paid Yet" if all entries are unpaid
        if not consumption_summary[0].get('last_paid_date'):
            consumption_summary[0]['last_paid_date'] = "Not Paid Yet"
        
        sql_query_electricity_consumption = """
            SELECT 
                name, bill_no, consumer_name, `usage`, status, rate_per_unit, amount
            FROM 
                `tabNEA Bill`
            WHERE
                consumer_name = %s
        """
        electricity_consumption = frappe.db.sql(sql_query_electricity_consumption, (consumer_name,), as_dict=True)

        return {
            "status": "success",
            "code": 200,
            "data": {
                "consumption_summary": consumption_summary[0] if consumption_summary else {},
                "electricity_consumption": electricity_consumption or []
            }
        }
    except Exception as e:
        frappe.throw(str(e))

   