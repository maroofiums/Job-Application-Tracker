from faker import Faker
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone

from applications.models import Company, Application
from interviews.models import Interview


fake = Faker()


def create_companies(user, count=20):
    """
    Create fake companies for a user
    """

    companies = []

    industries = [
        "Software",
        "AI",
        "FinTech",
        "Healthcare",
        "E-commerce",
        "Cyber Security",
        "Cloud",
        "Telecom",
    ]


    for _ in range(count):

        company = Company.objects.create(
            owner=user,
            name=fake.company(),
            website=fake.url(),
            industry=fake.random_element(
                industries
            ),
            location=fake.city(),
        )

        companies.append(company)

    print(
        f"{count} companies created"
    )

    return companies



def create_applications(user, companies, count=50):
    """
    Create fake job applications
    """

    applications = []

    positions = [
        "Machine Learning Engineer",
        "Backend Developer",
        "Python Developer",
        "AI Engineer",
        "Data Scientist",
        "Software Engineer",
        "Django Developer",
        "Data Analyst",
    ]

    locations = [
        "Karachi",
        "Lahore",
        "Islamabad",
        "Remote",
        "Hybrid",
    ]

    statuses = [
        Application.Status.APPLIED,
        Application.Status.SCREENING,
        Application.Status.INTERVIEW,
        Application.Status.OFFER,
        Application.Status.REJECTED,
    ]

    employment_types = [
        Application.EmploymentType.FULL_TIME,
        Application.EmploymentType.INTERNSHIP,
        Application.EmploymentType.CONTRACT,
    ]

    for _ in range(count):

        application = Application.objects.create(
            user=user,

            company=fake.random_element(
                companies
            ),

            position=fake.random_element(
                positions
            ),

            job_url=fake.url(),

            status=fake.random_element(
                statuses
            ),

            employment_type=fake.random_element(
                employment_types
            ),

            location=fake.random_element(
                locations
            ),

            salary_min=fake.random_int(
                min=30000,
                max=100000
            ),

            salary_max=fake.random_int(
                min=120000,
                max=300000
            ),

            applied_at=fake.date_between(
                start_date="-6m",
                end_date="today"
            ),

            deadline=fake.date_between(
                start_date="today",
                end_date="+30d"
            ),

            follow_up_date=fake.date_between(
                start_date="today",
                end_date="+20d"
            ),

            contact_person=fake.name(),
            notes=fake.paragraph(),
        )


        applications.append(application)

    print(
        f"{count} applications created"
    )

    return applications


def create_interviews(user, applications, count=15):
    """
    Create fake interviews
    """

    interviews = []

    interview_types = [
        Interview.InterviewType.PHONE,
        Interview.InterviewType.TECHNICAL,
        Interview.InterviewType.HR,
        Interview.InterviewType.FINAL,
    ]


    for _ in range(count):

        application = fake.random_element(
            applications
        )

        interview = Interview.objects.create(
            application=application,
            user=user,
            interview_type=fake.random_element(
                interview_types
            ),
            date=timezone.now()
            +
            timedelta(
                days=fake.random_int(
                    min=1,
                    max=30
                )
            ),
            interviewer=fake.name(),
            notes=fake.paragraph(),
        )

        interviews.append(interview)

    print(
        f"{count} interviews created"
    )

    return interviews



def seed_database(username="maroof"):

    """
    Main function
    Run this from Django shell
    """

    user = User.objects.get(
        username=username
    )

    companies = create_companies(
        user,
        count=20
    )

    applications = create_applications(
        user,
        companies,
        count=50
    )

    create_interviews(
        user,
        applications,
        count=15
    )

    print(
        "Database seeding completed!"
    )