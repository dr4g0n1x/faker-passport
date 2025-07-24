.. Faker Passport Provider documentation master file

Welcome to Faker Passport Provider's documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   providers/faker.providers.passport

Overview
--------

The Faker Passport Provider is an extension for the `Faker <https://faker.readthedocs.io/>`_ 
library that provides methods for generating realistic passport-related data.

Installation
------------

.. code-block:: bash

   pip install faker-passport

Quick Start
-----------

.. code-block:: python

   from faker import Faker
   from faker.providers.passport import Provider as PassportProvider

   fake = Faker()
   fake.add_provider(PassportProvider)

   # Generate passport data
   passport_number = fake.passport_number()
   date_of_birth = fake.passport_dob()
   owner_info = fake.passport_owner()

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
