import frappe

def get_context(context):

    opmember = frappe.db.sql("""SELECT name, name1, designation,facebook_id, profile_image, about_me, email, mobile_number FROM `tabOriflame Premium Member` ORDER BY creation DESC;""",
                               as_dict=True)
    context.opmember = opmember

    return  context