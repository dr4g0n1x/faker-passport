# Faker Passport Provider

A provider for [Faker](https://github.com/joke2k/faker) that generates realistic passport data.

## Installation

### From PyPI (when published)

```bash
pip install faker-passport
```

### For Development (Local Installation)

```bash
# Clone the repository
git clone https://github.com/dr4g0n1x/faker-passport.git
cd faker-passport

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

## Usage

```python
from faker import Faker
from faker_passport.providers.passport_custom import Provider as PassportCustomProvider

# Create faker instance
fake = Faker()

# Add passport provider
fake.add_provider(PassportCustomProvider)

# Generate passport number
print(fake.passport_number_custom())
# Output: 'FO137333'

# Generate date of birth
print(fake.passport_dob_custom(minimum_age=21, maximum_age=65))
# Output: datetime.datetime(1975, 8, 23, 0, 0)

# Generate complete passport owner information
owner = fake.passport_owner_custom()
print(owner)
# Output: {
#     'first_name': 'Michael',
#     'last_name': 'Sheppard',
#     'gender': 'M',
#     'date_of_birth': datetime.datetime(1981, 3, 17, 14, 31, 41),
#     'place_of_birth': 'Shelbyborough, CT'
# }
```

## Available Methods

### `passport_number_custom()`
Generates a random passport number following common passport number formats.

### `passport_dob_custom(minimum_age=18, maximum_age=90)`
Generates a date of birth suitable for a passport holder.

**Parameters:**
- `minimum_age` (int): Minimum age in years (default: 18)
- `maximum_age` (int): Maximum age in years (default: 90)

### `passport_owner_custom(gender=None)`
Generates complete passport owner information.

**Parameters:**
- `gender` (str, optional): Gender of the passport owner ('M' or 'F'). If None, randomly chosen.

**Returns:**
Dictionary containing:
- `first_name`: First name of the passport owner
- `last_name`: Last name of the passport owner
- `gender`: Gender ('M' or 'F')
- `date_of_birth`: Date of birth as datetime object
- `place_of_birth`: Place of birth (City, State)

## Development

### Setting Up Development Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Linux/Mac)
source venv/bin/activate

# Install the package in development mode
pip install -e .
```

### Running Tests

```bash
# Run unit tests
python -m unittest tests.test_passport_provider -v

# Or run the simple test script
python run_simple_test.py
```

### Project Structure

```
faker-passport/
├── faker_passport/
│   ├── __init__.py
│   └── providers/
│       ├── __init__.py
│       └── passport_custom/
│           └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_passport_provider.py
├── setup.py
├── README.md
└── run_simple_test.py
```

## License

This project is licensed under the MIT License.
