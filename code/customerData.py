from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('customerData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for _ in range(6759):
        country = fake.country()
        contact_name = fake.name()
        address = fake.address()
        city = fake.city()
        postal_code = fake.zipcode()
        phone = fake.phone_number()
        email = fake.email()

        insert_query = f"""
        INSERT INTO Customer (Country, ContactName, Address, City, PostalCode, Phone, Email)
        VALUES ("{country}", "{contact_name}", "{address}", "{city}", "{postal_code}", "{phone}", "{email}");
        """

        file.write(insert_query)
