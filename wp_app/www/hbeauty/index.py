import frappe

def get_context(context):

    hbsurvey = frappe.db.sql("""SELECT name, first_name, last_name, referred_by, email_id, mobile_number FROM `tabHBeauty` ORDER BY creation DESC;""",
                               as_dict=True)
    context.hbsurvey = hbsurvey

    return  context