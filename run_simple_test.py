"""Simple test to verify the passport provider works"""
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from faker import Faker
from faker_passport.providers.passport_custom import Provider as PassportCustomProvider

# Create faker instance
fake = Faker()
fake.add_provider(PassportCustomProvider)

print("Testing Passport Provider...")
print("-" * 50)

# Test passport number
print("Passport Numbers:")
for i in range(3):
    print(f"  {i+1}: {fake.passport_number_custom()}")

print("\nDates of Birth:")
print(f"  Default: {fake.passport_dob_custom()}")
print(f"  Young Adult (21-35): {fake.passport_dob_custom(minimum_age=21, maximum_age=35)}")

print("\nPassport Owner Information:")
owner = fake.passport_owner_custom()
for key, value in owner.items():
    print(f"  {key}: {value}")

print("\nTest completed successfully!")
