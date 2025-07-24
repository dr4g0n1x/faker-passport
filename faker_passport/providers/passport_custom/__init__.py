from datetime import datetime, timedelta
from typing import Optional
from faker.providers import BaseProvider


class Provider(BaseProvider):
    """Custom Passport provider for Faker."""

    passport_number_formats = (
        "??######",
        "########",
        "??#######",
    )

    def passport_number_custom(self) -> str:
        """Generate a random passport number."""
        pattern = self.random_element(self.passport_number_formats)
        return self.bothify(pattern).upper()

    def passport_dob_custom(self, minimum_age: int = 18, maximum_age: int = 90) -> datetime:
        """Generate a date of birth for passport."""
        today = datetime.now()
        min_date = today - timedelta(days=maximum_age * 365)
        max_date = today - timedelta(days=minimum_age * 365)

        return self.generator.date_time_between(
            start_date=min_date, end_date=max_date
        )

    def passport_owner_custom(self, gender: Optional[str] = None) -> dict:
        """Generate passport owner information."""
        if gender is None:
            gender = self.random_element(["M", "F"])

        if gender == "M":
            first_name = self.generator.first_name_male()
        else:
            first_name = self.generator.first_name_female()

        return {
            "first_name": first_name,
            "last_name": self.generator.last_name(),
            "gender": gender,
            "date_of_birth": self.passport_dob_custom(),
            "place_of_birth": f"{self.generator.city()}, {self.generator.state_abbr()}",
        }