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