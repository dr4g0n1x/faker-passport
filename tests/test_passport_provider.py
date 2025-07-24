import unittest
from datetime import datetime
from faker import Faker
from faker_passport.providers.passport_custom import Provider as PassportCustomProvider


class TestPassportProvider(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(PassportCustomProvider)
    
    def test_passport_number(self):
        """Test passport number generation."""
        for _ in range(10):
            passport_num = self.fake.passport_number_custom()
            self.assertIsInstance(passport_num, str)
            self.assertGreater(len(passport_num), 0)
            self.assertRegex(passport_num, r'^[A-Z0-9]+$')
    
    def test_passport_dob(self):
        """Test passport date of birth generation."""
        min_age = 25
        max_age = 65
        
        for _ in range(10):
            dob = self.fake.passport_dob_custom(minimum_age=min_age, maximum_age=max_age)
            self.assertIsInstance(dob, datetime)
            
            today = datetime.now()
            age = (today - dob).days / 365
            
            self.assertGreaterEqual(age, min_age - 1)
            self.assertLessEqual(age, max_age + 1)
    
    def test_passport_owner(self):
        """Test passport owner information generation."""
        owner = self.fake.passport_owner_custom()
        self.assertIsInstance(owner, dict)
        self.assertIn('first_name', owner)
        self.assertIn('last_name', owner)
        self.assertIn('gender', owner)
        self.assertIn('date_of_birth', owner)
        self.assertIn('place_of_birth', owner)
        self.assertIn(owner['gender'], ['M', 'F'])
        
        male_owner = self.fake.passport_owner_custom(gender='M')
        self.assertEqual(male_owner['gender'], 'M')
        
        female_owner = self.fake.passport_owner_custom(gender='F')
        self.assertEqual(female_owner['gender'], 'F')


if __name__ == '__main__':
    unittest.main()
