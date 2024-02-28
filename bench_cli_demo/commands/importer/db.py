import random
from faker import Faker
import random


def get_job_applicant_data():
    fake = Faker()

    job_list = [
        "Software Developer",
        "Data Scientist",
        "Business Analyst",
        "Project Manager",
        "DevOps Engineer",
        "Data Engineer",
    ]
    round_list = ["SDE", "DS", "BA", "PM", "DE", "DOE"]

    job_applicant_data = []

    for _ in range(100):
        applicant = {
            "email": fake.email(),
            "name": fake.name(),
            "job": random.choice(job_list),
            "interviews": [
                {
                    "round": random.choice(round_list),
                    "date": fake.date_between(
                        start_date="-1y", end_date="today"
                    ).isoformat(),
                    "status": random.choice(["Cleared", "Rejected", "Pending"]),
                    "feedback": random.choice(["Good", "Average", "Poor"]),
                }
                for _ in range(random.randint(2, 3))
            ],
        }
        job_applicant_data.append(applicant)

    return job_applicant_data
