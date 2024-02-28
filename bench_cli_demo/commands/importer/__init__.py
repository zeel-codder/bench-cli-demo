import click
from .job_applicant_import.job_applicant import import_job_applicants
from .helpers.delete import delete_documents


@click.group("rt-import")
def rt_import():
    pass


rt_import.add_command(import_job_applicants)
rt_import.add_command(delete_documents)
