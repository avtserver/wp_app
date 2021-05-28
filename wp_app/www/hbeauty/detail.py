# import frappe
#
# def get_context(context):
#
#     hiddensurvey = frappe.db.sql("""SELECT name, first_name, last_name, referred_by, email_id, mobile_number FROM `tabHBeauty` ORDER BY creation DESC;""",
#                                as_dict=True)
#     context.hiddensurvey = hiddensurvey
#
#     return  context

import frappe
# frappe.get_all(doctype, filters, fields, order_by, start, page_length)

def get_context(context):
    # context = hbdetail
    # frappe.get_all(HBeauty, name, first_name, last_name)
    context.hbdetail = frappe.get_doc("HBeauty","000032")
    return context