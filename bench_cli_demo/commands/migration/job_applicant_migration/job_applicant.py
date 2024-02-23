import frappe
import click
from ..db import get_job_applicant_data
from ..site import init_site_decorate
from .job_opening import import_job_opening, get_job_opening_exits
from .interview_round import import_interview_round, get_interview_round_exits


@click.command("import-job-applicant")
@init_site_decorate
def import_job_applicants():
    for _ in range(3):
        for job_applicant_data in get_job_applicant_data():

            job_opening = get_job_opening_exits(job_applicant_data["job"])

            if not job_opening:
                job_opening = import_job_opening(job_applicant_data["job"])

            job_applicant = frappe.get_doc(
                {
                    "doctype": "Job Applicant",
                    "email_id": job_applicant_data["email"],
                    "applicant_name": job_applicant_data["name"],
                    "job_title": job_opening,
                }
            )

            job_applicant.insert()

            if "interviews" in job_applicant_data:
                import_interviews(job_applicant_data["interviews"], job_applicant)

            print(f"Insert Job Applicant: {job_applicant}")

        frappe.db.commit()

    print("All Job Applicants are inserted successfully!")


def import_interviews(interviews, job_applicant):
    if not interviews:
        return

    for interview in interviews:
        interview_round = get_interview_round_exits(interview["round"])

        if not interview_round:
            interview_round = import_interview_round(interview["round"])

        interview = frappe.get_doc(
            {
                "doctype": "Interview",
                "job_applicant": job_applicant.name,
                "scheduled_on": interview["date"],
                "interview_round": interview_round,
                "status": interview["status"],
                "interview_summary": interview["feedback"],
            }
        )

        interview.insert()
