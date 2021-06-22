import csv

from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from projects.models import Project
from categories.models import Category, Subcategory
from locations.models import Location
from creators.models import Creator


def convert_timestamp_to_datetime(timestamp: str):
    return datetime.fromtimestamp(int(timestamp), tz=timezone.utc)


class Command(BaseCommand):
    help = "Populate Database"

    def add_arguments(self, parser):
        parser.add_argument("projects_path", help="Projects File Path")

    def handle(self, *args, **kwargs):
        project_path = kwargs["projects_path"]


        with open(project_path) as file:
            project_data = csv.DictReader(file, delimiter=",")

            current_row_count = 0
            total_row_count = sum(1 for row in file)

            file.seek(0)

            print("Seed Started...")

            for row in project_data:

                category = Category.objects.get_or_create(
                    name=row["category_name"],
                )[0]

                subcategory = Subcategory.objects.get_or_create(
                    name=row["subcategory"],
                    category=category,
                )[0]

                location = Location.objects.get_or_create(
                    name=row["location_name"],
                    localized_name=row["location_localized_name"],
                    country_full=row["location_expanded_country"],
                    country=row["location_country"],
                    state=row["location_state"],
                )[0]

                creator = Creator.objects.get_or_create(
                    name=row["creator_name"], slug=row["creator_slug"]
                )[0]

                Project.objects.get_or_create(
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
                    subcategory=subcategory,
                    location=location,
                    creator=creator,
                )

                current_row_count += 1

                if current_row_count % (total_row_count // 100) == 0:
                    row_percentage = round((current_row_count / total_row_count) * 100, 2)
                    self.stdout.write(f"\tProcessed { row_percentage }% of {total_row_count} lines")
