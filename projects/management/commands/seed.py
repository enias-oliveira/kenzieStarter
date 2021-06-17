import csv

from datetime import datetime

from django.core.management.base import BaseCommand

from projects.models import Project


def convert_timestamp_to_datetime(timestamp: str):
    return datetime.fromtimestamp(int(timestamp))


class Command(BaseCommand):
    help = "Populate Database"

    def add_arguments(self, parser):
        parser.add_argument("projects_path", help="Projects File Path")

    def handle(self, *args, **kwargs):
        project_path = kwargs["projects_path"]

        with open(project_path) as file:
            project_data = csv.DictReader(file, delimiter=',')
            row = next(project_data)

        project = Project.objects.get_or_create(
            name=row["name"],
            description=row["blurb"],
            backers=row["backers_count"],
            created_at=convert_timestamp_to_datetime(row["created_at"]),
            deadline=convert_timestamp_to_datetime(row["deadline"]),
            goal=float(row["goal"].replace(",", ".")),
            pledged=float(row["pledged"].replace(",", ".")),
            usd_pledged=float(row["usd_pledged"].replace(",", ".")),
            currency=row["currency"],
            launched_at=convert_timestamp_to_datetime(row["launched_at"]),
            state=row["state"],
            state_changed_at=convert_timestamp_to_datetime(
                row["state_changed_at"],
            ),
        )[0]

