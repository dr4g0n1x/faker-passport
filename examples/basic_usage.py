"""Basic usage examples for the Faker Passport Provider."""

from faker import Faker
from faker.providers.passport import Provider as PassportProvider

# Create a Faker instance
fake = Faker()

# Add the passport provider
fake.add_provider(PassportProvider)

# Example 1: Generate a passport number
print("=== Passport Numbers ===")
for i in range(5):
    print(f"Passport {i+1}: {fake.passport_number()}")

print("\n=== Dates of Birth ===")
# Example 2: Generate dates of birth with different age ranges
print(f"Adult (18-90): {fake.passport_dob()}")
print(f"Young adult (21-35): {fake.passport_dob(minimum_age=21, maximum_age=35)}")
print(f"Senior (65-85): {fake.passport_dob(minimum_age=65, maximum_age=85)}")

print("\n=== Passport Owner Information ===")
# Example 3: Generate complete passport owner information
owner1 = fake.passport_owner()
print(f"Random gender owner:")
for key, value in owner1.items():
    print(f"  {key}: {value}")

print("\nMale owner:")
male_owner = fake.passport_owner(gender='M')
for key, value in male_owner.items():
    print(f"  {key}: {value}")

print("\nFemale owner:")
female_owner = fake.passport_owner(gender='F')
for key, value in female_owner.items():
    print(f"  {key}: {value}")

# Example 4: Generate multiple passport records
print("\n=== Multiple Passport Records ===")
for i in range(3):
    print(f"\nPassport Record {i+1}:")
    print(f"  Number: {fake.passport_number()}")
    owner = fake.passport_owner()
    print(f"  Name: {owner['first_name']} {owner['last_name']}")
    print(f"  DOB: {owner['date_of_birth'].strftime('%Y-%m-%d')}")
    print(f"  Place of Birth: {owner['place_of_birth']}")
    print(f"  Gender: {owner['gender']}")
