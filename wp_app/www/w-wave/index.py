import frappe

def get_context(context):

    wwsurvey = frappe.db.sql("""SELECT name, first_name, last_name, referred_by, email_id, mobile_number, creation, pick_a_date FROM `tabWWave` ORDER BY creation DESC;""",
                             as_dict=True)
    context.wwsurvey = wwsurvey

    return  context