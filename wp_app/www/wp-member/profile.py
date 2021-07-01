import frappe

def get_context(context):

    try:
        docname = frappe.form_dict.docname
        context.opmember = frappe.get_doc("Oriflame Premium Member", docname)


        # opmember_list = frappe.db.sql(f"""
        #             SELECT name, name1, designation, profile_image, cover_image, short_bio_data, about_me,
        #             email, mobile_number FROM `tabOriflame Premium Member` WHERE sponser_id='{context.opmember.sponser_id}' ORDER BY creation DESC;""",
        #     as_dict=True)
        # context.opmember_list = opmember_list

        opm_blog = frappe.db.sql(f"""
                            SELECT name, creation, owner, title, blog_category, blogger, route,
                            read_time, published_on, blog_intro, content FROM `tabBlog Post` WHERE blogger='{context.opmember.blogger}' ORDER BY creation DESC;""",
                                      as_dict=True)
        context.opm_blog = opm_blog

    except Exception as e:
        frappe.local.flags.redirect_location = '/404'
        raise frappe.Redirect

        return context
