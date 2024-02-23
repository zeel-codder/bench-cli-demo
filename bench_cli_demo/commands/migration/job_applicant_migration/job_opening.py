import frappe


def import_job_opening(job_opening):
    if not job_opening:
        return

    job_opening = frappe.get_doc(
        {
            "doctype": "Job Opening",
            "job_title": job_opening,
            "designation": "Software Developer",
        }
    )

    job_opening.insert()

    return job_opening.name


def get_job_opening_exits(job_opening):
    if not job_opening:
        return False

    return frappe.get_value("Job Opening", {"job_title": job_opening}, "name")
