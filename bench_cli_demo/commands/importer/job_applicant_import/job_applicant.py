import frappe
import click
import csv
from ..site import init_site_decorate
from .job_opening import import_job_opening, get_job_opening_exits
from .interview_round import import_interview_round, get_interview_round_exits
from rich.progress import Progress
from ..helpers.utils import get_logger


"""
Exmple:
bench rt-import import-job-applicant /workspace/frappe-bench/job_applicant_data_20K.csv
"""
@click.command("import-job-applicant")
@click.argument('file_path', type=click.Path(exists=True))
@init_site_decorate
def import_job_applicants(file_path):

    logger = get_logger()

    if not file_path:
        print("Please specify the file path in the common_site_config.json")

    # read the data from the csv file
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header

        counter = 0

        with Progress() as progress:
            task = progress.add_task("[cyan]Importing Job Applicant...", total=20000)

            for row in reader:
                job_applicant_data = {
                    "email": row[0],
                    "name": row[1],
                    "job": row[2],
                    "interviews": [
                        {
                            "round": row[3],
                            "date": row[4],
                            "status": row[5],
                            "feedback": row[6],
                        }
                    ],
                }

                logger.info(f"Importing Job Applicant: {job_applicant_data['email']}")

                import_job_applicant(job_applicant_data)

                progress.update(task, advance=1)

                counter += 1

            frappe.db.commit()

            progress.stop()

            print(f"All Job Applicants({counter}) are inserted successfully!")


def import_job_applicant(job_applicant_data):
    logger = get_logger()

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

    logger.info(f"Job Applicant {job_applicant.name} is inserted successfully!")

    if "interviews" in job_applicant_data:
        import_interviews(job_applicant_data["interviews"], job_applicant)

    frappe.db.commit()


def import_interviews(interviews, job_applicant):
    logger = get_logger()

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

        logger.info(
            f"Interview {interview.name} for {job_applicant.name} is inserted successfully!"
        )
