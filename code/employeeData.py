from faker import Faker
import random

fake = Faker()

# Open a file for writing SQL queries
with open('employeeData.sql', 'w') as file:

    # Write SQL statements for creating the table

    # Write SQL statements for inserting fake data
    for _ in range(248):  # Assuming 500 employee records
        date_hired = fake.date()
        name = fake.name()
        password = fake.password()
        role = random.choice(
            ["Engineer", "Customer Support", "Stakeholder Relations", "Other"])
        # Assuming 10 different fields in the smart farm
        field_id = random.randint(1, 100)
        email = fake.email()
        phone = fake.phone_number()

        insert_query = f"""
        INSERT INTO Employee (DateHired, Name, Password, Role, FieldID, Email, Phone)
        VALUES ("{date_hired}", "{name}", "{password}", "{role}", {field_id}, "{email}", "{phone}");
        """

        file.write(insert_query)
