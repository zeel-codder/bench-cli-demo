import frappe


def import_interview_round(interview_round):
    if not interview_round:
        return

    interview_round = frappe.get_doc(
        {
            "doctype": "Interview Round",
            "round_name": interview_round
        }
    )

    interview_round.insert(ignore_mandatory=True)

    return interview_round.name


def get_interview_round_exits(interview_round):
    if not interview_round:
        return False

    return frappe.get_value("Interview Round", {"round_name": interview_round}, "name")
